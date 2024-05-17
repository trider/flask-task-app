import datetime, os,numpy as np,pandas as pd,requests
import json
from flask import Flask, Blueprint, url_for, request, session, redirect, render_template, jsonify, json
from bson.objectid import ObjectId
from bson.json_util import dumps, JSONOptions, CANONICAL_JSON_OPTIONS, RELAXED_JSON_OPTIONS
from api import _mongo_db as mdb

url = "mongodb+srv://jonnygold:1rHF6hprHIrTZq8Jfeye@cluster0.jlwmt.mongodb.net/?retryWrites=true&w=majority&ignoreUndefined=true"

taskDB = mdb.mongoDb(url, "tasksDB")


def usersManage(command, category, val=None):
    if command == 'get':
        return usersDataGet(category, val)
    else:
        return 'Invalid command'
       
def usersDataGet(category, val=None, data=None):
    if category == 'users':
        res = taskDB.queryCollection('users', {})
    elif category == 'user':
        res = taskDB.queryCollectionById('users', val)
     
    data = dumps(res, json_options=CANONICAL_JSON_OPTIONS)
    return jsonify(json.loads(data))
       
     

       
 
 
