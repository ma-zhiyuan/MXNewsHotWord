#-*- coding: UTF-8 -*-
import json
import time
from django.shortcuts import render, redirect
from hotword_manipulation.models.model import HotWordModel


def index(request):
    hotWord = HotWordModel()
    topResultList,blackResultList = hotWord.query_item()
    #topResultList = [{u'query_type': u'alphago', u'valid': 0, u'position': 1, u'date': u'2017-08-03', u'query': u'query1', u'date_str': u'2017-08-03 11:55:01'}, {u'query_type': u'alphago', u'valid': 0, u'position': 2, u'date': u'2017-08-03', u'query': u'query2', u'date_str': u'2017-08-03 11:55:02'}, {u'query_type': u'alphago', u'valid': 0, u'position': 3, u'date': u'2017-08-03', u'query': u'query3', u'date_str': u'2017-08-03 11:55:03'}, {u'query_type': u'alphago', u'valid': 0, u'position': 4, u'date': u'2017-08-03', u'query': u'query4', u'date_str': u'2017-08-03 11:55:04'}, {u'query_type': u'alphago', u'valid': 0, u'position': 5, u'date': u'2017-08-03', u'query': u'query5', u'date_str': u'2017-08-03 11:55:05'}, {u'query_type': u'alphago', u'valid': 0, u'position': 6, u'date': u'2017-08-03', u'query': u'query6', u'date_str': u'2017-08-03 11:55:06'}, {u'query_type': u'alphago', u'valid': 0, u'position': 7, u'date': u'2017-08-03', u'query': u'query7', u'date_str': u'2017-08-03 11:55:07'}, {u'query_type': u'alphago', u'valid': 0, u'position': 8, u'date': u'2017-08-03', u'query': u'query8', u'date_str': u'2017-08-03 11:55:08'}, {u'query_type': u'alphago', u'valid': 0, u'position': 9, u'date': u'2017-08-03', u'query': u'query9', u'date_str': u'2017-08-03 11:55:09'}]
    #blackResultList = [{u'query_type': u'alphago', u'valid': 1, u'position': 10, u'date': u'2017-08-03', u'query': u'query10', u'date_str': u'2017-08-03 11:55:10'}]
    return render(request,'index.html',{'topResultList':topResultList,'blackResultList':blackResultList})

def pullblack(request,queryword):
    hotWord = HotWordModel()
    hotWord.pullblack(queryword)
    time.sleep(1)
    topResultList,blackResultList = hotWord.query_item()
    return render(request,'index.html',{'topResultList':topResultList,'blackResultList':blackResultList})

def recovery(request,queryword):
    hotWord = HotWordModel()
    hotWord.recovery(queryword)
    time.sleep(1)
    topResultList, blackResultList = hotWord.query_item()
    return render(request, 'index.html', {'topResultList': topResultList, 'blackResultList': blackResultList})

def insertword(request):
    hotWord = HotWordModel()
    if request.POST:
        word = request.POST['word']
        ind = request.POST['index']
        if word.strip()!='' and ind.strip()!='':
            hotWord.insertword(word,ind)
    time.sleep(1)
    topResultList, blackResultList = hotWord.query_item()
    return render(request, 'index.html', {'topResultList': topResultList, 'blackResultList': blackResultList})

if __name__ == '__main__':
    index("")