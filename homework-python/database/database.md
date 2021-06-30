https://www.youtube.com/watch?v=TwnCXdCa8qg - series of videos

https://docs.python.org/3/library/sqlite3.html - official module docs

## sqlite browser

https://sqlitebrowser.org/

Install in linux:

    sudo apt-get install sqlitebrowser


## SQL

https://www.sqltutorial.org/sql-data-types/

https://www.sqltutorial.org/sql-syntax/


### create table

    CREATE TABLE IF NOT EXISTS time_slots (
         "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         "start" DATETIME NOT NULL,
         "status" VARCHAR DEFAULT "available"
    );


### select 

    select * from time_slots;;

with a condition

    SELECT id, status from time_slots 
    WHERE start > '2020-02-01';

or 

    select * from time_slots 
    WHERE id < 2;

with some computations

    SELECT CAST(id + 1000 AS text) || 'some_suffix', DATETIME(start) from time_slots 
    WHERE start > '2020-02-01';

### delete table 

    DROP TABLE time_slots;
    DROP TABLE IF EXISTS time_slots;



### insert

    INSERT INTO time_slots(id, start, status) 
    VALUES (4, "2020-04-01 20:20", "available");

UNIQUE constraint is checked

many:

    INSERT INTO time_slots(id, start, status) 
    VALUES 
	(1, "2020-01-01 20:20", "available"),
	(2, "2020-02-02 20:20", "available"),
	(3, "2020-03-03 20:20", "booked")
	;


### delete rows

all 

    DELETE from time_slots;

according to the filter

### update 
    
    UPDATE t
    SET c1 = new_value, 
        c2 = new_value
    WHERE condition;


