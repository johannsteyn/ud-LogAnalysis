# ud-LogAnalysis
Full Stack web developer project
So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors

How to run the data:
1. Install and configure Linux VM through Virtual Box.
2. Install Vagrant files.
3. Install SQL database files.
4. cd into the VM file and then cd into the Vagrant file.
5.Run Vagrant up
6.log into VM via vagrant ssh
7. log into DB via psql -d news -f newsdata.sql (for later logins use psql -d news)
Use this create view to answer question 2.
- CREATE VIEW views AS 
SELECT authors, title
FROM authors JOIN articles
ON articles.authors=autors.id
8. run logsanalysis.py 
9.\q to exit db
