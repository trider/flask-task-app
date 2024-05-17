import datetime, os,numpy as np,pandas as pd,requests
import json
from flask import Flask, Blueprint, url_for, request, session, redirect, render_template, jsonify, json
from bson.objectid import ObjectId
from bson.json_util import dumps, JSONOptions, CANONICAL_JSON_OPTIONS, RELAXED_JSON_OPTIONS
from api import _mongo_db as mdb

url = "mongodb+srv://jonnygold:1rHF6hprHIrTZq8Jfeye@cluster0.jlwmt.mongodb.net/?retryWrites=true&w=majority&ignoreUndefined=true"

taskDB = mdb.mongoDb(url, "tasksDB")


def usersManage(target, command, val):
 if command == 'get':
  if target == 'users':
   return getCollection(target, {})
  else:
   return 'Invalid target'
 else:
  return 'Invalid command'



def getCollection(collection, query):
	res = taskDB.queryCollection(collection, query)
	print(res)
	data = dumps(res, json_options=CANONICAL_JSON_OPTIONS)
	return jsonify(json.loads(data))

 