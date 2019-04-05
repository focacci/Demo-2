class Platform:

    def __init__(self, start, end, platformId):
        self.start = start
        self.end = end
        self.platformId = platformId

    def next(self):
        return self.platformId + 1
