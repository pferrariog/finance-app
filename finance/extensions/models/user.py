from finance.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    """Default user model"""

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        doc="identification number",
        comment="Integer representing the sequence number",
    )
    name = db.Column(
        db.String(255),
        nullable=False,
        doc="username",
        comment="Current user name used to identify",
    )
    email = db.Column(
        db.String, unique=True, nullable=False, doc="user email", comment="Primary user email"
    )
    cgc = db.Column(
        db.String,
        unique=True,
        nullabel=False,
        doc="cpf/cnpj",
        comment="User government register - CPF/CNPJ",
    )
    password = db.Column(
        db.String(255), unique=True, nullable=False, doc="", comment="User password"
    )
    admin = db.Column(
        db.Boolean, default=False, doc="admin status", comment="Status that set admin privileges"
    )
