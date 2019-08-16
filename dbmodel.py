from server import db
    
class Dataset(db.Model):
    __tablename__ = 'datasets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True)
    password = db.Column(db.String(20), index=True)

    def __init__(self, username, password):
        self.name = name
        self.password = author

    def __repr__(self):
        return '<id {}>'.format(self.id)