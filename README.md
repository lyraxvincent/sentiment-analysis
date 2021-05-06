# **Sentiment Analysis**

**Sentiment analysis** (also known as opinion mining or emotion AI) refers to the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information. Sentiment analysis is widely applied to voice of the customer materials such as reviews and survey responses, online and social media, and healthcare materials for applications that range from marketing to customer service to clinical medicine.

## **Data Labeling**
Used here is **TextBlob**, a Python library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.  
It's documentation [here.](https://textblob.readthedocs.io/en/dev/index.html)

## **Data Collection**

The Twitter API **tweepy** was used to collect tweets related to COVID-19.  
You may view the script collect_tweets.py

## **Deployment**
A web-app handling sentiment analysis where a user inputs their text and the system outputs the sentiment associated with it was deployed using the Flask api and is live [here.](https://sentlysis.herokuapp.com/)

## **Resources**

- [Introduction to using Textblob for Sentiment Analysis](https://towardsdatascience.com/having-fun-with-textblob-7e9eed783d3f)
- [Build and deploy your first Machine Learning web app](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99)
- [Hosting a python web app on heroku](https://dev.to/towernter/hosting-a-python-django-web-application-on-heroku-2i48)
- [Retrieving html form data using Flask](https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/)
