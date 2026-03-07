import pandas as pd

df = pd.read_csv("../data/structured/daily_sales.csv")
print(df.columns)


def retrieve_sales_info(query):

    q = query.lower()

    if "total" in q or "revenue" in q:

        total = df["total_revenue"].sum()

        return f"Total revenue across dataset: {total:.2f}"

    if "average" in q:

        avg = df["total_revenue"].mean()

        return f"Average revenue per record: {avg:.2f}"

    if "top product" in q or "best selling" in q:

        top = (
            df.groupby("product_name")["units_sold"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        return "Top selling products:\n" + top.to_string()

    return df.head(10).to_string()