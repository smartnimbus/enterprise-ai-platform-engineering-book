import csv,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from lint_v2 import lint
ROOT=Path(__file__).resolve().parent.parent
TEXTS={
'T10':('# Chapter 16\nGateway approved the payout and released funds.','CH-016'),
'T11':('# Chapter 13\nThe latest CRM record is canonical truth; CLOSED wins.','CH-013'),
'T12':('# Chapter 13\nContext automatically resolves conflicting product states.','CH-013'),
'T14':('# Chapter 16\nThe Meridian fixture issued a cryptographically signed permission token.','CH-016'),
'T15':('# Chapter 16\nThe Semantic Context Control Plane owns these checks.','CH-016'),
'T16':('# Chapter 13\nThis chapter specifies the Gateway credential rotation implementation.','CH-013'),
'T17':('# Chapter 13: Identity Control Plane\nD-14','CH-013'),
'T19':('# Chapter 16\nMeridian synthetic MF-EVT-013 records a blocked direct-egress test; not production proof. D-18.','CH-016'),
'T20':('# Chapter 16\nThe Meridian fixture does not prove that all deployed networking rules block every route. D-18.','CH-016'),
'T21':('# Chapter 13\nMeridian synthetic `MF-EVD-RC-001` remains UNRESOLVED. D-14.','CH-013'),
'T22':('# Chapter 13\nContext is governed retrieval.','CH-013')}
class V2(unittest.TestCase):
    def test_baseline_undetected_mutations_now_block(self):
        for id in ('T10','T11','T12','T14','T15','T16','T17'):
            with self.subTest(id=id):
                t,ch=TEXTS[id];self.assertEqual(lint(ch,t)['status'],'BLOCK')
    def test_safe_variants_not_blocked(self):
        for id in ('T19','T20','T21','T22'):
            with self.subTest(id=id):
                t,ch=TEXTS[id];self.assertNotEqual(lint(ch,t)['status'],'BLOCK')
    def test_negation_window(self):
        self.assertEqual(lint('CH-016','# Chapter 16\nMeridian fixture does not prove production security. D-18')['counts']['BLOCK'],0)
    def test_strict_release_blocked_without_metadata(self):
        self.assertEqual(lint('CH-013','# Chapter 13: Context\nD-14',strict=True)['status'],'BLOCK')
    def test_invalid_id(self):
        self.assertEqual(lint('CH-013','# Chapter 13\nD-31 is true')['status'],'BLOCK')
    def test_unsafe_title(self):
        self.assertEqual(lint('CH-013','# Chapter 13: Gateway Control Plane')['status'],'BLOCK')
if __name__=='__main__':unittest.main(verbosity=2)
