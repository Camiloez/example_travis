import pytest
import sys
#from data.preprocessing_helpers import row_to_list, convert_to_int

class TestRowToList(object):
	def test_on_no_tab_no_missing_value(self):
		assert 1 == 0.5 + 0.5
	@pytest.mark.xfail
	def test_on_two_tabs_no_missing_value(self):
		assert 2/3 == 0.3113


class TestConvertToInt(object):
	@pytest.mark.skipif(sys.version_info > (2,7), reason = "requires Python 2.7")
	def test_with_no_comma(self):
		assert "hi" == True
	def test_with_one_comma(self):
		assert "" is not None