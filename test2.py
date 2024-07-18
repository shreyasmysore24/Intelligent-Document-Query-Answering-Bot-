import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import UnstructuredPDFLoader
import ollama
import os
import streamlit as st

def load_and_retrieve_docs(pdf_file):
  loader = UnstructuredPDFLoader(file_path=pdf_file)
  data = loader.load()
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
  chunks = text_splitter.split_documents(data)
  embeddings = OllamaEmbeddings(model="mistral")
  vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)

  return vectorstore


def format_docs(docs):
  return "\n\n".join(doc.page_content for doc in docs)


def pdf_chain(pdf_file, question):
  
  with open("temp_pdf.pdf", "wb") as f:
            f.write(pdf_file.getbuffer())
            
  docs = load_and_retrieve_docs(r"C:\Users\shrey\Desktop\urlmaker\temp_pdf.pdf")
  retriever = docs.as_retriever()
  retrieved_docs = retriever.invoke(question)
  formatted_context = format_docs(retrieved_docs)  # Pass retrieved documents for formatting
  
  formatted_prompt = f"Question: {question}\n\nContext: {formatted_context}"
  
  response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': formatted_prompt}])
  st.write( response['message']['content'])
  # value = st.text_input("please enter exit before attaching new file")
  # print(response['message']['content'])
  
  # if(value=="exit"):
  #     os.remove('C:\Users\shrey\Desktop\urlmaker\temp.pdf.pdf')


# Example usage
# pdf_path = r"C:\Users\shrey\Desktop\urlmaker\shreyas_sr_resume.pdf"  # Adjust the path as needed
# question = "What are all the skills"

# answer_pdf = pdf_chain(pdf_path, question)
# print(answer_pdf)
