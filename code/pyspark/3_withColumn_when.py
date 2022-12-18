import pyspark.sql.functions as F


def mark_fintech(filter_direction_date):
    trx = filter_direction_date.withColumn(
        "is_FinTech",
        F.when(
            ((F.col('correspondant_bank_name') == 'N26') |
             (F.col('correspondant_bank_name') == 'WISE') |
             (F.col('correspondant_bank_name') == 'REVOLUT')),
            1
        ).otherwise(0)
    )
    return trx
