#!/usr/bin/env python
# coding: utf-8

# # PDF to Text converter
# 

# Use Anaconda prompt to install these libraries
# pip install PyPDF2
# pip install textract
# pip install nltk

# In[74]:


import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')


# In[75]:


pdfFileObj = open(r'C:\Users\bjoseph\Documents\Sourav Resume\BI\bonny_joseph.pdf','rb')
#The pdfReader variable is a readable object that will be parsed.
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


# If you know that there is only 1 page, then use the follwoing simple code
# 
# pageObject = pdfReader.getPage(0)
# 
# print(pageObject.extractText())

# In[76]:


#Use the below code if you dont know the number of pages. This will allow us to parse through all the pages.
num_pages = pdfReader.numPages
count = 0
text = ""
#The while loop will read each page.
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()


# In[77]:


print(text)


# In[78]:


#The word_tokenize() function will break our text phrases into individual words.
tokens = word_tokenize(text)
#We'll create a new list that contains punctuation we wish to clean.
punctuations = ['(',')',';',':','[',']',',','|','-']
#We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much value as keywords.
stop_words = stopwords.words('english')
#We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]


# In[79]:


keywords = ' '.join(keywords)
keywords


# In[80]:


# Install the docx2txt package
get_ipython().system('pip install docx2txt')
# Import the library
import docx2txt

# Store the job description into a variable
job_description = docx2txt.process("Desktop\Description Job.docx")

# Print the job description
print(job_description)


# In[81]:


job_desc_tokens = word_tokenize(job_description)
punctuations = ['(',')',';',':','[',']',',','/','-']
stop_words = stopwords.words('english')
job_desc_keywords = [word for word in job_desc_tokens if not word in stop_words and not word in punctuations]


# Word to vector from Scratch

# In[82]:



from collections import Counter
# count word occurrences
a_vals = Counter(keywords)
b_vals = Counter(job_desc_keywords)

# convert to word-vectors
words  = list(a_vals.keys() | b_vals.keys())
a_vect = [a_vals.get(word, 0) for word in words]        # [0, 0, 1, 1, 2, 1]
b_vect = [b_vals.get(word, 0) for word in words]        # [1, 1, 1, 0, 1, 0]

# find cosine
len_a  = sum(av*av for av in a_vect) ** 0.5             # sqrt(7)
len_b  = sum(bv*bv for bv in b_vect) ** 0.5             # sqrt(4)
dot    = sum(av*bv for av,bv in zip(a_vect, b_vect))    # 3
cosine = dot / (len_a * len_b) 


# In[83]:


print(cosine)


# We can use Cosine similarity/Jaccard similarity between the list. 
# We can even use it from dfferent libraries including td-if,nltk, spacy, gensim

# Reference:
# https://medium.com/better-programming/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f
# https://medium.com/@randerson112358/resume-scanner-2c30f5baf92c

# In[ ]:




