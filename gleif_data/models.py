import pandas as pd
from pydantic import BaseModel, AfterValidator
from typing import Optional, List, Annotated
from pydantic_extra_types.country import CountryAlpha2
from pathlib import Path

from .enumerations import RegistrationStatus, LEIIssuer


def is_legal_form_valid(legal_form: str) -> str:
    """
    Validate if the legal form is in the ISO 20275 ELF code list.
    """

    try:
        path_df = Path(__file__).parent / 'data' / 'elf_code_list_publication.csv'
        df = pd.read_csv(path_df)
        elf_codes = set(df.elf_code.str.upper())

    except FileNotFoundError:
        raise FileNotFoundError("Missing ELF code list CSV file: 'elf_code_list_publication.csv'")

    if legal_form.upper() not in elf_codes:
        raise ValueError(
            f"'{legal_form}' is not a valid legal form. Ensure it complies with ISO 20275. "
            f"See: https://www.gleif.org/en/lei-data/code-lists/iso-20275-entity-legal-forms-code-list"
        )
    return legal_form


def is_registration_status_valid(status: str):
    """
    Validate if the registration status is one of the accepted values.
    """

    valid_statuses = [s.value for s in RegistrationStatus]

    if status.upper() not in valid_statuses:
        raise ValueError(f"'{status}' is not a valid registration status. Allowed: {valid_statuses}")
    return status


def is_lei_issuer_valid(lei_issuer: str):
    """
    Validate if the LEI issuer is one of the accepted values.
    """

    valid_issuers = [s.value for s in LEIIssuer]
    if lei_issuer.upper() not in valid_issuers:
        raise ValueError(f"'{lei_issuer}' is not a valid registration status. Allowed: {valid_issuers}")
    return lei_issuer


class LeiRecordFilter(BaseModel):
    """
    Filter model for LEI records.
    """

    country: Optional[CountryAlpha2] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    legal_form: Annotated[str, AfterValidator(is_legal_form_valid)]
    status: Optional[Annotated[str, AfterValidator(is_registration_status_valid)]] = None
    lei_issuer: Optional[str] = None


class LegalName(BaseModel):
    """
    Represents a legal name with associated language.
    """

    name: str
    language: str


class Address(BaseModel):
    """
    Represents an address with optional and mandatory fields.
    """

    language: str
    addressLines: List[str]
    addressNumber: Optional[str] = None
    addressNumberWithinBuilding: Optional[str] = None
    mailRouting: Optional[str] = None
    city: str
    region: Optional[str] = None
    country: str
    postalCode: Optional[str] = None


class RegisteredAt(BaseModel):
    """
    Entity's registration authority details.
    """

    id: str
    other: Optional[str] = None


class LegalForm(BaseModel):
    """
    Entity's legal form identifier.
    """

    id: str


class SuccessorEntity(BaseModel):
    """
    Optional successor entity info, if LEI was transferred.
    """

    lei: Optional[str] = None
    name: Optional[str] = None


class CompanyAttributes(BaseModel):
    """
    Main attributes describing an LEI-registered entity.
    """

    lei: str
    legalName: Optional[LegalName] = None
    legalAddress: Optional[Address] = None
    headquartersAddress: Optional[Address] = None
    registeredAt: Optional[RegisteredAt] = None
    registeredAs: Optional[str] = None
    jurisdiction: Optional[str] = None
    category: Optional[str] = None
    legalForm: Optional[LegalForm] = None
    status: Optional[str] = None
