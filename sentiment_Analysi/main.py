from textblob import TextBlob
with open('mytext.txt','r') as f:
    text = f.read()
blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)

with open('mytext2.txt','r') as f:
    text2 = f.read()
blob2 = TextBlob(text2)
sentiment2 = blob2.sentiment.polarity # -1 to 1
print(sentiment2)

with open('mytext3.txt','r') as f:
    text2 = f.read()
blob3 = TextBlob(text2)
sentiment3 = blob3.sentiment.polarity # -1 to 1
print(sentiment3)