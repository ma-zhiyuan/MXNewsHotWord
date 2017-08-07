from django.shortcuts import render
from hotword_manipulation.models.model import HotWordModel

#es = Elasticsearch(hosts=[{'host':'search-mx-news-online-dev-vgoagyua54cwn35gjb5acqlroi.ap-northeast-2.es.amazonaws.com', 'port': 443}],connection_class=RequestsHttpConnection,use_ssl=True,verify_certs=True)

def index(request):
    hotword = HotWordModel()
    resultstring = hotword.query_item()
    return render(request,'index.html',{'hotword':resultstring})
