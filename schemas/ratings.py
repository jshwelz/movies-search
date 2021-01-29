#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from marshmallow import fields
from marshmallow.schema import Schema


class Rating(Schema):
	title = fields.String(required=True)
	genres = fields.String(required=True)
	# @post_load: Register a method to invoke after deserializing an object.
	#             The method receives the deserialized data and returns the processed data.



rating_schema = Rating()
