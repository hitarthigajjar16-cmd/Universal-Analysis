import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px
from intelligence import generate_kpis, executive_summary, explain_chart, recommend_chart

st.set_page_config(page_title="Universal Analytics Dashboard", layout="wide")

USERS_FILE = "users.json"

# ---------------------------
# USER MANAGEMENT
# ---------------------------
def init_users():
    if not os.path.exists(USERS_FILE):
        users = {
            "admin": {"password": "admin123", "role": "admin"},
            "analyst": {"password": "analyst123", "role": "analyst"},
            "viewer": {"password": "viewer123", "role": "viewer"}
        }
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)

def load_users():
    init_users()
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def authenticate(username, password):
    users = load_users()
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    return None

# ---------------------------
# SESSION INIT
# ---------------------------
st.session_state.setdefault("logged_in", False)
st.session_state.setdefault("role", None)
st.session_state.setdefault("datasets", {})
st.session_state.setdefault("active_dataset", None)

# ---------------------------
# LOGIN
# ---------------------------
if not st.session_state.logged_in:
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        role = authenticate(username, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.role = role
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.info("admin/admin123 | analyst/analyst123 | viewer/viewer123")
    st.stop()

# ---------------------------
# HEADER
# ---------------------------
st.title("📊 Universal Analytics Dashboard")
st.caption(f"Logged in as: {st.session_state.role}")

# ---------------------------
# DATASET MANAGEMENT
# ---------------------------
st.sidebar.header("Datasets")

if st.session_state.role == "admin":
    uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.session_state.datasets[uploaded.name] = df
        st.session_state.active_dataset = uploaded.name
        st.sidebar.success(f"{uploaded.name} uploaded")

if not st.session_state.datasets:
    st.warning("No dataset uploaded.")
    st.stop()

dataset_list = list(st.session_state.datasets.keys())
selected = st.sidebar.selectbox("Select Dataset", dataset_list)
st.session_state.active_dataset = selected
df = st.session_state.datasets[selected]

# ---------------------------
# DATA INFO
# ---------------------------
st.subheader("Dataset Info")
c1, c2 = st.columns(2)
c1.metric("Rows", df.shape[0])
c2.metric("Columns", df.shape[1])

with st.expander("Preview"):
    st.dataframe(df.head(100), use_container_width=True)

# ---------------------------
# KPIs
# ---------------------------
st.subheader("KPIs")
kpis = generate_kpis(df)
for k, v in kpis.items():
    st.success(f"{k}: {v}")

# ---------------------------
# EXECUTIVE SUMMARY
# ---------------------------
st.subheader("Executive Summary")
st.info(executive_summary(df))

# ---------------------------
# VISUALIZATION
# ---------------------------
if st.session_state.role in ["admin", "analyst"]:
    st.subheader("Visualization")

    x_col = st.selectbox("X-axis", df.columns)
    y_col = st.selectbox("Y-axis", df.columns)

    chart_type = recommend_chart(df[x_col], df[y_col])

    if pd.api.types.is_numeric_dtype(df[y_col]):
        agg = st.selectbox("Aggregation", ["mean", "sum", "count"])
    else:
        agg = "count"

    if agg == "mean":
        plot_df = df.groupby(x_col)[y_col].mean().reset_index()
    elif agg == "sum":
        plot_df = df.groupby(x_col)[y_col].sum().reset_index()
    else:
        plot_df = df.groupby(x_col).size().reset_index(name=y_col)

    fig = px.bar(plot_df, x=x_col, y=y_col, template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Chart Explanation")
    st.info(explain_chart(plot_df, x_col, y_col))

else:
    st.info("Viewer mode: Visualization disabled")

# ---------------------------
# LOGOUT
# ---------------------------
if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()
