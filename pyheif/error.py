class HeifError(Exception):
    def __init__(self, code, subcode, message):
        self.code = code
        self.subcode = subcode
        self.message = message

    def __str__(self):
        return 'Code: {}, Subcode: {}, Message: "{}"'.format(self.code, self.subcode, self.message)

    def __repr__(self):
        return 'HeifError({}, {}, "{}"'.format(self.code, self.subcode, self.message)
