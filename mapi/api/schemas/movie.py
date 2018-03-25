from marshmallow import fields, Schema

class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    director = fields.String(allow_none=True)
    genres = fields.List(fields.String())
    year = fields.Integer(required=True)

class MovieUpdateSchema(Schema):
    name = fields.String()
    director = fields.String()
    genres = fields.List(fields.String())
    year = fields.Integer()