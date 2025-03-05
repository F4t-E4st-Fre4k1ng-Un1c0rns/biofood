import pandas as pd
from prophet import Prophet
from datetime import date
from math import ceil


def analyze_sales(data: dict[str, date | float]) -> list[dict[str, date | float]]:
    df = pd.DataFrame.from_dict(data)
    df["ds"] = pd.to_datetime(df["date"])
    df["y"] = df["sales"]
    for column in df.columns:
        df = df.fillna({column: 0})

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    return [
        {
            "ds": row["ds"].to_pydatetime().date(),
            "yhat_lower": ceil(row["yhat_lower"]),
            "yhat_upper": ceil(row["yhat_upper"]),
            "yhat": ceil(row["yhat"]),
        }
        for _index, row in forecast.iterrows()
    ]
