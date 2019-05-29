from elasticsearch import Elasticsearch
import sys
import os
import json
import time
from elasticsearch import  helpers


HOST = "http://localhost:9200/"
es = Elasticsearch(hosts=[HOST])

request_body = {
    "settings" : {
        "number_of_shards": 5,
        "number_of_replicas": 0
    }
}

mapping = {
		"document": {
			"properties": {
				"id": {"type":"text"},
				"title": {"type":"text", "analyzer": "english"},
				"body": {"type":"text", "analyzer": "english"},
				"categorie": {"type":"keyword"},
		        "viewcount": {"type":"integer"},
		        "score": {"type":"integer"},
		        "creation_date": {"type":"date", "format": "date_hour_minute_second"},
		        "answers": {"type":"text", "analyzer": "english"},
		        "comments": {"type":"text", "analyzer": "english"},
		        "answer_score": {"type":"integer"},
		        "accepted_answer": {"type":"text", "analyzer": "english"},
		        "accepted_answer_score": {"type":"integer"},
		        "link": {"type":"text", "analyzer": "english"},
			}
		}
}

try:
	es.indices.delete(index='index')
except:
	pass

es.indices.create(index = 'index', body = request_body)
es.indices.put_mapping(index="index", doc_type="document", body=mapping, include_type_name=True)


folder = tuple(os.listdir('json_bulks'))

title = "lifehacks1.json"

for bulk in folder:
	print(bulk)
	os.system("curl -s -XPOST 'http://localhost:9200/_bulk'  -H 'Content-Type: application/json' --data-binary @json_bulks/" + bulk)

