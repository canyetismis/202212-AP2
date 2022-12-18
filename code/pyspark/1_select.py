def select_clients(clients_master):
    clients = clients_master.select(
        'client_id',
        'client_name',
        'parent_company_id',
        'parent_company_name'
    ).collect()

    return clients
