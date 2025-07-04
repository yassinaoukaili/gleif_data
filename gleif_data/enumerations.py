from enum import Enum


class LEIIssuer(str, Enum):
    """
    Enumeration of known LEI Issuers and their unique identifiers.
    """

    CENTRAL_SECURITIES_CLEARING_SYSTEM_NIGERIA = '029200067A7K6CH0H586'
    CSD_SLOVAKIA = '097900BEFH0000000217'
    LONDON_STOCK_EXCHANGE = '213800WAVVOPS85N2205'
    NATIONAL_SETTLEMENT_DEPOSITORY_RUSSIA = '253400M18U5TB02TW421'
    DEPOZITARUL_CENTRAL_ROMANIA = '254900LXHEVKYGERER05'
    QATAR_CREDIT_BUREAU = '254900PMALKJRL1YGQ18'
    KDPW = '259400L3KBYEVNHEJF55'
    CSD_PRAGUE = '315700LK78Z7C0WMIL03'
    LEIL = '335800FVH4MOKZS9VH40'
    NATIONAL_SECURITIES_DEPOSITORY_LIMITED = '335800NFZPTMGTPAHE42'
    JAPAN_EXCHANGE_GROUP_TOKYO_STOCK_EXCHANGE = '353800279ADEFGKNTV65'
    STRATE = '378900F4A0A690EA6735'
    BUNDESANZEIGER_VERLAG = '39120001KULK7200U106'
    TUNISIE_CLEARING = '4117IB8J63IUO2SES575'
    GS1_MEXICO = '4469000001AVO26P9X86'
    NASDAQ_LEI = '485100001PLJJ09NZT59'
    KDD_CENTRAL_SECURITIES_CLEARING_CORPORATION = '48510000JZ17NWGUA510'
    FEDERAL_STATISTICAL_OFFICE = '506700LOLO7M6V0E4247'
    WM_DATENSERVICE = '5299000J2N45DDNE4Y28'
    GS1 = '52990034RLKT0WSOAM90'
    EQS = '529900F6BNUR3RJ2WH29'
    UBISURE_RAPIDLEI = '529900T8BM49AURSDO55'
    BLOOMBERG = '5493001KJTIIGC8Y1R12'
    NORDLEI = '549300O897ZC5H7CY412'
    SACB_MOARIF = '558600FNC30A8J9EGQ54'
    EURONEXT_DUBLIN = '635400DZBUIMTBCXGA12'
    BEIJING_NATIONAL_INSTITUTE_OF_FINANCIAL_STANDARDIZATION = '655600IJ8LS3CCDA4421'
    KVK_NETHERLANDS_CHAMBER_OF_COMMERCE = '724500A93Z8V1MJK5349'
    FINNISH_PATENT_AND_REGISTRATION_OFFICE_PRH = '743700OO8O2N3TQKJC81'
    ZAGREB_STOCK_EXCHANGE_ZSE = '7478000050A040C0D041'
    TAKASBANK = '789000TVSB96MCOKSB52'
    INFOCAMERE = '815600EAD78C57FCE690'
    INFOCERT_SPA = '815600F58F7382929F40'
    XERIUS = '894500IIP432AHQ64V02'
    CORPME = '959800R2X69K6Y6MX775'
    INSEE = '969500Q2MA9VBQ8BG884'
    UNILEI = '98450045AN5EB5FDC780'
    KSD = '9884008RRMX1X5HV6625'
    GMEI_UTILITY = 'EVK05KS7XY1DEII3R011'


class RegistrationStatus(str, Enum):
    """
    Enumerations of registration statuses
    """

    ISSUED = 'ISSUED'
    LAPSED = 'LAPSED'
    ANNULLED = 'ANNULLED'
    PENDING_TRANSFER = 'PENDING_TRANSFER'
    PENDING_ARCHIVAL = 'PENDING_ARCHIVAL'
    DUPLICATE = 'DUPLICATE'
    RETIRED = 'RETIRED'
    MERGED = 'MERGED'
