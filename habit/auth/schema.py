from marshmallow import Schema, fields


class Users(Schema):

    user_id = fields.Int()
    username = fields.Str()
    password = fields.Str(load_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    phone = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()
    last_login = fields.DateTime()
    is_archive = fields.Bool()


class Habit(Schema):

    habit_id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    user_id = fields.Int()
    is_archive = fields.Bool()

