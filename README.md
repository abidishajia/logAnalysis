# Log Analysis

### About

In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. 

### Setup
  Install Vagrant And VirtualBox
  Clone this repository

### To Run
  Launch Vagrant VM by running vagrant up, you can the log in with vagrant ssh
  To load the data, use the command psql -d news -f newsdata.sql to connect a database and run the necessary SQL statements.
  To execute the program, run python3 newsdata.py from the command line.


#### View
``` CREATE VIEW dailyErrors AS SELECT daily_log.date, round(daily_error.error_request * 100.0 / daily_log.total_request, 2) AS error_log FROM ( select time::date AS date, count(*) AS total_request FROM log GROUP BY date ) AS daily_log join ( select time::date as date, count(*) as error_request from log where status != '200 OK' group by date ) as daily_error on daily_log.date = daily_error.date; ```
