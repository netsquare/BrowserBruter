import sys

class Tee:
    def __init__(self, log_file):
        self.log_file = log_file
        self.stdout_orig = sys.stdout

    def write(self, text):
        self.stdout_orig.write(text)
        with open(self.log_file, 'a') as log:
            log.write(text)

    def flush(self):
        self.stdout_orig.flush()
