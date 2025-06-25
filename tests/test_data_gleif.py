import unittest
from gleif_data import GleifData
from gleif_data.models import LeiRecordFilter, CompanyAttributes
import pandas as pd
from pydantic import ValidationError


class TestGleifData(unittest.TestCase):

    def test_invalid_search_input(self):
        with self.assertRaises(TypeError):
            GleifData.search(6876783287)

    def test_invalid_filter_raises(self):
        with self.assertRaises(ValidationError):
            filters = LeiRecordFilter()

    def test_search_lei(self):
        df = GleifData.search('529900FCMZ4LKXFD0R69')
        self.assertTrue(isinstance(df, pd.DataFrame))


if __name__ == '__main__':
    unittest.main()
