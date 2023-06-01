from marshmallow import Schema
from marshmallow import fields


class UserSchema(Schema):
    """Default users schema"""

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    admin = fields.Str(load_only=True, default=False)


class UserRegisterSchema(UserSchema):
    """Register user Schema"""

    email = fields.Str(required=True)
    cgc = fields.Str(required=True, load_only=True)
