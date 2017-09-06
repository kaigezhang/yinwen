import os
from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with

from .models import Paper
from .serializers import paper_schema, papers_schema
from app.database import db
from app.exceptions import InvalidUsage
from app.extensions import cors

blueprint = Blueprint('papers', __name__)

PY_FOLDER = os.path.abspath(os.path.dirname(__file__))  # This directory
UPLOAD_FOLDER = os.path.abspath(os.path.join(PY_FOLDER, os.pardir, os.pardir)) + '/uploads'


@blueprint.route('/api/papers', methods=['GET'])
# @use_kwargs(papers_schema)
@marshal_with(papers_schema)
def get_papers():
    res = Paper.query
    return res.all()

@blueprint.route('/api/papers', methods=['POST'])
@use_kwargs(papers_schema)
@marshal_with(papers_schema)
def make_papers(filename):
    files = request.files.getlist('file')
    paperlist = []
    for file in files:
        filename = file.filename
        paper = Paper(filename=filename)
        paperlist.append(paper)
        file.save(UPLOAD_FOLDER, filename)
    return paperlist

