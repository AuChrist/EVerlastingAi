import urllib.request
import wikipedia

def check_internet_connection():

    try:
        urllib.request.urlopen('https://google.com')
        return True
    except:
        return False


def check_on_wikipedia(query):
    query = query.lower()
    query = query.replace("Who is", "")
    query = query.replace("What is", "")
    query = query.replace("Do you know", "")
    query = query.replace("Tell me about", "")

    query = query.strip()   

    try:
        data = wikipedia.summary(query, sentences=3)
        return data
    except Exception as e:
        return ""

