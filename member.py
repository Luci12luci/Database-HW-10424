class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name

@classmethod
def from_db(cls, value):
    return cls(value[0], value[1])

@staticmethod
def vloz_do_db(cursor):
    print("vlozte meno clena:")
    meno = input()
    cursor.execute("INSERT INTO memeber (name) VALUES(%s)", (meno))
    print(meno)

def __str__(self):
    return f" ---MEMBER---\nID Clena: {self.id}\nMeno: {self.name}"