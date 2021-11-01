#!/usr/bin/env python3
from .db import db
from sqlalchemy.sql import func


class Reporter(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    created = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())

    key = db.Column(db.String(512), unique=True, nullable=False)

    info_digest = db.Column(db.String(32), nullable=True, default=None)
    last_seen = db.Column(db.DateTime(timezone=True), nullable=True, default=None)
