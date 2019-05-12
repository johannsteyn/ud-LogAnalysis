import psycopg2


def main():
   
    conn = psycopg2.connect("dbname=news")


    cur = conn.cursor()


    sql_popular_articles = """
      SELECT article_view.title, article_view.view
      FROM article_view
      ORDER BY article_view.view DESC
      LIMIT 3;
    """
    cur.execute(sql_popular_articles)
    print("Most popular articles:")
    for (title, view) in cur.fetchall():
        print("    {} - {} views".format(title, view))
    print("-" * 70)

    sql_popular_authors = """
    SELECT article_view.name, SUM(article_view.view) AS author_view
    FROM article_view
    GROUP BY article_view.name
    ORDER BY author_view DESC;
    """
    cur.execute(sql_popular_authors)
    print("Most popular authors:")
    for (name, view) in cur.fetchall():
        print("    {} - {} views".format(name, view))
    print("-" * 70)

    sql_more_than_one_percent_errors = """
    SELECT *
    FROM error_rate
    WHERE error_rate.percentage > 1
    ORDER BY error_rate.percentage DESC;
    """
    cur.execute(sql_more_than_one_percent_errors)
    print("Days with more than 1% errors:")
    for (date, percentage) in cur.fetchall():
        print("    {} - {}% errors".format(date, percentage))
    print("-" * 70)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
