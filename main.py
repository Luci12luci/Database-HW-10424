import psycopg2
from author import Author
from genre import Genre
from book import Book
from member import Member

conn = psycopg2.connect(
    dbname='b4l1o2iguxktujhgmzv1',
    user='uhkelmgkhpkwcyjdl3qd',
    password='ZIuTMMFceJbOGxBmDJGxtBRfTrRVSs',
    host='b4l1o2iguxktujhgmzv1-postgresql.services.clever-cloud.com',
    port=50013
)

cursor = conn.cursor()
def vypis_menu():
    print("1. Pridat autora")
    print("2. Pridat zaner")
    print("3. Pridat knihu")
    print("4. Pridat clena")

def aplikacia():
    while True:
        vypis_menu()
        choice = input("Vasa moznost: ")
        if choice == "1":
            Author.vloz_do_db(cursor)
            conn.commit()
        elif choice == "2":
            Genre.vloz_do_db(cursor)
            conn.commit()
        elif choice == "3":
            Author.zobraz_autorov(cursor)
            authorID = input("ID Authora: ")
            Genre.zobraz_zanre(cursor)
            genreID = input("ID zanru: ")
            Book.vloz_do_db(cursor, authorID, genreID)
            conn.commit()
        elif choice == "4":
            Member.vloz_do_db(cursor)
            conn.commit()
        else:
            print("Neplatny vstup")

aplikacia()
