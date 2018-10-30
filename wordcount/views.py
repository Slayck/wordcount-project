from django.http import HttpResponse
from django.shortcuts import render
import operator

def hello(request):
    return HttpResponse("<h1>Hello World!</h1>") #Code is inside of it

def about(request):
    return render(request, "about.html",{})

def home(request):
    return render(request,"home.html",{"welcome":"Welcome to your Dragon World"}) #Code is rendering you into a full html page

def count(request):
    sentText = request.GET['fullText']
    words = sentText.split()
    lenText = len(words)
    wordDict = {}
    for word in words:
        if word.lower() in wordDict:
            wordDict[word.lower()] += 1
        else:
            wordDict[word.lower()] = 1
    wordList = wordDict.items()
    sortedList = sorted(wordList,key=operator.itemgetter(1),reverse=True)
    return render(request,"count.html",{"SentText":sentText,"LenText":lenText,"wordList":sortedList})
