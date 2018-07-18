

class AloneException(Exception):
    def __init__(self, code, message):
        super(AloneException, self).__init__(message)
        self.code = code
        self.message = message

    def __str__(self):
        return 'code: {}, message: {}'.format(self.code, self.message)
