from marshmallow import Schema, fields
from marshmallow.validate import Length, Range

class ReviewSchema(Schema):
    feedback = fields.Str(validate=Length(3, 10))
    grade = fields.Int(validate=Range(1, 100))


REVIEW_SCHEMA = {
    '#schema': 'https://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'feedback': {
            'type': 'string',
            'minLength': 5,
            'maxLength': 100,
        },
        'grade': {
            'type': 'integer',
            'minimum': 1,
            'maximum': 100
        },
    },
    'required': ['feedback', 'grade']
}