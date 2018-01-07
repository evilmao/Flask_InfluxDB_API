#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", 'gif'}
app = Flask(__name__)
app.config.from_object("config")

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS
# 判断文件名称是否支持

from app import views, models