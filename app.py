#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Necessary imports
import streamlit as st
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = "e6a46eff9fb24283b09a6bc0ae1b5c3f"
endpoint = "https://cognitive-language-halfblood.cognitiveservices.azure.com/"

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

st.title("PII Redaction Application")

#Textbox for text user is entering
st.subheader("Enter the text you'd like to analyze to redact PII:")
text = st.text_input('Enter text') #text is stored in this variable

st.header("Results")

def pii_recognition_example(client):
    documents = [
        text
    ]
    response = client.recognize_pii_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]
    for doc in result:
        st.write("Redacted Text: {}".format(doc.redacted_text))
        for entity in doc.entities:
            st.write("Entity: {}".format(entity.text))
            st.write("\tCategory: {}".format(entity.category))
            st.write("\tConfidence Score: {}".format(entity.confidence_score))
            st.write("\tOffset: {}".format(entity.offset))
            st.write("\tLength: {}".format(entity.length))
pii_recognition_example(client)




