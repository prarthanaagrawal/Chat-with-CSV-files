# import streamlit as st
# from langchain_experimental.agents import create_csv_agent
# from langchain.llms import OpenAI
# from dotenv import load_dotenv
# def main():

#     load_dotenv()

#     st.set_page_config(page_title="Ask your CSV")
#     st.header("Ask your CSV🤩")

#     user_csv = st.file_uploader("Upload your CSV file",type = "csv")

#     if user_csv is not None:
#         user_question = st.text_input("Ask a question about your CSV")

#         llm = OpenAI(temperature = 0)
#         agent = create_csv_agent(llm,user_csv,verbose=True)

#         if user_question is not None and user_question != "":
#             response = agent.run(user_question)
#             st.write(response)
    

# if __name__ == "__main__":
#     main()

import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV🤩")

    user_csv = st.file_uploader("Upload your CSV file", type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask a question about your CSV")

        openai_api_key = os.getenv("OPENAI_API_KEY")  # Get the OpenAI API key from environment variables

        if openai_api_key:
            llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
            agent = create_csv_agent(llm, user_csv, verbose=True)

            if user_question is not None and user_question != "":
                response = agent.run(user_question)
                st.write(response)
        else:
            st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    
if __name__ == "__main__":
    main()
