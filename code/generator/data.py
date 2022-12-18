import pandas as pd
import os


class Data:

    def __init__(self):
        # modify these according to your need
        _name_separators = [
            ' und ',
            ' & ',
            ' u. '
        ]

        _legal_suffixes_short = [
            ' AG',
            ' A.G',
            ' A.G.',
            ' KG',
            ' K.G',
            ' K.G.',
            ' GmbH',
            ' GMBH',
            ' G.m.b.H.',
            ' G.M.B.H.',
            ' GmbH & Co. KG',
            ' GmbH und Co. KG',
            ' GmbH u. Co. KG',
            ' AG & Co. KG',
            ' A.G. & Co. KG',
            ' AG und Co. KG',
            ' AG u. Co. KG',
            ' OHG',
            ' O.H.G',
            ' O.H.G.',
        ]

        _legal_suffixes_long = [
            ' Aktiengesellschaft',
            'Aktiengesellschaft',
            ' Kommanditgesellschaft',
            'Kommanditgesellschaft',
            ' Gesellschaft mit beschränkter Haftung',
            'Gesellschaft mit beschränkter Haftung',
            ' Gesellschaft mbH',
            'Gesellschaft mbH',
            ' Gesellschaft M.B.H.',
            'Gesellschaft M.B.H.',
            ' Offene Handelsgesellschaft',
            'Offene Handelsgesellschaft',
        ]

        _parent_companies = [
            'NOKIC SCHWERINDUSTRIE GROUP GMBH',
            'THOMAS ANDERS UND SOHN AG',
            'DIETER UND BOHLEN GMBH',
            'DEUTSCHMANN HOLDING AG'
        ]

        _bank_names = [
            'COMMERZBANK',
            'SANTANDER',
            'DEUTSCHE BANK',
        ]

        _fintech_names = [
            'N26',
            'REVOLUT',
            'WISE',
        ]

        # dataframes are made in here
        cwd = os.getcwd()
        self.surnames = pd.read_csv(
            f'{cwd}/generator/surname_data/surnames.csv')
        self.name_separators = pd.DataFrame(
            _name_separators, columns=['separator'])
        self.legal_suffixses_short = pd.DataFrame(
            _legal_suffixes_short, columns=['legal_suffix'])
        self.legal_suffixes_long = pd.DataFrame(
            _legal_suffixes_long, columns=['legal_suffix'])
        self.parent_companies = pd.DataFrame(
            _parent_companies, columns=['parent_company'])
        self.bank_names = pd.DataFrame(_bank_names, columns=['bank_name'])
        self.fintech_names = pd.DataFrame(
            _fintech_names, columns=['fintech_name'])
