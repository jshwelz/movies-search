#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from models.Base import Base
from sqlalchemy import Column, String, Integer, BIGINT


class RatingsModel(Base):
    __tablename__ = 'ratings'
    movieId = Column(Integer)
    userId = Column(Integer, primary_key=True)
    rating = Column(BIGINT)
