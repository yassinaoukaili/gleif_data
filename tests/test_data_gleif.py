import unittest
from gleif_data import GleifData
from gleif_data.models import LeiRecordFilter
import pandas as pd
from pydantic import ValidationError


class TestGleifData(unittest.TestCase):
    def setUp(self):
        self.filters = LeiRecordFilter(legal_form='CDOV', country='AG', status='LAPSED')
        self.response_dict = {"type": "lei-records", "id": "529900FCMZ4LKXFD0R69",
                              "attributes": {"lei": "529900FCMZ4LKXFD0R69",
                                             "entity": {"legalName": {"name": "AIRBUS", "language": "en"},
                                                        "otherNames": [], "transliteratedOtherNames": [],
                                                        "legalAddress": {"language": "fr", "addressLines": [
                                                            "2 \u00c9TOLE DEWOITINE POINT ROUND"],
                                                                         "addressNumber": None,
                                                                         "addressNumberWithinBuilding": None,
                                                                         "mailRouting": None,
                                                                         "city": "BLAGNAC", "region": "FR-OCC",
                                                                         "country": "FR",
                                                                         "postalCode": "31700"},
                                                        "headquartersAddress": {"language": "fr",
                                                                                "addressLines": [
                                                                                    "2 \u00c9TOLE DEWOITINE POINT ROUND"],
                                                                                "addressNumber": None,
                                                                                "addressNumberWithinBuilding": None,
                                                                                "mailRouting": None,
                                                                                "city": "BLAGNAC",
                                                                                "region": "FR-OCC",
                                                                                "country": "FR",
                                                                                "postalCode": "31700"},
                                                        "registeredAt": {"id": "RA000192", "other": None},
                                                        "registeredAs": "383 474 814", "jurisdiction": "FR",
                                                        "category": "GENERAL",
                                                        "legalForm": {"id": "6CHY", "other": None},
                                                        "associatedEntity": {"lei": None, "name": None},
                                                        "status": "ACTIVE",
                                                        "expiration": {"date": None, "reason": None},
                                                        "successorEntity": {"lei": None, "name": None},
                                                        "successorEntities": [],
                                                        "creationDate": "1991-11-04T00:00:00Z",
                                                        "subCategory": None, "otherAddresses": [],
                                                        "eventGroups": []}, "registration": {
                                      "initialRegistrationDate": "2013-10-15T15:03:24Z",
                                      "lastUpdateDate": "2024-10-21T14:09:20Z", "status": "ISSUED",
                                      "nextRenewalDate": "2025-12-13T00:00:00Z",
                                      "managingLou": "213800WAVVOPS85N2205",
                                      "corroborationLevel": "FULLY_CORROBORATED",
                                      "validatedAt": {"id": "RA000192", "other": None},
                                      "validatedAs": "383 474 814", "otherValidationAuthorities": []},
                                             "bic": ["AIRBFR22XXX"], "mic": None, "ocid": "fr\/383474814",
                                             "qcc": "QFR8B4D42P", "spglobal": ["565710"],
                                             "conformityFlag": "CONFORMING"}, "relationships": {
                "managing-lou": {"links": {
                    "related": "https:\/\/api.gleif.org\/api\/v1\/lei-records\/529900FCMZ4LKXFD0R69\/managing-lou"}},
                "lei-issuer": {"links": {
                    "related": "https:\/\/api.gleif.org\/api\/v1\/lei-records\/529900FCMZ4LKXFD0R69\/lei-issuer"}},
                "field-modifications": {"links": {
                    "related": "https:\/\/api.gleif.org\/api\/v1\/lei-records\/529900FCMZ4LKXFD0R69\/field-modifications"}},
                "direct-parent": {"links": {
                    "reporting-exception": "https:\/\/api.gleif.org\/api\/v1\/lei-records\/529900FCMZ4LKXFD0R69\/direct-parent-reporting-exception"}},
                "ultimate-parent": {"links": {
                    "reporting-exception": "https:\/\/api.gleif.org\/api\/v1\/lei-records\/529900FCMZ4LKXFD0R69\/ultimate-parent-reporting-exception"}}},
                              "links": {
                                  "self": "https:\/\/api.gleif.org\/api\/v1\/lei-records\/529900FCMZ4LKXFD0R69"}}

    def test_invalid_search_input(self):
        with self.assertRaises(TypeError):
            GleifData.search(6876783287)

    def test_invalid_filter_raises(self):
        with self.assertRaises(ValidationError):
            LeiRecordFilter()

    def test_search_lei(self):
        df = GleifData.search('529900FCMZ4LKXFD0R69')
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_url_building(self):
        GleifData._build_url(self.filters)

    def test_build_company_attributes(self):
        GleifData._build_company_attributes(self.response_dict)

    def test_get_companies(self):
        companies = GleifData.get_companies(self.filters)
        self.assertTrue(companies, list)

    def test_get_companies_df(self):
        df = GleifData.get_companies_df(self.filters)
        self.assertTrue(isinstance(df, pd.DataFrame))


if __name__ == '__main__':
    unittest.main()
