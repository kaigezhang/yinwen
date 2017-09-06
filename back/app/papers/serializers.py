from marshmallow import Schema, fields, pre_load, post_dump

class PaperSchema(Schema):
    filename = fields.Str()

    @pre_load
    def make_paper(self, data):
        data = data['file']
        return data

    @post_dump
    def dump_paper(self, data):
        return {
            'file': data
        }


paper_schema = PaperSchema()
papers_schema = PaperSchema(many=True)