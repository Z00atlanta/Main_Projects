# Name: Logan Warren
# Assignment: Module 6 - Assignment 6
# 4/20/26

import sqlite3

connection = sqlite3.connect("LoganCompany.sqlite")
cur = connection.cursor()

print("Database Connected.")

cur.execute('DROP TABLE IF EXISTS works_on')
cur.execute('DROP TABLE IF EXISTS employee')
cur.execute('DROP TABLE IF EXISTS project')
cur.execute('DROP TABLE IF EXISTS department')
connection.commit()

cur.execute('CREATE TABLE department(dept_num TEXT PRIMARY KEY, dept_name TEXT, location TEXT)')

cur.execute('CREATE TABLE employee(emp_num INTEGER PRIMARY KEY, emp_fname TEXT, emp_lname TEXT, dept_num TEXT, FOREIGN KEY(dept_num) REFERENCES department(dept_num))')

cur.execute('CREATE TABLE project(project_num TEXT PRIMARY KEY, project_name TEXT, budget INTEGER)')

cur.execute('CREATE TABLE works_on(emp_num INTEGER, project_num TEXT, job TEXT, enter_date TEXT, FOREIGN KEY(emp_num) REFERENCES employee(emp_num), FOREIGN KEY(project_num) REFERENCES project(project_num))')
connection.commit()

cur.execute('INSERT INTO department VALUES("d1","Mathematics","Dallas")')
cur.execute('INSERT INTO department VALUES("d2","Accounting","Seattle")')
cur.execute('INSERT INTO department VALUES("d3","Marketing","Dallas")')
connection.commit()

cur.execute('INSERT INTO employee VALUES(25348,"Matthew","Smith","d1")')
cur.execute('INSERT INTO employee VALUES(10102,"Ann","Jones","d2")')
cur.execute('INSERT INTO employee VALUES(18316,"Elizabeth","Smith","d3")')
cur.execute('INSERT INTO employee VALUES(29346,"James","James","d1")')
cur.execute('INSERT INTO employee VALUES(12325,"Alex","Lopez","d2")')
cur.execute('INSERT INTO employee VALUES(90042,"John","Barrimore","d1")')
cur.execute('INSERT INTO employee VALUES(9031,"Elke","Hansel","d3")')
cur.execute('INSERT INTO employee VALUES(2581,"Elsa","Bertoni","d2")')
cur.execute('INSERT INTO employee VALUES(28559,"Sybill","Moser","d1")')
connection.commit()

cur.execute('INSERT INTO project VALUES("p1","Apollo",120000)')
cur.execute('INSERT INTO project VALUES("p2","Germini",95000)')
cur.execute('INSERT INTO project VALUES("p3","Mercury",186500)')
connection.commit()

cur.execute('INSERT INTO works_on VALUES(10102,"p1","Analyst","2021.10.1")')
cur.execute('INSERT INTO works_on VALUES(10102,"p3","Manager","2021.1.1")')
cur.execute('INSERT INTO works_on VALUES(25348,"p2","Clerk","2020.7.15")')
cur.execute('INSERT INTO works_on VALUES(18316,"p2",NULL,"2007.6.1")')
cur.execute('INSERT INTO works_on VALUES(29346,"p3",NULL,"2020.10.11")')
cur.execute('INSERT INTO works_on VALUES(2581,"p2","Analyst","2020.10.25")')
cur.execute('INSERT INTO works_on VALUES(9031,"p1","Manager","2018.2.13")')
cur.execute('INSERT INTO works_on VALUES(28559,"p2",NULL,"2019.4.7")')
cur.execute('INSERT INTO works_on VALUES(28559,"p3","Clerk","2015.3.14")')
cur.execute('INSERT INTO works_on VALUES(9031,"p2","Manager","2016.4.7")')
cur.execute('INSERT INTO works_on VALUES(29346,"p1","Analyst","2007.1.4")')
cur.execute('INSERT INTO works_on VALUES(12325,"p1","Clerk","2020.12.1")')
cur.execute('INSERT INTO works_on VALUES(12325,"p2",NULL,"2002.5.16")')
cur.execute('INSERT INTO works_on VALUES(90042,"p2","Analyst","2012.6.18")')
cur.execute('INSERT INTO works_on VALUES(9031,"p3","Manager","2016.4.18")')
connection.commit()

cur.execute('UPDATE department SET location="Washington" WHERE dept_num="d1"')

cur.execute('DELETE FROM employee WHERE emp_fname="James" AND emp_lname="James"')
connection.commit()

print("\nThe employee table:")
cur.execute("SELECT * FROM employee")
for row in cur:
    print(row)

print("\nThe department table:")
cur.execute("SELECT * FROM department")
for row in cur:
    print(row)

print("\nThe works_on table:")
cur.execute("SELECT * FROM works_on")
for row in cur:
    print(row)

print("\nEmployees working on Apollo:")
cur.execute(
'SELECT employee.emp_fname, employee.emp_lname, department.dept_name, department.location ' \
'FROM employee JOIN department ON employee.dept_num = department.dept_num ' \
'JOIN works_on ON employee.emp_num = works_on.emp_num ' \
'JOIN project ON works_on.project_num = project.project_num ' \
'WHERE project.project_name = "Apollo"'
)

for row in cur:
    print(row)