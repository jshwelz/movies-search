#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from models.Base import Base
from sqlalchemy import Column, String, Integer


class TagsModel(Base):
    __tablename__ = 'tags'
    movieId = Column(Integer)
    userId = Column(Integer, primary_key=True)
    tag = Column(String)
