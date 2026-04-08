import streamlit as st
import pandas as pd

from chatbot import get_response
from rag import create_vector_db
from ticket import create_ticket

# Sample data
data = [
    {"issue": "AC not cooling", "solution": "Clean filter"},
    {"issue": "Light not working", "solution": "Replace bulb"},
]
df = pd.DataFrame(data)

# Create DB
vector_db = create_vector_db(df)

# UI
st.title("🏢 AI Maintenance Bot")

query = st.text_input("Enter your issue:")

if st.button("Submit"):
    if query:
        response = get_response(query, vector_db)
        ticket = create_ticket(query)

        st.subheader("🤖 AI Response")
        st.write(response)

        st.subheader("🎫 Ticket")
        st.json(ticket)