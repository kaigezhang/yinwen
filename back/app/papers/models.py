from app.database import Column, Model, SurrogatePK, db


class Paper(SurrogatePK, Model):
    __tablename__ = 'papers'

    id = Column(db.Integer, primary_key=True, autoincrement=True)
    filename = Column(db.String(100), unique=True, nullable=False)


    def __init__(self, filename):
        db.Model.__init__(self, filename=filename)

    def __repr__(self):
        return '<Paper({filename!r})'.format(filename=self.filename)