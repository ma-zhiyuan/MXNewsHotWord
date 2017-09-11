#-*- coding: UTF-8 -*-
import json
import time
from django.shortcuts import render, redirect
from hotword_manipulation.models.model import HotWordModel

#默认入口
def index(request):
    hotWord = HotWordModel()
    topResultList,blackResultList = hotWord.query_item()
    return render(request,'index.html',{'topResultList':topResultList,'blackResultList':blackResultList})

#拉黑接口
def pullblack(request,queryword):
    hotWord = HotWordModel()
    hotWord.pullblack(queryword)
    time.sleep(1)
    topResultList,blackResultList = hotWord.query_item()
    return render(request,'index.html',{'topResultList':topResultList,'blackResultList':blackResultList})

#恢复
def recovery(request,queryword):
    hotWord = HotWordModel()
    hotWord.recovery(queryword)
    time.sleep(1)
    topResultList, blackResultList = hotWord.query_item()
    return render(request, 'index.html', {'topResultList': topResultList, 'blackResultList': blackResultList})

#插入热词
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
