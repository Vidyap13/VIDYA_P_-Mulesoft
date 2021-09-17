import sqlite3
conn=sqlite3.connect('moviesdb.sqlite')
cur=conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Movies;
CREATE TABLE Movies(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    actor TEXT,
    actress TEXT,
    director TEXT,
    year_of_release INTEGER
);
''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Me Before You', 'Sam Claffin', 'Emilia Clarke', 'Thea Sharrock', 2016)''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('The Notebook', 'Ryan Gosling', 'Rachael McAdams', 'Nick Cassavetes', 2004)''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Midnight Sun', 'Patrick Schwarzenegger', 'Bella Thorne', 'Scott Speer', 2018)''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Aquaman', 'Jason Momoa', 'Amber Heard', 'James Wan', 2018)''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('The Fault In Our Stars', 'Ansel Elgort', 'Shailene Woodley', ' Josh Boone', 2014)''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('The Vow', 'Channing Tatum', 'Rachel McAdams', 'Michael Sucsy', 2012)''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('The Da Vinci Code', 'Tom Hanks', 'Audrey Tautou', ' Ron Howard', 2006)''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('San Andreas', 'Dwayne Johnson', 'Carla Gugino', 'Brad Peyton', 2015)''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('A Star Is Born', 'Bradley Cooper', 'Lady Gaga', 'Bradley Cooper', 2018)''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Jungle Cruise', 'Dwayne Johnson', 'Emily Blunt', 'Jaume Collet-Serra', 2021)''')
cur.execute('''INSERT INTO Movies(title,actor,actress,director,year_of_release) VALUES
   ('Extraction', 'Chris Hemsworth', 'Golshifteh Farahani', 'Sam Hargrave', 2020)''')

sql_all = 'SELECT * FROM Movies'
print ("\n{:<5} {:<30} {:<25}{:<25} {:<25} {:<20}\n".format('Id','Title','Actor','Actress','Director','Year Of Release'))
for row in cur.execute(sql_all):
    id,title,actor,actress,director,year_of_release=row
    print ("{:<5} {:<30} {:<25}{:<25} {:<25} {:<20}".format(id,title,actor,actress,director,year_of_release))

actor_search=input("\nEnter the actor name: ")
print('\nMovies starring '+actor_search+' are: \n' )
print("{:<30}{:<25}{:<25}{:<20}\n".format('Title','Actress','Director','Year of Release'))
for row in cur.execute('SELECT title,actress,director,year_of_release FROM Movies WHERE actor= ?',(actor_search,)):
    title,actress,director,year_of_release=row
    print("{:<30}{:<25}{:<25}{:<20}".format(title,actress,director,year_of_release))
conn.commit()