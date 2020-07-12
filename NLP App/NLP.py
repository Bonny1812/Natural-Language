# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 10:44:18 2020

@author: bjoseph
"""
import streamlit as st 




# NLP Pkgs

from gensim.summarization import summarize

# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


# Function for Sumy Summarization
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result

def main():
    st.title("NLP with Streamlit")
    st.subheader("For testing purpose")
    
    if st.checkbox("Show Text Summarizer"):
        st.subheader("Summarize")
        
        message = st.text_area("Enter Text","Type Here ..")
        summary_options = st.selectbox("Choose Summarizer",['sumy','gensim'])
        if st.button("Summarize"):
            if summary_options == 'sumy':
                st.text("Using Sumy Summarizer ..")
                summary_result = sumy_summarizer(message)
            elif summary_options == 'gensim':
                st.text("Using Gensim Summarizer ..")
                summary_result = summarize(message)
            else:
                st.warning("Using Default Summarizer")
                st.text("Using Gensim Summarizer ..")
                summary_result = summarize(message)
                
            st.success(summary_result)


	# Summarization
    















if __name__ == '__main__':
	main()
