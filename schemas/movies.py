#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from marshmallow import fields, post_load
from marshmallow.schema import Schema


class Movie(Schema):
	movieId = fields.Integer()
	title = fields.String(required=True)
	genres = fields.String(required=True)
	rating = fields.Integer()
	userId = fields.Integer()
	tag = fields.String()


movie_schema = Movie()
