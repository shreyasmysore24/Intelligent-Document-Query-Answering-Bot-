import streamlit as st
from ur import rag_chain  # Import your RAG Chain function from ur.py
from test2 import pdf_chain
import os

# Title and description
st.title("Question Answering Bot 🤖")
# st.markdown("Enter a URL and a query to get answers from the RAG chain.")

# URL Question Answering Section
st.sidebar.subheader("Web Question Answering")
st.sidebar.markdown("Enter a URL and a query to get answers.")

url_key = "url_input"
query_key = "url_query"

url = st.sidebar.text_input("Enter URL", key=url_key)
query = st.sidebar.text_input("Enter Query", key=query_key)

if st.sidebar.button("Get Answer"):
    if url and query:
         answer = rag_chain(url, query)  # Call your RAG Chain function here
         st.write("Answer:")
         st.write(answer)
    else:
        st.sidebar.warning("Please enter both URL and query.")

# PDF Attachment Question Answering Section
st.sidebar.subheader("PDF Attachment Question Answering")
st.sidebar.markdown("Upload a PDF file and enter a query to get answers.")

pdf_key = "pdf_upload"
query_pdf_key = "pdf_query"

uploaded_file = st.sidebar.file_uploader("Upload PDF file", type=["pdf"], key=pdf_key)

query_pdf = st.sidebar.text_input("Enter Query")

if st.sidebar.button("Get Answer PDF"):
    if uploaded_file is not None and query_pdf:
        
    
            # answer_pdf = 
            pdf_chain(uploaded_file, query_pdf)
            # st.write("Answer:")
            # st.write(answer_pdf)
      
        
        
    else:
        st.sidebar.warning("Please upload a PDF file and enter a query.")

