from model.Platform import Platform


class New(Platform):

    def __init__(self, start, end, platformId):
        super().__init__(start, end, platformId)
        self.start = start
        self.end = end
        self.platformId = platformId
