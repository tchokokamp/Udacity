# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays; "
user_table_drop = "DROP TABLE IF EXISTS users; "
song_table_drop = "DROP TABLE IF EXISTS  songs; "
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
       songplay_id  SERIAL PRIMARY KEY NOT NULL, 
       start_time TIMESTAMP,
       user_id int,
       level varchar(100),
       song_id varchar(100),
       artist_id varchar(100),
       session_id int,
       location  varchar(100),
       user_agent  varchar(150));
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
       user_id int, 
       first_name varchar(100),
       last_name  varchar(100),
       gender char(1),
       level varchar(100)
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
       song_id varchar(100), 
       title varchar(100),
       artist_id varchar(100),
       year int,
       duration decimal(8,3)
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
       artist_id varchar(100), 
       name varchar(100),
       location varchar(100),
       latitude decimal(8,3),
       longitude decimal(8,3)
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
      start_time  TIMESTAMP, 
      hour int,
      day int,
      weekday int,
      month int,
      year int    
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""
INSERT INTO users(user_id,first_name, last_name, gender, level) VALUES(%s,%s,%s,%s,%s);
""")

song_table_insert = ("""
INSERT INTO songs(song_id,title, artist_id, year, duration) VALUES(%s,%s,%s,%s,%s);
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id,name,location,latitude,longitude) VALUES(%s,%s,%s,%s,%s);
""")

time_table_insert = ("""
INSERT INTO time(start_time, hour, day, weekday, month, year) VALUES(%s,%s,%s,%s,%s,%s);
""")



# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id
FROM songs s INNER JOIN artists a 
ON a.artist_id = s.artist_id
WHERE s.title = %s 
AND a.artist_id = %s 
AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]