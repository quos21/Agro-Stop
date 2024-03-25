from openai import OpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
import os
key = os.environ.get('key')

st.title("Agro-Bot 👨‍🌾")
st.write("Ask your query in the chat below")

client = OpenAI(api_key=key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



try:
    if prompt := st.chat_input("What is up?"):


        template='''You are to act as an agricultural expert and solve this query given by the user. 
                I will describe my situation and you will give me a two part solution, where one part includes the straightforward solution an the second part includes the steo by step solution. 
                You should only reply with your answer and nothing else. Also keep in mind the solution should be in great detail and in the same language the query is in. Do not write explanations.I am telling the query now.




                ''' + prompt
        st.session_state.messages.append({"role": "user", "content": template})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m['content']}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

except NameError:
    st.error('Try re-opening the link again')

st.markdown(
        """
        <style>
            .st-emotion-cache-6qob1r.eczjsme3{
                background-color: grey;
                background-image: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1));;
            }
        </style>
        """,
        unsafe_allow_html=True
)