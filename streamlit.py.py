#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import wikipedia


# In[6]:


def get_top_books():
    try:
        top_books = wikipedia.page("List of best-selling books")
        return top_books
    except wikipedia.exceptions.DisambiguationError as e:
        # In case of disambiguation error, we can try to fetch a specific page
        page_title = e.options[0]
        page = wikipedia.page(page_title)
        return page

def main():
    st.title("Top 100 English Books Chatbot")
    st.write("Welcome to the Top 100 English Books Chatbot! Type your questions related to books below:")

    top_books = get_top_books()

    user_input = st.text_input("Ask your question here:")

    if user_input:
        try:
            answer = wikipedia.summary(user_input)
            st.write(answer)
        except wikipedia.exceptions.PageError:
            st.write("Sorry, I couldn't find any relevant information.")
        except wikipedia.exceptions.DisambiguationError as e:
            st.write(f"Sorry, I found multiple possible articles. Please be more specific: {', '.join(e.options)}")

if __name__ == "__main__":
    main()


# In[ ]:




