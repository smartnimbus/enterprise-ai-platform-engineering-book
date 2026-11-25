import json,unittest,tempfile,csv
from pathlib import Path
from build_twin import build,assess,impact,add_node,add_edge
SRC=Path('/mnt/data')
class TwinTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.nodes,cls.edges,cls.sources=build(SRC)
    def test_counts(self):
        self.assertEqual(len(self.nodes),315)
        self.assertEqual(sum(1 for x in self.nodes.values() if x['type']=='decision'),30)
        self.assertEqual(sum(1 for x in self.nodes.values() if x['type']=='chapter'),58)
        self.assertEqual(sum(1 for x in self.nodes.values() if x['type']=='article'),100)
        self.assertEqual(sum(1 for x in self.nodes.values() if x['type']=='pattern'),100)
    def test_no_dangling(self):self.assertEqual(assess(self.nodes,self.edges)['orphan_links'],0)
    def test_no_repeated_edges(self):self.assertEqual(assess(self.nodes,self.edges)['duplicate_edge_triplets'],0)
    def test_impact_d10(self):
        v=impact(self.nodes,self.edges,'D-10');self.assertGreater(v['count'],0)
        self.assertIn('KA-013',[x['id'] for x in v['dependent_candidates']])
    def test_impact_article(self):
        v=impact(self.nodes,self.edges,'KA-001');self.assertEqual(v['count'],0) # no invented dependants
    def test_no_approval_from_reference(self):
        self.assertFalse(any(x['type'] in {'approved_by','validates','implements','tested_by'} for x in self.edges))
    def test_no_source_elevation(self):
        self.assertTrue(all(x['status']=='OBSERVED_LOCAL_CANDIDATE' for x in self.nodes.values()))
    def test_duplicate_id_blocked(self):
        with self.assertRaises(ValueError):
            add_node(self.nodes,'D-10','decision','Duplicate',SRC/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv')
    def test_invalid_id_blocked(self):
        with self.assertRaises(ValueError):
            add_node({},'D-999','decision','Not registered',SRC/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv')
    def test_invalid_edge_blocked(self):
        with self.assertRaises(ValueError):
            add_edge([], 'D-10','KA-001','automatically_approved',SRC/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv','test')
    def test_deterministic_contents(self):
        n,e,_=build(SRC)
        self.assertEqual(json.dumps(self.nodes,sort_keys=True),json.dumps(n,sort_keys=True))
        self.assertEqual(json.dumps(self.edges,sort_keys=True),json.dumps(e,sort_keys=True))
    def test_source_sha64(self):self.assertTrue(all(len(n['source_sha256'])==64 for n in self.nodes.values()))
    def test_scenario_definitions_not_pass(self):self.assertEqual(assess(self.nodes,self.edges)['completed_validation_coverage'],'NOT_MEASURABLE_WITH_SOURCE_FILES')
if __name__=='__main__':unittest.main(verbosity=2)
