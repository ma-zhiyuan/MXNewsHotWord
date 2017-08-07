#-*- coding: UTF-8 -*-
import json
from django.shortcuts import render
from hotword_manipulation.models.model import HotWordModel


def index(request):
    hotWord = HotWordModel()
    top,black = hotWord.query_item()
    #resultstring = [{u'sort': [1], u'_type': u'hotword', u'_source': {u'query_type': u'alphago', u'valid': 0, u'position': 1, u'date': u'2017-08-03', u'query': u'query1', u'date_str': u'2017-08-03 11:55:01'}, u'_score': None, u'_index': u'hotword', u'_id': u'8b09fc98eb98edcff9700ee747064cd6'}, {u'sort': [2], u'_type': u'hotword', u'_source': {u'query_type': u'alphago', u'valid': 0, u'position': 2, u'date': u'2017-08-03', u'query': u'query2', u'date_str': u'2017-08-03 11:55:02'}, u'_score': None, u'_index': u'hotword', u'_id': u'796e92b9df3e0fc7b9ee0c37a462cec8'}, {u'sort': [3], u'_type': u'hotword', u'_source': {u'query_type': u'alphago', u'valid': 0, u'position': 3, u'date': u'2017-08-03', u'query': u'query3', u'date_str': u'2017-08-03 11:55:03'}, u'_score': None, u'_index': u'hotword', u'_id': u'191b7c69711a5d9462f93383ff5b656b'}, {u'sort': [4], u'_type': u'hotword', u'_source': {u'query_type': u'alphago', u'valid': 0, u'position': 4, u'date': u'2017-08-03', u'query': u'query4', u'date_str': u'2017-08-03 11:55:04'}, u'_score': None, u'_index': u'hotword', u'_id': u'a831310709b13937ec75cd787e5e82d8'}, {u'sort': [5], u'_type': u'hotword', u'_source': {u'query_type': u'alphago', u'valid': 0, u'position': 5, u'date': u'2017-08-03', u'query': u'query5', u'date_str': u'2017-08-03 11:55:05'}, u'_score': None, u'_index': u'hotword', u'_id': u'659d4e20bb23055f184db3278889fd27'}, {u'sort': [6], u'_type': u'hotword', u'_source': {u'query_type': u'alphago', u'valid': 0, u'position': 6, u'date': u'2017-08-03', u'query': u'query6', u'date_str': u'2017-08-03 11:55:06'}, u'_score': None, u'_index': u'hotword', u'_id': u'bb57b30062cade85810753be946a3278'}, {u'sort': [7], u'_type': u'hotword', u'_source': {u'query_type': u'alphago', u'valid': 0, u'position': 7, u'date': u'2017-08-03', u'query': u'query7', u'date_str': u'2017-08-03 11:55:07'}, u'_score': None, u'_index': u'hotword', u'_id': u'a6f472ffd42646bd29a925887999653d'}, {u'sort': [8], u'_type': u'hotword', u'_source': {u'query_type': u'alphago', u'valid': 0, u'position': 8, u'date': u'2017-08-03', u'query': u'query8', u'date_str': u'2017-08-03 11:55:08'}, u'_score': None, u'_index': u'hotword', u'_id': u'fce1d6e36711923651481c5dd4ee7733'}, {u'sort': [9], u'_type': u'hotword', u'_source': {u'query_type': u'alphago', u'valid': 0, u'position': 9, u'date': u'2017-08-03', u'query': u'query9', u'date_str': u'2017-08-03 11:55:09'}, u'_score': None, u'_index': u'hotword', u'_id': u'171556e1418debb465bf39b10c6416ad'}, {u'sort': [10], u'_type': u'hotword', u'_source': {u'query_type': u'alphago', u'valid': 0, u'position': 10, u'date': u'2017-08-03', u'query': u'query10', u'date_str': u'2017-08-03 11:55:10'}, u'_score': None, u'_index': u'hotword', u'_id': u'c8d26567789f8484ff1d3a546abdc9e2'}]
    topResultList = []
    blackResultList = []
    for res in top:
        topResultList.append(res.get("_source"))
    for res in black:
        blackResultList.appens(res.get("_source"))
    return render(request,'index.html',{'topResultList':topResultList,'blackResultList':blackResultList})


if __name__ == '__main__':
    index("")