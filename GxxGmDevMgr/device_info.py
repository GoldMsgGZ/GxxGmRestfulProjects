#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8

from app import database

class device_info:
    id = database.Column(database.Integer, primary_key=True)
