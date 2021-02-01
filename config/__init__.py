#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


class Config:
	APP_NAME = os.environ.get('APP_NAME', str('Movie Lens Search Api'))
	DATABASE_URL = os.environ.get('DATABASE_URL', str('mysql+pymysql://root:testpass@localhost/challenge?local_infile=1'))
	ENVIRONMENT = os.environ.get('ENVIRONMENT', str('local'))
	SECRET = os.environ.get('SECRET', str('foobar'))
	URL = os.environ.get('URL', str('http://127.0.0.1:5000/'))
