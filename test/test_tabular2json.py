import pytest
from app import tab2json as t2j

def test_parse_line():
  typical_line = "-rw-rw-r-- 1 someuser somegroup 35149 Aug  4 09:25 somefile\n"
  target = ["-rw-rw-r--", "1", "someuser", "somegroup", "35149", "Aug",  "4", "09:25", "somefile"]
  assert t2j.parse_line(typical_line) == target
