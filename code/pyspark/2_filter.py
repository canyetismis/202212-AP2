import pyspark.sql.functions as F


def filter_direction_date(select_transactions):
    trx = select_transactions.filter(
        (F.col('direction') == 'out') &
        (F.col('date') <= '2020-12-31')
    )

    return trx
