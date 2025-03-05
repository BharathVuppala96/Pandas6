import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df=store[store['amount']>500]
    rich=len(set(df['customer_id']))
    return pd.DataFrame([rich],columns=['rich_count'])

    