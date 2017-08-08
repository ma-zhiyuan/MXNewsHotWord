#-*- coding: UTF-8 -*-
import logging
import hashlib
import time
import json
from elasticsearch import Elasticsearch,RequestsHttpConnection

logger=logging.getLogger("django")

class HotWordModel:
    def __init__(self):
        self._es_host='search-mx-news-online-dev-vgoagyua54cwn35gjb5acqlroi.ap-northeast-2.es.amazonaws.com'
        self._es_port=443

    def setES_CLIENT(self):
       self._es_client = Elasticsearch(
          hosts=[{'host': self._es_host, 'port': self._es_port}],
          use_ssl=True,
          verify_certs=True,
          connection_class=RequestsHttpConnection
        )

    def query_item(self):
        self.setES_CLIENT()
        query_top = '{"query":{"match":{"valid":0}},"sort":[{"position":{"order":"asc"}},{"query_type":{"order":"desc"}},{"date_str":{"order":"desc"}}]}'
        query_black = "{\"query\": {\"match\": {\"valid\": 1}}}"
        top = self._es_client.search(index="hotword", body=query_top)
        black = self._es_client.search(index="hotword", body=query_black)
        tophit = top.get("hits").get("hits")
        blackhit = black.get("hits").get("hits")
        topResultList = []
        blackResultList = []
        for res in tophit:
            topResultList.append(res.get("_source"))
        for res in blackhit:
            blackResultList.append(res.get("_source"))
        return topResultList,blackResultList

    def pullblack(self,queryword):
        self.setES_CLIENT()
        word = Word('','','','','','')
        queryjson = '{"query":{"match":{"query":"'+queryword+'"}}}'
        res = self._es_client.search(index="hotword", body=queryjson)
        wordjson = res.get("hits").get("hits")[0].get("_source")
        s = json.dumps(wordjson)
        ss = s.replace("'","\"")
        word.__dict__ = json.loads(ss)
        print word
        word.valid = 1
        m = hashlib.md5()
        m.update(queryword)
        md5word = m.hexdigest()
        word.date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        word.date_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        pullstring =json.dumps(word.__dict__)
        self._es_client.index(index="hotword", doc_type="hotword", id=md5word, body=pullstring)


class Word:
    def __init__(self,query,query_type,position,date,date_str,valid):
        self.query = query
        self.query_type = query_type
        self.position = position
        self.date = date
        self.date_str = date_str
        self.valid = valid
    def __str__(self):
        return '\n'.join(['%s:%s' % item for item in self.__dict__.items()])
