import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summerize():
    url=urltext.get('1.0','end').strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publicatin_date.config(state='normal')
    summary.config(state='normal')
    sentiments.config(state='normal')
    
    title.delete('1.0','end')
    title.insert('1.0',article.title)

    author.delete('1.0','end')
    author.insert('1.0',article.authors)

    publicatin_date.delete('1.0','end')
    publicatin_date.insert('1.0',article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)

    analysis = TextBlob(article.text)
    sentiments.delete('1.0','end')
    sentiments.insert('1.0'f'polarity : {analysis.polarity},Sentiments :{"Positive" if analysis.polarity >0 else "Negative" if analysis.polarity<0 else "Netural"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publicatin_date.config(state='disabled')
    summary.config(state='disabled')
    sentiments.config(state='disabled')



    

# Bulding GUI
root = tk.Tk()
root.title = ("Article Summarizer")
root.geometry = ('1200x600')
# Title
tlabel = tk.Label(root, text='Title')
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disable', bg='#D3D3D3')
title.pack()
# author
alabel = tk.Label(root, text='Author')
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disable', bg='#D3D3D3')
author.pack()
# Publication date
plabel = tk.Label(root, text='Publication Date')
plabel.pack()
publicatin_date = tk.Text(root, height=1, width=140)
publicatin_date.config(state='disable', bg='#D3D3D3')
publicatin_date.pack()
# summary
slabel = tk.Label(root, text='Summary')
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disable', bg='#D3D3D3')
summary.pack()
# Sentiments
selabel = tk.Label(root, text='Sentiments Analysis')
selabel.pack()
sentiments = tk.Text(root, height=1, width=140)
sentiments.config(state='disable', bg='#D3D3D3')
sentiments.pack()
# url
ulabel = tk.Label(root, text='URL')
ulabel.pack()
urltext = tk.Text(root, height=1, width=140)
urltext.pack()
# Button
btn = tk.Button(root, text='Submit',command=summerize)
btn.pack()
root.mainloop()
