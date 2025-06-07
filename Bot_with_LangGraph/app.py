import streamlit as st
from transformers import pipeline
from bot import ChatBot


mybot= ChatBot()
graph= mybot()

st.title("Simple ChatBot with LangGraph")
st.write("Ask any question and Chatbot will try to give right answer")

question= st.text_input("Enter youre question here: ")
input= {'messages': [question]}

if st.button('Get Answer'):
    if input:
        response= graph.invoke(input)
        st.write("Answer:", response['messages'][-1].content)
    else:
        st.warning("Please write the question to get a right answer.")
        
st.markdown("---")
st.caption("Powered by Streamlit and Transformers")