#!/usr/bin/env python3
import unittest
from validate_ai_change import check

BASE={"work_item":"EX-006","agent_id":"ai-contributor-001","human_sponsor":"human-task-owner","repository":"owner/repo","base_sha":"b38854ba1386b587ad8c31ef007f4bc7bdbe82a1","allowed_paths":["automation/tests/**","examples/synthetic/**"],"forbidden_paths":["meridian/fixture/**"],"lease_status":"ACTIVE"}
class Test(unittest.TestCase):
    def test_good(self): self.assertEqual(check(BASE,["automation/tests/test.py"]),[])
    def test_out_of_scope(self): self.assertTrue(check(BASE,["manuscript/chapter-13.md"]))
    def test_frozen(self): self.assertTrue(check(BASE,["meridian/fixture/01-context-manifest.json"]))
    def test_root_governance(self): self.assertTrue(check(BASE,["REPOSITORY-GOVERNANCE.md"]))
    def test_relative_escape(self): self.assertTrue(check(BASE,["automation/tests/../../secrets.env"]))
    def test_lease_not_active(self): self.assertTrue(check(dict(BASE,lease_status="EXPIRED"),["automation/tests/a.py"]))
    def test_conflict(self):
        claim={"work_item":"EX-002","allowed_paths":["automation/tests/**"],"lease_status":"ACTIVE"}
        self.assertTrue(check(BASE,["automation/tests/a.py"],[claim]))
    def test_no_conflict_same_item(self):
        claim={"work_item":"EX-006","allowed_paths":["automation/tests/**"],"lease_status":"ACTIVE"}
        self.assertFalse(check(BASE,["automation/tests/a.py"],[claim]))
    def test_duplicate_paths(self): self.assertTrue(check(BASE,["automation/tests/a.py","automation/tests/a.py"]))
    def test_missing_sponsor(self): self.assertTrue(check(dict(BASE,human_sponsor=""),["automation/tests/a.py"]))
    def test_invalid_sha(self): self.assertTrue(check(dict(BASE,base_sha="x"),["automation/tests/a.py"]))
if __name__ == "__main__": unittest.main(verbosity=2)
