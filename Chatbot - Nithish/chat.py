import streamlit as st
from chatbot import chat
c=0
def main():
    global c
    st.title("Apashyam Chatbot")
    st.write("Welcome to Chatbot. Please type a message and press Enter to start the conversation.")
    c+=1
    input=st.text_input("You:",key=f"input{c}")

    if input:
        response=chat(input)
        st.text_area("Chatbot:",value=response,height=100,max_chars=None,key=f"chatbot_response_{c}")

        if response.lower() in ['goodbye','bye','assom']:
            st.write("Thank you for chatting with me. Have a great day!")
            st.stop()
if __name__=='__main__':
    main()
