from tree import db


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<User id={self.id} name={self.name}>'
