import psycopg2

def three_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("Select title, count(*) as total from log, articles WHERE path = concat('/article/',articles.slug) GROUP BY articles.title ORDER BY total DESC LIMIT 3;")
    results = c.fetchall()
    db.close()
    for result in results:
        print('The article "{}" had {} views.'.format(result[0], result[1]))

def three_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("Select authors.name from authors, (Select articles.author, count(*) as total from log, articles WHERE path = concat('/article/',articles.slug) GROUP BY articles.author ORDER BY total DESC) as nameAuthors WHERE authors.id = nameAuthors.author;")
    results = c.fetchall()
    db.close()
    for result in results:
        print(result[0])

def get_errors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("CREATE VIEW dailyErrors AS SELECT daily_log.date, round(daily_error.error_request * 100.0 / daily_log.total_request, 2) AS error_log FROM ( select time::date AS date, count(*) AS total_request FROM log GROUP BY date ) AS daily_log join ( select time::date as date, count(*) as error_request from log where status != '200 OK' group by date ) as daily_error on daily_log.date = daily_error.date;")
    c.execute("SELECT * FROM dailyErrors WHERE error_log > 1")
    results = c.fetchall()
    db.close()
    for i in results:
        print(str(i[0]) + ' - ' + str(i[1]) + ' %' + ' errors')


if __name__ == '__main__':
    print('[Analysis Report]')
    print('')
    three_articles()
    print('')
    three_authors()
    print('')
    get_errors()
