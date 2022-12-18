def join_clients(filter_fintech, clients):
    data = filter_fintech.join(
        clients,
        on='client_id',
        how='left'
    )
    return data
