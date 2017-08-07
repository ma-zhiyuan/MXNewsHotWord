#-*- coding: UTF-8 -*-
import json
from django.shortcuts import render
from hotword_manipulation.models.model import HotWordModel


def index(request):
    hotWord = HotWordModel()
    topResultList,blackResultList = hotWord.query_item()
    #topResultList = [{"_index":"hotword","_type":"hotword","_id":"8b09fc98eb98edcff9700ee747064cd6","_score":"null","_source":{"query":"query1","query_type":"alphago","position":1,"date":"2017-08-03","date_str":"2017-08-03 11:55:01","valid":0},"sort":[1]},{"_index":"hotword","_type":"hotword","_id":"796e92b9df3e0fc7b9ee0c37a462cec8","_score":"null","_source":{"query":"query2","query_type":"alphago","position":2,"date":"2017-08-03","date_str":"2017-08-03 11:55:02","valid":0},"sort":[2]},{"_index":"hotword","_type":"hotword","_id":"191b7c69711a5d9462f93383ff5b656b","_score":"null","_source":{"query":"query3","query_type":"alphago","position":3,"date":"2017-08-03","date_str":"2017-08-03 11:55:03","valid":0},"sort":[3]},{"_index":"hotword","_type":"hotword","_id":"a831310709b13937ec75cd787e5e82d8","_score":"null","_source":{"query":"query4","query_type":"alphago","position":4,"date":"2017-08-03","date_str":"2017-08-03 11:55:04","valid":0},"sort":[4]},{"_index":"hotword","_type":"hotword","_id":"659d4e20bb23055f184db3278889fd27","_score":"null","_source":{"query":"query5","query_type":"alphago","position":5,"date":"2017-08-03","date_str":"2017-08-03 11:55:05","valid":0},"sort":[5]},{"_index":"hotword","_type":"hotword","_id":"bb57b30062cade85810753be946a3278","_score":"null","_source":{"query":"query6","query_type":"alphago","position":6,"date":"2017-08-03","date_str":"2017-08-03 11:55:06","valid":0},"sort":[6]},{"_index":"hotword","_type":"hotword","_id":"a6f472ffd42646bd29a925887999653d","_score":"null","_source":{"query":"query7","query_type":"alphago","position":7,"date":"2017-08-03","date_str":"2017-08-03 11:55:07","valid":0},"sort":[7]},{"_index":"hotword","_type":"hotword","_id":"fce1d6e36711923651481c5dd4ee7733","_score":"null","_source":{"query":"query8","query_type":"alphago","position":8,"date":"2017-08-03","date_str":"2017-08-03 11:55:08","valid":0},"sort":[8]},{"_index":"hotword","_type":"hotword","_id":"171556e1418debb465bf39b10c6416ad","_score":"null","_source":{"query":"query9","query_type":"alphago","position":9,"date":"2017-08-03","date_str":"2017-08-03 11:55:09","valid":0},"sort":[9]}]
    #blackResultList = [{"_index":"hotword","_type":"hotword","_id":"c8d26567789f8484ff1d3a546abdc9e2","_score":1,"_source":{"query":"query10","query_type":"alphago","position":10,"date":"2017-08-03","date_str":"2017-08-03 11:55:10","valid":1}}]
    return render(request,'index.html',{'topResultList':topResultList,'blackResultList':blackResultList})

def pullblack(request):
    hotWord = HotWordModel()
    hotWord.pullblack()
    topResultList,blackResultList = hotWord.query_item()
    return render(request,'index.html',{'topResultList':topResultList,'blackResultList':blackResultList})

if __name__ == '__main__':
    index("")