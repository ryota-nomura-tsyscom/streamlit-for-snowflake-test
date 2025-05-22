import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.title("Hierarchical Data Charts")

df = pd.read_csv("data/employees.csv", header=0).convert_dtypes()
# st.dataframe(df)

labels = df[df.columns[0]]
parents = df[df.columns[1]]

tabs = st.tabs(["Treemap", "Icicle", "Sunburst", "Sankey"])

with tabs[0]:
    data = go.Treemap(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgray"
    )
    fig = go.Figure(data)
    st.plotly_chart(fig, use_container_width=True)

with tabs[1]:
    data = go.Icicle(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgray"
    )
    fig = go.Figure(data)
    st.plotly_chart(fig, use_container_width=True)

with tabs[2]:
    data = go.Sunburst(
        ids=labels,
        labels=labels,
        parents=parents,
        insidetextorientation='horizontal'
    )
    fig = go.Figure(data)
    st.plotly_chart(fig, use_container_width=True)

with tabs[3]:
    data = go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=[i for i, parent in enumerate(parents) if parent in labels.values],
            target=[list(labels).index(parent) if parent in labels.values else 0 for parent in parents if parent in labels.values],
            value=[1 for _ in range(len(labels)) if parents.iloc[_] in labels.values]
        )
    )
    fig = go.Figure(data)
    st.plotly_chart(fig, use_container_width=True)