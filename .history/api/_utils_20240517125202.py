import datetime, os,numpy as np,pandas as pd,requests
import json
from flask import Flask, Blueprint, url_for, request, session, redirect, render_template, jsonify, json
import _mongo_db as mdb
import "./_config.json" as config

taskDB = mdb.mongoDb("mongodb://localhost:27017/", "taskDB")