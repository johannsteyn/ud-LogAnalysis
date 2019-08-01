# ud-LogAnalysis
Full Stack web developer project
So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

How to run the data:
1. Install virtual box and open shell you want to run the project in.
2. Ensure the vagrant files are located in the shared file location between your host computer and the virtaul one.
3. Download the sql files from Udacity and move those to the shared file location as well.
4. Open your shell and cd into the location of the vagrant file
5.Run Vagrant up
6.log into VM via vagrant ssh
7. log into DB via psql -d news -f newsdata.sql (for later logins use psql -d news)
-Use \dt to see all the tables
-Use \d tablename to see a specific table
Use this create view to answer question 2.
- CREATE VIEW views AS 
SELECT authors, title
FROM authors JOIN articles
ON articles.authors=autors.id
8. run logsanalysis.py 

To exit the sql command line use \q or CNTRL z.
