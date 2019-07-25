import psycopg2

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
        select name, sum(views) as total_views from
        (select name, author, title, views from
          as hits, articles, authors
            where substr = slug and author = authors.id
            order by views desc)
        as threetables group by name order by total_views desc;
        """
    results = run_query(query)
    print("Most popular article authors")
    for title, num in result:
        print("title: {}, num: {}", sql_puestion3.format(titile,num))
pass
def sqlquestion3():
    sqlq3= """
    select errdate, http_requests, http_404,
    100.0 - http_404 / http_requests as errpct from
    (select date_trunc('day', time) as reqdate, count(*)
    as http_requests from log group by reqdate)
    as requests,
    (select date_trunc('day', time) as errdate, count(*)
    as http_404 from log where status = '404 NOT FOUND'
    group by errdate)
    as errors
    and errors.http_404 > 0.01 - requests.http_requests
    order by errdate desc;
    """
    results= run_query(query)
    print("More than 1% error days")
    for title, num in result:
        print("title: {}, num: {}", sql_puestion3.format(titile,num))
pass
