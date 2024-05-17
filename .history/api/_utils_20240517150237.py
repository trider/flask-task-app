import datetime, os,numpy as np,pandas as pd,requests
import json
from flask import Flask, Blueprint, url_for, request, session, redirect, render_template, jsonify, json
from bson.objectid import ObjectId
from bson.json_util import dumps, JSONOptions, CANONICAL_JSON_OPTIONS, RELAXED_JSON_OPTIONS
from api import _mongo_db as mdb

url = "mongodb+srv://jonnygold:1rHF6hprHIrTZq8Jfeye@cluster0.jlwmt.mongodb.net/?retryWrites=true&w=majority&ignoreUndefined=true"

taskDB = mdb.mongoDb(url, "tasksDB")


def usersManage(command, target, val, request):
 if command == 'get':
  return usersGet(target, val)
  
  
def usersGet(target, val):
 if target == 'users':
  return getCollection(target {})
 elif target == 'user':
  return getCollection(target, {"username": val})
 

def getCollection(collection, query):
	res = taskDB.queryCollection(collection, query)
	print(res)
	data = dumps(res, json_options=CANONICAL_JSON_OPTIONS)
	return jsonify(json.loads(data))

 