import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spvoice")
    speak.Speak(str)


if __name__ == '__main__':
     speak("News for today")
     # inn = int(input("PRESS 1 to exit"))

     url="https://newsapi.org/v2/top-headlines?country=in&apiKey=755bc6f495f5460ab565852ca8f379b1"
     news=requests.get(url).text
     news_dict=json.loads(news)
     # print(news_dict["articles"])
     arts=news_dict['articles']
     for article in arts:
         speak(article['title'])

     speak("thanks for listening")

