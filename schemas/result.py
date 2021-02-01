#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from marshmallow import fields
from marshmallow.schema import Schema


class Result(Schema):
	result_type = fields.String()
	data = fields.List(fields.Dict())
	count = fields.Integer()
	total = fields.Integer()
	page = fields.Integer()
	pageCount = fields.Integer()


result_schema = Result()
