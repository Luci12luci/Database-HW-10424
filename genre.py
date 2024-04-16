class Genre:
    def __init__(self, id):
        self.id = genre_id

@classmethod
def from_db(cls, value):
    return cls(value[0])

@staticmethod
def vloz_do_db(cursor):
    print("vlozte zaner:")
    cursor.execute("INSERT INTO genre (genre) VALUES(%s)", (zaner))
    print(zaner)

def __str__(self):
    return f" ---GENRE---\nID Genre: {self.genre_id}"