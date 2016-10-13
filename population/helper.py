def noApos(x):
    return x.replace("'","''").replace("’","''").replace("ʼ","''")

def resetTables(cursor):
    cursor.execute("DELETE FROM has_genre")
    cursor.execute("DELETE FROM has_cast")
    cursor.execute("DELETE FROM has_crew")
    cursor.execute("DELETE FROM produced_by")
    cursor.execute("DELETE FROM Movies")
    cursor.execute("DELETE FROM Genre")
    cursor.execute("DELETE FROM Person")
    cursor.execute("DELETE FROM Company")

def deleteTables(cursor):
    cursor.execute("DROP TABLE Movies CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE Genre CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE Person CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE Company CASCADE CONSTRAINTS")
    cursor.execute("DROP TABLE has_genre")
    cursor.execute("DROP TABLE has_cast")
    cursor.execute("DROP TABLE has_crew")
    cursor.execute("DROP TABLE produced_by")

def remakeTables(cursor):
    cursor.execute("""
        CREATE TABLE Movies(movie_id number NOT NULL PRIMARY KEY,
            title varchar(500) NOT NULL,
            release_date varchar(50),
            budget number,
            revenue number,
            popularity number,
            overview varchar(2000),
            poster_path varchar(100),
            run_time number)
    """)
    cursor.execute("""
        CREATE TABLE Genre(genre_id number NOT NULL PRIMARY KEY,
            name varchar(300) NOT NULL)
    """)
    cursor.execute("""
        CREATE TABLE Person(person_id number NOT NULL PRIMARY KEY,
            name varchar(300) NOT NULL,
            poster_path varchar(100))
    """)
    cursor.execute("""
        CREATE TABLE Company(company_id number NOT NULL PRIMARY KEY,
            name varchar(300) NOT NULL)
    """)
    cursor.execute("""
        CREATE TABLE has_genre(movie_id number NOT NULL REFERENCES Movies(movie_id),
            genre_id number NOT NULL REFERENCES Genre(genre_id))
    """)
    cursor.execute("""
        CREATE TABLE has_cast(movie_id number NOT NULL REFERENCES Movies(movie_id),
            person_id number NOT NULL REFERENCES Person(person_id),
            role varchar(300),
            ord number)
    """)
    cursor.execute("""
        CREATE TABLE has_crew(movie_id number NOT NULL REFERENCES Movies(movie_id),
            person_id number NOT NULL REFERENCES Person(person_id),
            job varchar(300) NOT NULL,
            department varchar(300))
    """)
    cursor.execute("""
        CREATE TABLE produced_by(movie_id number NOT NULL REFERENCES Movies(movie_id),
            company_id number NOT NULL REFERENCES Company(company_id))
    """)

def printCount(cursor):
    print(cursor.execute("select count(*) from movies").fetchall())
    print(cursor.execute("select count(*) from genre").fetchall())
    print(cursor.execute("select count(*) from has_genre").fetchall())
    print(cursor.execute("select count(*) from company").fetchall())
    print(cursor.execute("select count(*) from produced_by").fetchall())
    print(cursor.execute("select count(*) from person").fetchall())
    print(cursor.execute("select count(*) from has_cast").fetchall())
    print(cursor.execute("select count(*) from has_crew").fetchall())
