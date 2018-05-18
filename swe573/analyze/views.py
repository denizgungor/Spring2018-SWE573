from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
import json
import tweepy
from tweepy import cursor
from tweepy import API
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
from textblob import TextBlob
import operator
from analyze.graphstuff.Graph import Graph
from swe573 import settings
from django.http import HttpResponse

consumer_key = 'bT3x6y2rZCI6h6PQlaAOeQlAu'
consumer_secret = 'MpcpsCdVfixFSbbQnnHvr5fxgZmx2Dx2fQCwzppfPDOMvbphZh'
access_token = '995715271208919040-kJlqUCQuV14dSpflm6BqRxFOlwBT987'
access_token_secret = 'o6CQaDFtiVRgCuTWNCwc4qLfSOvkAJfXM4RCL0g7KzeWV'
var1 = "data123"

# global actions
nltk.download('vader_lexicon')


# Create your views here.
@login_required
def home(request):
    return render(request, 'analyze/home.html')


@login_required
def test(request, string):
    resultDataSet = list()
    sentimentDataSet = []
    sentimentValueDataSet = []
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    searchquery = string + '-filter:retweets'
    requestData = api.search(q=searchquery, count=15, lang='en')
    jsonObject = json.dumps([status._json for status in requestData])
    results = json.loads(jsonObject)
    import preprocessor
    for tweet in results:
        preprocessor.set_options(preprocessor.OPT.URL, preprocessor.OPT.MENTION, preprocessor.OPT.RESERVED)
        tweetData = preprocessor.clean(tweet['text'])
        # print(tweetData)
        # sid = SentimentIntensityAnalyzer()
        # ss = sid.polarity_scores(tweetData)
        # text = str([text.encode('utf-8') for text in tweet])
        # sid = SentimentIntensityAnalyzer()
        # ss = sid.polarity_scores("a")
        # testimonial = TextBlob(text)
        resultDataSet.append(tweet)

    for i in resultDataSet:
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(i['text'])
        # result_sentiment = max(ss.items(), key=operator.itemgetter(1))[0]
        result_sentiment = ss.items()
        sentimentDataSet.append(result_sentiment)

    generate_sentiment_graph(sentimentDataSet)
    print(settings.BASE_DIR + settings.STATIC_URL + 'deniz_graph.png')

    args = {'data': resultDataSet, 'sentiments': sentimentDataSet, 'string': string, 'scoreList': ss.items(),
            'sentiment_graph': reverse(show_sentiment_graph)}

    return render(request, 'analyze/test.html', args)


def generate_sentiment_graph(data_set):
    result = Graph(data_set).draw_graph()
    print("--------------------------------Denizdenizdeniz------------------------")
    print(result)
    return result


def show_sentiment_graph(request):
    my_graph = open(settings.BASE_DIR + settings.STATIC_URL + 'deniz_graph.png', "rb").read()
    print(settings.BASE_DIR + settings.STATIC_URL + 'deniz_graph.png')
    return HttpResponse(my_graph, content_type="image/png")


def logout(request):
    return render(request, 'analyze/logout.html', {})


def login(request):
    return render(request, 'analyze/login.html', {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'analyze/register.html', {'form': form})

#			resultDataSet.append(k+"-_-"+ss[k]+"-_-"+tweet)
