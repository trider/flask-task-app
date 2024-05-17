import datetime, datetime, re
from flask import Flask, Blueprint, url_for, request, session, redirect, render_template, jsonify, json
from bson.objectid import ObjectId
from bson.json_util import dumps, JSONOptions, CANONICAL_JSON_OPTIONS, RELAXED_JSON_OPTIONS
from api import _mongo_db as mdb

CANONICAL_JSON_OPTIONS = JSONOptions(datetime_representation=2, json_mode=1, document_class=dict, tz_aware=True)

url = "mongodb+srv://jonnygold:1rHF6hprHIrTZq8Jfeye@cluster0.jlwmt.mongodb.net/?retryWrites=true&w=majority&ignoreUndefined=true"

taskDB = mdb.mongoDb(url, "tasksDB")

def remove_oid(string):
    while True:
        pattern = re.compile('{\s*"\$date":\s*(\"[a-z0-9]{1,}\")\s*}')
        match = re.search(pattern, string)
        if match:
            string = string.replace(match.group(0), match.group(1))
        else:
            return string



def usersManage(command, category, val=None):
    if command == 'get':
        return usersDataGet(category, val)
    else:
        return 'Invalid command'
       
def usersDataGet(category, val=None, data=None):
    if category == 'users':
        res = taskDB.queryCollection('users', {})
    elif category == 'user':
        res = taskDB.queryCollectionItem('users', {'userName': val})
    data = dumps(res, json_options=CANONICAL_JSON_OPTIONS)
    return jsonify(json.loads(remove_oid(data)))
       
     

       
 
 
