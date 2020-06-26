import sys


class Hnode:

    def __init__(self, val, name):
        self.keyval = val
        self.name = name
        self.next = None


class Htable:

    def __init__(self, size):
        self.tsize = size
        self.entries = []

    def hash(self, string):  # returns an integer key
        out = 0
        for i in range(len(string)):
            out += ord(string[i]) * (i + 1)

        return out % self.tsize

    def add(self,node):
        loc = hash(node.keyval)
        nextnode = self.entries[loc]
        node.next = nextnode
        self.entries[loc] = node

    def find(self, key):
        index = hash(key)
        out = self.entries[index]
        if out is None:
            return out
        found = False
        while out is not None and found is not True:
            if out.keyval == key:
                found = True
            else:
                out = out.next
        return out

def main():
    


if __name__ == '__main__':
    main()
