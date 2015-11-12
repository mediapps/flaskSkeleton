# -*- coding: utf-8 -*-
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_from_directory
from datetime import datetime,time, timedelta, date
import traceback
import utils
import os

from config.config import MACHINE, SECRET_KEY

######################## APP CONFIGURATION ########################

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY= SECRET_KEY,
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


######################## APP FLOW ########################

@app.route('/')
def display_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=MACHINE["HOST"], port=MACHINE["PORT"])