#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from models.Base import Base
from sqlalchemy import Column, String, Integer


class LinkModel(Base):
    __tablename__ = 'links'
    movieId = Column(Integer)
    imdbId = Column(Integer)
    tmdbId = Column(Integer)
