from random import random
import random
import pandas as pd
from .data import Data
from datetime import date, timedelta

data = Data()
rand_generator = random

#"public functions"


def generate_clients_table(n: int = 100, parent_company_percent: int = 50, seed: int = 123):
    rand_generator.seed(seed)
    rand = rand_generator

    # generate client data
    client_id = []
    client_name = []

    for i in range(0, n):
        client_id.append(i+1)
        client_name.append(generate_random_company())

    # generate parent company data
    parent_companies = data.parent_companies
    parent_company_id_list = []
    parent_company_name_list = []

    for i in range(0, len(parent_companies)):
        parent_company_id_list.append(i+1)
        parent_company_name_list.append(
            parent_companies._get_value(i, 'parent_company'))

    # generate clients table
    parent_company_id = []
    parent_company_name = []
    for i in range(0, n):
        if (rand.randint(0, 100) <= parent_company_percent):
            index = rand.randint(0, len(parent_companies)-1)
            parent_company_id.append(parent_company_id_list[index])
            parent_company_name.append(parent_company_name_list[index])
        else:
            parent_company_id.append(0)
            parent_company_name.append(None)

    data_vals = {
        'client_id': client_id,
        'client_name': client_name,
        'parent_company_id': parent_company_id,
        'parent_company_name': parent_company_name
    }

    return pd.DataFrame(data=data_vals)


def generate_transactions_table(clients: pd.DataFrame, n: int = 1000, start_date: date = date(2018, 1, 1), end_date: date = date(2021, 12, 31)):
    client_ids = clients['client_id'].tolist()
    finttech_names = data.fintech_names['fintech_name'].tolist()
    bank_names = data.bank_names['bank_name'].tolist()
    rand = rand_generator

    # generate transactions table
    client_id = []
    transaction_volume = []
    correspondant_name = []
    correspondant_bank_name = []
    date = []
    direction = []

    for i in range(0, n):

        id = rand.randint(0, len(client_ids)-1)
        client_id.append(client_ids[id])
        transaction_volume.append(rand.randint(10, 50)*1000)
        date.append(generate_random_date(start_date, end_date))

        # 40% chance that it is a transaction to company's other bank account
        if (rand.randint(0, 100) <= 40):
            correspondant_name.append(clients._get_value(id, 'client_name'))
        else:
            correspondant_name.append(generate_random_company())

        # 30% chance that it is a transaction to a fintech account
        if (rand.randint(0, 100) <= 30):
            correspondant_bank_name.append(
                finttech_names[rand.randint(0, len(finttech_names)-1)])
        else:
            correspondant_bank_name.append(
                bank_names[rand.randint(0, len(bank_names)-1)])

        # 50% chance that it is an outgoing transaction:
        if (rand.randint(0, 100) <= 50):
            direction.append("out")
        else:
            direction.append("in")

    data_vals = {
        'client_id': client_id,
        'transaction_volume': transaction_volume,
        'correspondant_name': correspondant_name,
        'correspondant_bank_name': correspondant_bank_name,
        'date': date,
        'direction': direction
    }

    return pd.DataFrame(data=data_vals)

# "private" functions


def generate_random_company():
    rand = rand_generator
    surnames = data.surnames
    name_separators = data.name_separators
    legal_suffixes_long = data.legal_suffixes_long
    legal_suffixes_short = data.legal_suffixses_short

    # randomly select a surname
    # some companies have two partners, based on observation this has a 30% chance happening
    if (rand.randint(0, 100) <= 30):
        name1 = surnames._get_value(rand.randint(
            0, len(surnames.index)-1), 'surname')
        separator = name_separators._get_value(random.randint(
            0, len(name_separators.index)-1), 'separator')
        name2 = surnames._get_value(rand.randint(
            0, len(surnames.index)-1), 'surname')

        company_name = name1 + separator + name2
    else:
        company_name = surnames._get_value(
            rand.randint(0, len(surnames.index)-1), 'surname')

    # randomly select a legal suffix
    # some instances will have long names, based on observation this has a 15% chance of hapening
    if (rand.randint(0, 100) <= 15):
        legal_suffix = legal_suffixes_long._get_value(rand.randint(
            0, len(legal_suffixes_long.index)-1), 'legal_suffix')
    else:
        legal_suffix = legal_suffixes_short._get_value(rand.randint(
            0, len(legal_suffixes_short.index)-1), 'legal_suffix')

    return company_name + legal_suffix


def generate_random_date(start_date: date, end_date: date):
    rand = rand_generator

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = rand.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date
