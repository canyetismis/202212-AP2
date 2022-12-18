import pyspark.sql.functions as F


def top_clients(join_clients):
    data = join_clients.groupBy(['client_id', 'client_name', 'parent_company_name'])\
        .agg(F.sum("transaction_volume").alias("total_transaction_volume"))\
        .orderBy(F.desc("total_transaction_volume"))
    return data
