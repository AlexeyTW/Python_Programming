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