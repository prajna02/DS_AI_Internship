CREATE TABLE interns 
(id INTEGER PRIMARY KEY,
name TEXT,
track TEXT,
stipend INTEGER);

INSERT INTO interns (name, track, stipend) VALUES('Asha', 'Data Science', 15000);
INSERT INTO interns (name, track, stipend) VALUES('Rahul', 'Web Dev', 12000);
INSERT INTO interns (name, track, stipend) VALUES('Meena', 'Data Science', 14000);
INSERT INTO interns (name, track, stipend) VALUES('Kiran', 'UI/UX', 13000);
INSERT INTO interns (name, track, stipend) VALUES('Aioon', 'Web Dev', 12500);

select*from interns;

id  name   track         stipend
--  -----  ------------  -------
1   Asha   Data Science  15000
2   Rahul  Web Dev       12000
3   Meena  Data Science  14000
4   Kiran  UI/UX         13000
5   Aioon  Web Dev       12500


select name, track from interns;

name   track
-----  ------------
Asha   Data Science
Rahul  Web Dev
Meena  Data Science
Kiran  UI/UX
Aioon  Web Dev
