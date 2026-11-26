import unittest
from pathlib import Path
from lint_manuscript import lint
BASE=Path(__file__).resolve().parent
class LintTests(unittest.TestCase):
 def assertBlocked(self,s,chapter='CH-013'):self.assertEqual(lint(chapter,s)['status'],'BLOCK')
 def test_a_clean(self):self.assertEqual(lint('CH-013',(BASE/'PILOT-A-CH13-D14.md').read_text())['status'],'DRAFT_LINT_PASS_NOT_APPROVED')
 def test_b_clean(self):self.assertEqual(lint('CH-016',(BASE/'PILOT-B-CH16-D10-D18.md').read_text())['status'],'DRAFT_LINT_PASS_NOT_APPROVED')
 def test_unknown_decision(self):self.assertBlocked('# Title\nD-31 proposes another control')
 def test_unknown_chapter(self):self.assertBlocked('# Title\nCH-099 is important')
 def test_fake_meridian_event(self):self.assertBlocked('# Title\nMeridian synthetic MF-EVT-999 event')
 def test_legacy_layer(self):self.assertBlocked('# Title\nLayer 6 handles security')
 def test_legacy_plane(self):self.assertBlocked('# Title\nsecurity plane grants approval')
 def test_context_wrong_authority(self):self.assertBlocked('# Title\nContext authorizes payment mutations')
 def test_gateway_wrong_reconciliation(self):self.assertBlocked('# Title\nGateway reconciles product records')
 def test_refund_posted(self):self.assertBlocked('# Title\nMeridian refund was posted successfully')
 def test_production_claim(self):self.assertBlocked('# Title\nMeridian fixture proves production network enforcement')
 def test_conflict_resolved(self):self.assertBlocked('# Title\nRetail CRM conflict resolved')
 def test_delegation_widened(self):self.assertBlocked('# Title\nrefund:request implies refund:execute')
 def test_no_evidence_grade(self):self.assertBlocked('# Title\nD-14 MF-EVD-RC-001 unresolved')
 def test_negated_context_authority(self):self.assertEqual(lint('CH-013','# Title\nContext does not authorize payment mutations. D-14.')['counts']['BLOCK'],0)
 def test_negated_gateway_reconcile(self):self.assertEqual(lint('CH-016','# Title\nGateway does not reconcile product records. D-10.')['counts']['BLOCK'],0)
 def test_release_report_reference(self):self.assertEqual(lint('CH-016','# Chapter 16: Gateway Control Plane\nSynthetic MF-EVD-RG-001 records blocked promotion. D-10.')['counts']['BLOCK'],0)
 def test_invalid_chapter(self):self.assertBlocked('# Title\nD-14','CH-999')
 def test_missing_title(self):self.assertBlocked('Meridian synthetic D-14 example')
if __name__=='__main__':unittest.main(verbosity=2)
