from . import db


class Manufacturer(db.Model):
    __tablename__ = 'manufacturers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    automobiles = db.relationship('Automobile', backref='manufacturer',
                                  lazy='dynamic')

    def __repr__(self):
        return '<Manufacturer %r>' % self.name


class Automobile(db.Model):
    __tablename__ = 'automobiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'),
                                nullable=False)

    def __repr__(self):
        return '<Automobile %r>' % self.name
