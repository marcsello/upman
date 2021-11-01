#!/usr/bin/env python3
from flask import jsonify, abort, Response, request
from flask_classful import FlaskView
from schemas import ReporterSchema
from model import db, Reporter
from marshmallow import ValidationError
from utils import json_required, apikey_required
from sqlalchemy.exc import IntegrityError


class ReporterView(FlaskView):
    reporters_schema = ReporterSchema(many=True)
    reporter_schema = ReporterSchema(many=False)

    decorators = [apikey_required]

    def index(self):
        reporters = Reporter.query.all()
        return jsonify(self.reporters_schema.dump(reporters))

    def get(self, id_: int):
        reporter = Reporter.query.get_or_404(id_)
        return jsonify(self.reporter_schema.dump(reporter))

    @json_required
    def post(self):
        try:
            reporter = self.reporter_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return abort(422, str(e))

        db.session.add(reporter)
        try:
            db.session.commit()
        except IntegrityError:
            abort(409)

        return jsonify(self.reporter_schema.dump(reporter)), 201

    @json_required
    def patch(self, id_: int):
        reporter = Reporter.query.get_or_404(id_)

        try:
            reporter = self.reporter_schema.load(request.json, session=db.session, instance=reporter, partial=True)
        except ValidationError as e:
            return abort(422, str(e))

        db.session.add(reporter)
        try:
            db.session.commit()
        except IntegrityError:
            abort(409)

        return jsonify(self.reporter_schema.dump(reporter)), 200

    def delete(self, id_: int):
        reporter = Reporter.query.get_or_404(id_)
        db.session.delete(reporter)
        db.session.commit()
        return Response(status=204)
