import psycopg2
from webapp.services.utils import getSqlScript


def recreateDatabase():
    conn = psycopg2.connect(user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""SELECT pg_terminate_backend(pg_stat_activity.pid)
                    FROM pg_stat_activity
                    WHERE pg_stat_activity.datname = 'Locadora';
                """)
    
    cur.execute('DROP DATABASE IF EXISTS "Locadora";')
    cur.execute('CREATE DATABASE "Locadora";')
    cur.close()
    conn.close()

    conn = psycopg2.connect(database="Locadora", user="postgres", password="B4T@TaC0mF31JãO", host="postgres")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(getSqlScript('recreate/createTables'))

    cur.close()
    conn.close()

    return "ok"

