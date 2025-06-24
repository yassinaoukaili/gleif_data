from .models import LeiRecordFilter, CompanyAttributes
from urllib.parse import urlparse, parse_qs, urlencode
from typing import Union, List
import requests
import pandas as pd


class GleifData:

    BASE_URL = "https://api.gleif.org/api/v1/lei-records"

    FILTER_MAP = {
        "city": "filter[entity.addresses.city]",
        "country": "filter[entity.addresses.country]",
        "postal_code": "filter[entity.addresses.postalCode]",
        "legal_form": "filter[entity.legalForm]",
        "status": "filter[registration.status]",
        "lei_issuer": "filter[registration.managingLou]",
    }

    @classmethod
    def _build_url(cls, filters: LeiRecordFilter) -> str:

        """
        Build the query URL with filters encoded.
        Raises ValueError if no filters are provided.
        """

        raw_params = filters.model_dump()
        query_params = {}

        for key, value in raw_params.items():
            if value is not None and key in cls.FILTER_MAP:
                query_params[cls.FILTER_MAP[key]] = value.value if hasattr(value, 'value') else value

        if not any(k.startswith("filter[") for k in query_params):
            raise ValueError("At least one filter must be provided.")

        return f"{cls.BASE_URL}?{urlencode(query_params)}"

    @staticmethod
    def _get_last_page(links: dict) -> int:

        """
        Parse the pagination to get the last page number.
        """

        try:
            last_page = parse_qs(urlparse(links['last']).query)['page[number]'][0]
            return int(last_page)
        except (KeyError, ValueError, IndexError):
            return 1

    @staticmethod
    def _build_company_attributes(company: dict) -> dict:

        """
        Extract and structure company attributes from API response.
        """

        return {**company['attributes']['entity'], 'lei': company['attributes']['lei']}

    @classmethod
    def get_companies(cls, filters: LeiRecordFilter) -> List[CompanyAttributes]:

        """
        Get a list of companies matching the filter criteria.
        """

        url = cls._build_url(filters)
        response = requests.get(url)
        if not response.ok:
            raise requests.HTTPError(f"Request failed [{response.status_code}]: {response.text}")

        res = response.json()
        last_page = cls._get_last_page(res.get('links', 1))
        next_page = res['links'].get('first')
        data_dicts = []

        for _ in range(1, last_page+1):
            response = requests.get(next_page)

            if not response.ok:
                continue

            res = response.json()
            data_dicts.extend(res.get('data', []))
            next_page = res['links'].get('next')

            if not next_page:
                break

        return [CompanyAttributes(**cls._build_company_attributes(c)) for c in data_dicts]

    @classmethod
    def get_companies_df(cls, filters: LeiRecordFilter) -> pd.DataFrame:

        """
        Return company data as a concatenated pandas DataFrame.
        """

        companies = cls.get_companies(filters)
        dfs = [pd.json_normalize(c.model_dump(), sep='_') for c in companies]
        return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

    @classmethod
    def _single_search(cls, lei: str) -> Union[pd.DataFrame, None]:

        """
        Retrieve a single company by its LEI and return as DataFrame.
        """

        url = f"{cls.BASE_URL}/{lei}"
        response = requests.get(url)
        if not response.ok:
            return None

        res = response.json()
        data = res.get('data')
        if not data:
            return None

        company = CompanyAttributes(**cls._build_company_attributes(data))
        return pd.json_normalize(company.model_dump(), sep='_')

    @classmethod
    def search(cls, lei: Union[str, List[str]]) -> pd.DataFrame:

        """
        Search for one or more LEI records and return results as DataFrame.
        """

        if isinstance(lei, str):
            df = cls._single_search(lei)
            return df if df is not None else pd.DataFrame()

        if isinstance(lei, list):
            dfs = [cls._single_search(l) for l in lei]
            return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

        raise TypeError("LEI must be a string or a list of strings.")
