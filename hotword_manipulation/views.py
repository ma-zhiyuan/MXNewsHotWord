from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch,RequestsHttpConnection
from elasticsearch import helpers

es = Elasticsearch(hosts=[{'host':'search-mx-news-online-dev-vgoagyua54cwn35gjb5acqlroi.ap-northeast-2.es.amazonaws.com', 'port': 443}],
connection_class=RequestsHttpConnection,
use_ssl=True,
verify_certs=True)

def index(request):
    query_string = "{\"query\": {\"match_all\": {}}}"
    res = es.search(index="hotword", body=query_string)

    return render(request,'index.html',{'hotword':res})
