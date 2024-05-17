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
        pattern = re.compile('{\s*"\$oid":\s*(\"[a-z0-9]{1,}\")\s*}')
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
        for item in res:
            item["created"]	= str(item["created"])
            item["updated"]	= str(item["updated"])	
            
    elif category == 'user':
        res = taskDB.queryCollectionItem('users', {'userName': val})
        res["created"]	= str(res["created"])
        res["updated"]	= str(res["updated"])
    data = dumps(res, json_options=CANONICAL_JSON_OPTIONS)
    data = remove_oid(data)
    return jsonify(json.loads(data))


def tasksManage(command, category, val=None):
    if command == 'get':
        return tasksDataGet(category, val)
    # elif command == 'add':
    #     return tasksDataAdd(category, val)
    # elif command == 'update':
    #     return tasksDataUpdate(category, val)
    # elif command == 'delete':
    #     return tasksDataDelete(category, val)
    # else:
    #     return 'Invalid command'    
       
     

       
 
 
