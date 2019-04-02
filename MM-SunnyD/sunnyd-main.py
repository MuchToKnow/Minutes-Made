#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MM-Sunnyd - sunnyd-main.py
# Minutes Made, Copyright 2019
# Maintainer: Harry Yao

import config_mm as conf

from quart import Quart, abort, Blueprint, current_app, jsonify, request
from flask_pymongo import PyMongo

app = Quart(__name__)

@app.before_first_request
async def create_db():
    """Connect to the postgres database."""
    app.config['MONGO_URI'] = conf.MONGOCONNECTIONURI
    app.mongo = PyMongo(app)

@app.route('/transcripts/add', methods=['POST'])
async def transcripts_add():
    """Adds a transcript to the MongoDB database"""
    data = await request.get_json()
    if data.get('SpeakerID', None) is not None and data.get('Text', None) is not None:
        app.mongo.db.transcripts.insert_one(data)
        return jsonify({'success': True, 'message': 'Transcript successfully added'}), 200
    return jsonify({'success': False, 'message': 'Bad request parameters'}), 400

if __name__ == "__main__":
    app.run()
