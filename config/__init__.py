#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


class Config:
	APP_NAME = os.environ.get('APP_NAME', str('Movie Lens Search Api'))
	BRANCH_NAME = os.environ.get('BRANCH_NAME', str('develop'))
<<<<<<< HEAD
	DATABASE_URL = os.environ.get('DATABASE_URL', str('mysql+pymysql://root:testpass@localhost/challenge?local_infile=1'))
=======
	DATABASE_URL = os.environ.get('DATABASE_URL', str('mysql+pymysql://root:testpass@localhost/challenge'))
>>>>>>> 26af151738f48cbc3baae784ecd9a5455fbd5a9d
	ENVIRONMENT = os.environ.get('ENVIRONMENT', str('local'))
	SECRET = os.environ.get('SECRET', str('foobar'))
	DEBUG = os.environ.get('DEBUG', bool(
		True))  # IMPORTANT: this must be set 'False' for production security of GET /token !!!
	URL = os.environ.get('URL', str('http://127.0.0.1:5000/'))
