class error:
    @classmethod
    def INVALID(cls, value, entity='Value'):
        return "Invalid {}: {}.".format(entity, value)

    @classmethod
    def MISSING(cls, missing_info):
        return "Missing {} info.".format(missing_info)

    @classmethod
    def NOFILE(cls, file):
        return "Missing {} file.".format(file)
