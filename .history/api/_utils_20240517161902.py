import datetime
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
        resp = taskDB.queryCollectionItem('users', {'userName': val})
   
        res = {
         "_id": str(resp['_id']),
         "userName": resp['userName'], 
         "email": resp['email'], 
         "password": resp['password'],
         "created": str(resp['created']),
         "updated": resp['updated']
         }

    data = dumps(res, json_options=CANONICAL_JSON_OPTIONS)
    return jsonify(json.loads(data))
       
     

       
 
 
