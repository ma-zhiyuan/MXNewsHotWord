#-*- coding: UTF-8 -*-
import logging
from elasticsearch import Elasticsearch,RequestsHttpConnection

logger=logging.getLogger("django")

class HotWordModel(object):
    def __init__(self):
        self._es_host='search-mx-news-online-dev-vgoagyua54cwn35gjb5acqlroi.ap-northeast-2.es.amazonaws.com'
        self._es_port=443

    #def setES_CLIENT(self):
    #   self._es_client = Elasticsearch(
    #        hosts=[{'host': self._es_host, 'port': self._es_port}],
    #        use_ssl=True,
    #        verify_certs=True,
    #        connection_class=RequestsHttpConnection
    #    )

    def query_item(self):
        self.setES_CLIENT()
        query_top = "{\"query\": {\"match\": {\"valid\": 0}},\"sort\": {\"position\": {\"order\": \"asc\"}}}"
        query_black = "{\"query\": {\"match\": {\"valid\": 1}}}"
        top = self._es_client.search(index="hotword", body=query_top)
        black = self._es_client.search(index="hotword", body=query_black)
        tophit = top.get("hits").get("hits")
        blackhit = black.get("hits").get("hits")
        return tophit,blackhit
