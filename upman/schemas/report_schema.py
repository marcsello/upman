#!/usr/bin/env python3
from marshmallow import fields, Schema, RAISE


class ReportSchema(Schema):
    info_digest = fields.String(required=True)
    key = fields.String(required=False)

    class Meta:
        load_only = ['info_digest', 'key']
        unknown = RAISE
