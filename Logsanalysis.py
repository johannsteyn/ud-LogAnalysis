#!/usr/bin/env python2
import psycopg2

def run_query():
    conn = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()

sqlq1= """
    select top 3 from articles
    from newsdata
    order by desc;
   """           
sqlq2="""
   select name, count(log.id)
    from views, log, articles
    where log.path=concat('/article/', articles.slug)
    group by name, views
    order by views desc;
  """
sqlq3= """
    select time, status
    , count(*) percent
    from log
    where status = '404 NOT FOUND'
    group by time, status
    having count(*) > 0.02
    order by percent desc
    """
def sqlquestion1():
    results = run_query(query)
    print("Most popular articles:")
    for i in result:
        print(str(i[0] + '---' +` str(i[1]) + 'views')
    print(" ")

def sqlquestion2():
    results = run_query(query)
    print("Most popular article authors")
    for i in result:
        print(str(i[0] + '---' +` str(i[1]) + 'views')
    print(" ")

pass
def sqlquestion3():
    results= run_query(query)
    print("More than 1% error days")
    for i in result:
        print(str(i[0] + '---' +` str(i[1]) + 'views')
    print(" ")
