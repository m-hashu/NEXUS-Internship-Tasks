import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load cleaned dataset from Task 1
df = pd.read_csv("data/OnlineRetail_clean.csv", parse_dates=["InvoiceDate"], encoding="ISO-8859-1",dtype={"InvoiceNo": str})

# Create base aggregations
df["Month"] = df["InvoiceDate"].dt.to_period("M").dt.to_timestamp()
df["Hour"] = df["InvoiceDate"].dt.hour

# App setup
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Online Retail Dashboard", style={"textAlign": "center"}),

    # Dropdown for country selection
    html.Div([
        html.Label("Select Country:"),
        dcc.Dropdown(
            id="country-filter",
            options=[{"label": c, "value": c} for c in sorted(df["Country"].unique())],
            value="United Kingdom",  # default
            clearable=False
        )
    ], style={"width": "50%", "margin": "auto"}),

    # Charts
    dcc.Graph(id="monthly-sales"),
    dcc.Graph(id="top-products"),
    dcc.Graph(id="hourly-sales"),
])

# Callbacks for interactivity
@app.callback(
    [Output("monthly-sales", "figure"),
     Output("top-products", "figure"),
     Output("hourly-sales", "figure")],
    [Input("country-filter", "value")]
)
def update_charts(selected_country):
    dff = df[df["Country"] == selected_country]

    # Monthly sales
    monthly = dff.groupby("Month")["Sales"].sum().reset_index()
    fig_monthly = px.line(monthly, x="Month", y="Sales", title=f"Monthly Sales - {selected_country}")

    # Top 10 products
    top_products = (
        dff.groupby("Description")["Sales"]
        .sum()
        .nlargest(10)
        .reset_index()
    )
    fig_products = px.bar(
        top_products, x="Sales", y="Description",
        orientation="h", title=f"Top 10 Products - {selected_country}"
    )

    # Hourly sales pattern
    hourly = dff.groupby("Hour")["Sales"].sum().reset_index()
    fig_hourly = px.bar(hourly, x="Hour", y="Sales", title=f"Sales by Hour - {selected_country}")

    return fig_monthly, fig_products, fig_hourly

if __name__ == "__main__":
    app.run(debug=True)
