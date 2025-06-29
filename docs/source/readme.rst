GleifData
=========

``GleifData`` is a Python class that interfaces with the `GLEIF API <https://www.gleif.org/en/about-lei/open-data/gleif-api>`_ to retrieve legal entity data (LEI records). It supports filtering, and structured output via Pydantic models and pandas.

Features
--------

- Query LEI records using filters such as city, country, postal code, legal form, status, and LEI issuer.
- Retrieve results and combine them into a list or a pandas DataFrame.
- Perform single or bulk LEI lookups.
- Structured output using custom Pydantic models or Pandas DataFrame.

----

Usage
-----

Filtered LEI list, output as a pandas dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from gleif_data import GleifData, LeiRecordFilter

    filters = LeiRecordFilter(city="Paris", country="FR", legal_form="1GNM")
    df = GleifData.get_companies_df(filters)

    display(df.head())

Direct search for single or multiple LEIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Function takes as input either a single LEI as string or multiple LEIs as a list of strings

.. code-block:: python

    from gleif_data import GleifData

    list_leis = ["529900FCMZ4LKXFD0R69", "635400FHLYLDBRFWIX09", "635400BR2ROC1FVEBQ56"]
    df = GleifData.search(list_leis)

    display(df)

List of ``CompanyAttribues`` objects for OOP implementations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from gleif_data import GleifData, LeiRecordFilter

    filters = LeiRecordFilter(city="Roma", postal_code="00199")
    companies = GleifData.get_companies(filters)

    for company in companies:
        print(company.lei, company.legalName.name, company.legalAddress.addressLines)

----

Acknowledgments
---------------

Data provided by GLEIF. This project is not affiliated with or endorsed by GLEIF.

Contributions
------------

Contributions are welcome! If you’d like to suggest a feature, fix a bug, or improve the documentation, feel free to open an issue or submit a pull request. Please make sure your changes are well-tested and follow the style of the existing code.
