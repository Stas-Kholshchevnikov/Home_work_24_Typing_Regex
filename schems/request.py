from marshmallow import Schema, fields


class RequestSchema(Schema):
    """
    Схема запроса для валидации
    """
    cmd1 = fields.Str(required=True)
    val1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    val2 = fields.Str(required=True)
    file_name = fields.Str()
