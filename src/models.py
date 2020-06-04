from . import db


class Account(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'ACCOUNT_INFO'
    accountId = db.Column(db.Integer,
                          primary_key=True)
    name = db.Column(db.String(64),
                     index=False,
                     unique=True,
                     nullable=False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    address = db.Column(db.Text,
                        index=False,
                        unique=False,
                        nullable=True)
    admin = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)
    mobile = db.Column(db.BigInteger,
                       index=False,
                       unique=False,
                       nullable=False)

    def serialize(self):
        return {"accountId": self.accountId,
                "name": self.name,
                "email": self.email,
                "created": self.created,
                "mobile": self.mobile,
                "address": self.address,
                "admin": self.admin}

    def __repr__(self):
        return '<Account {}>'.format(self.name)
