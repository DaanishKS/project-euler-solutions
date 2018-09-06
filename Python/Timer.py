import time


class Timer:
    def __init__(self):
        self.startTime = time.perf_counter()

    def start(self):
        self.startTime = time.perf_counter()

    def stop(self):
        self.stopTime = time.perf_counter() - self.startTime
        print('\nElasped time is %s seconds' % self.stopTime)
        return self.stopTime
