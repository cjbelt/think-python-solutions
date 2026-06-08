class Kangaroo(object):
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        return "Kangaroo's Pouch: %s" % self.pouch_contents

if __name__ == '__main__':
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)
