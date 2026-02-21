import pandas as pd

def generate_kpis(df):
    kpis = {}
    num_cols = df.select_dtypes(include="number").columns

    if len(num_cols) > 0:
        col = num_cols[0]
        kpis[f"Average {col}"] = round(df[col].mean(), 2)
        kpis[f"Max {col}"] = df[col].max()
        kpis[f"Min {col}"] = df[col].min()

    kpis["Total Records"] = df.shape[0]
    return kpis


def executive_summary(df):
    rows, cols = df.shape
    num_cols = df.select_dtypes(include="number").columns

    summary = f"This dataset contains {rows} rows and {cols} columns."

    if len(num_cols) > 0:
        col = num_cols[0]
        summary += f" The average {col} is {round(df[col].mean(),2)}."

    return summary


def explain_chart(plot_df, x_col, y_col):
    top = plot_df.sort_values(y_col, ascending=False).iloc[0]
    return f"Highest {y_col} is {top[y_col]} for {x_col} = {top[x_col]}."


def recommend_chart(x_series, y_series):
    if pd.api.types.is_numeric_dtype(y_series):
        return "bar"
    return "bar"
