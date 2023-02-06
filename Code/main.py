# import the necessary packages
# tkinter is used to create a visual interface
import tkinter as tk

# If nltk is not installed on the system, to install: pip install nltk
# nltk is used for sensitivity analysis
import nltk

# If TextBlob is not installed on the system, to install it: pip install textblob
# we need API provider to perform NLP tasks and hence TextBlob is used to process text data
from textblob import TextBlob

# iI newspaper is not installed on the system, to install it: pip3 install newspaper3k
# this library will be used for article collection and development
from newspaper import article, Article

def summarize():
    # To specify the start and end point for the url
    # assigning the obtained 'url' address from the user to a variable
    url = utext.get('1.0', "end").strip()

    # creating the article variable
    article = Article(url)

    # data is downloaded
    article.download()

    # separation of data to facilitate understanding
    article.parse()

    # to make use of the NLP methods
    article.nlp()

    # config is required to prevent user from making changes and this has to be done for all the columns
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    # In case of changing the content, everything has to be deleted there first
    title.delete('1.0', "end")
    title.insert('1.0', article.title)

    author.delete('1.0', "end")
    author.insert('1.0', article.authors)

    publication.delete('1.0', "end")
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)

    # sensitivity is analysed
    # here the entire article is sentimentally analysed and not just the summary
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', "end")
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}.Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


# tkinter
root = tk.Tk()

# the name of the application
root.title("SUMMaRIZER")

# the size of the window is specified
root.geometry('1200x600')

# Properties of the headers are defined that are tagged between root.mainloop () and root.
tlabel = tk.Label(root, text="Title")
tlabel.pack()

# Disable all text boxes so that user cannot manipulate them except the url which takes the input from the user
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
# pack it with pack() and complete it.
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Published Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# for the url to be entered by the user
ulabel = tk.Label(root, text="Enter URL")
ulabel.pack()

# In order not to write an url for the 2nd time, name it differently for instance, 'utext'
utext = tk.Text(root, height=1, width=140)
utext.pack()

# add a button for the summary
# this button calls a function that performs the actual news summarization
btn = tk.Button(root,text ="Summarize", command=summarize)
btn.pack()

# main loop is created
root.mainloop()
