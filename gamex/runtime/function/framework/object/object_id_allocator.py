class ObjectID:
    ACCUM_ID = 0

    @staticmethod
    def alloc(self):
        id = ObjectID.ACCUM_ID
        ObjectID.ACCUM_ID += 1
        return id
