#!/usr/bin/env python3
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from model import Reporter


class ReporterSchema(SQLAlchemyAutoSchema):

    name = fields.String(required=True)
    key = fields.String(required=True)

    class Meta:
        dump_only = ['id', 'created', 'info_digest', 'last_seen']
        load_only = ['key']
        model = Reporter
        include_relationships = True
        load_instance = True
        include_fk = False
