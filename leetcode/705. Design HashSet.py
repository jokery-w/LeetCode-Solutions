class MyHashSet(object):
    def __init__(self):
        self.dict = {}

    def add(self, key):
        if key not in self.dict:
            self.dict[key] = True

    def remove(self, key):
        if key in self.dict:
            self.dict.pop(key)

    def contains(self, key):
        if key in self.dict:
            return True
        return False

