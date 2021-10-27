#!/usr/bin/env python3
from flask import abort, Response
from flask_classful import FlaskView, route, request
from utils import json_required

from marshmallow import ValidationError

from schemas import ReportSchema


class ReportView(FlaskView):
    report_schema = ReportSchema(many=False)

    def _make_report(self, key: str, info_digest: str) -> Response:
        return Response(status=201)

    @route("/<key>/<info_digest>")
    def get_combo(self, key: str, info_digest: str):
        return self._make_report(key, info_digest)

    @route("/<info_digest>")
    def get(self, info_digest: str):
        key = request.headers.get('Authorization')
        if not key:
            return abort(401, "No key provided")
        return self._make_report(key, info_digest)

    @json_required
    def post(self):
        try:
            report = self.report_schema.load(request.json)
        except ValidationError as e:
            return abort(422, str(e))

        key = report.get('key', request.headers.get('Authorization'))
        if not key:
            return abort(401, "No key provided")

        return self._make_report(key, report['info_digest'])
