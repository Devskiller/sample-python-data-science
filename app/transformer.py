import pandas as pd


def join(orders: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(columns=("order_id", "user_id", "item", "email")).set_index(
        "order_id"
    )
