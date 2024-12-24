from collections import defaultdict

class Logger:

    def __init__(self):
        self.messageDict = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messageDict or self.messageDict[message] <= timestamp:
            self.messageDict[message] = timestamp + 10
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)