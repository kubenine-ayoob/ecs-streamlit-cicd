import streamlit as st
import datetime
import os

st.set_page_config(page_title="ECS Streamlit CI/CD ")

st.title("AWS ECS Streamlit CI/CD ")

st.success("Version 1.0.1")

st.write("Application deployed using ECS Fargate")

st.write(f"Current Time: {datetime.datetime.now()}")

st.write(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")

st.info("This application is deployed through GitHub Actions")