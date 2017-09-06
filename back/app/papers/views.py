import os
from flask import Blueprint, request, jsonify
from flask_apispec import use_kwargs, marshal_with

from .models import Paper
from .serializers import paper_schema, papers_schema
from app.database import db
from app.exceptions import InvalidUsage
from app.extensions import cors
from services.pdf2html import pdf2html

blueprint = Blueprint('papers', __name__)

PY_FOLDER = os.path.abspath(os.path.dirname(__file__))  # This directory
UPLOAD_FOLDER = os.path.abspath(os.path.join(PY_FOLDER, os.pardir, os.pardir)) + '/uploads/pdfs/'


@blueprint.route('/api/papers', methods=['GET'])
# @use_kwargs(papers_schema)
@marshal_with(papers_schema)
def get_papers():
    res = Paper.query
    return res.all()

@blueprint.route('/api/papers', methods=['POST'])
# @use_kwargs(paper_schema)
# @marshal_with(paper_schema)
def make_papers():
    files = request.files.getlist('file')
    print(len(request.files))
    # paperlist = []
    for file in files:
        filename = file.filename
        paper = Paper(filename)
        # paperlist.append(paper)
        pdf_path = UPLOAD_FOLDER + filename
        file.save(pdf_path)
        pdf2html(pdf_path)
    return jsonify({
        'success': True
    })

