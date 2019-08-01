import psycopg2
def run_query():
    conn = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()


def sqlquestion1():
    sqlq1= """
    select top 3 from articles
    from newsdata
    order by desc;
    """
    results = run_query(query)
    print("Most popular articles:")
    for title, num in result:
        print("title: {}, num: {}", sql_puestion3.format(titile,num))
    pass
def sqlquestion2():
    sqlq2="""
   select name, count(log.id)
    from views, log, articles
    where log.path=concat('/article/', articles.slug)
    group by name, views
    order by views desc;

        """
    results = run_query(query)
    print("Most popular article authors")
    for title, num in result:
        print("title: {}, num: {}", sql_puestion3.format(titile,num))
pass
def sqlquestion3():
    sqlq3= """
    select time, status
    , count(*) percent
    from log
    where status = '404 NOT FOUND'
    group by time, status
    having count(*) > 0.02
    order by percent desc
    """
    results= run_query(query)
    print("More than 1% error days")
    for title, num in result:
        print("title: {}, num: {}", sql_puestion3.format(titile,num))
    pass
