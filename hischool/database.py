from hischool import db

class School(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String)
    data = db.Column(db.PickleType())

    def __repr__(self):
        return '<School %r>' % self.keyword

db.create_all()
