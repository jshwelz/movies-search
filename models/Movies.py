#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from models.Base import Base
from sqlalchemy import Column, String, Integer


class MoviesModel(Base):
    __tablename__ = 'movies'
    movieId = Column(Integer, primary_key=True)
    title = Column(String)
    genres = Column(String)
