#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from marshmallow import fields
from marshmallow.schema import Schema


class Tag(Schema):
	movieId = fields.Integer(required=True)
	userId = fields.Integer(required=True)
	title = fields.String(required=True)
	tag = fields.String(required=True)


tag_schema = Tag()
