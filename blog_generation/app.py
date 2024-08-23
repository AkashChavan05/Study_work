import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get responce from LLAMA2
def getllamaresponce(input_text,no_words,blog_style):
    #llama model load

    llm=CTransformers(model="",
                      model_type="llama",
                      config={"max_token":256,
                              "temparature":0.01}
                      )
    
        ## Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response



st.set_page_config(page_title="Blogs Generation",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Blogs Generation")

input_text = st.text_input("Enter the blog Topic")

##creating the 2 columns for additional 2 fields

col1,col2 = st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    
submit= st.buttom("Generate Blog")

if submit:
    st.write(getllamaresponce(input_text,no_words,blog_style))