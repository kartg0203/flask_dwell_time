import psycopg2
from psycopg2 import pool
import config

def connect_test():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        # conn = psycopg2.connect(database=config.DB_DATABASE, user=config.DB_USERNAME, password=config.DB_PASSWORD, host=config.DB_HOST, port=config.DB_PORT, options=f"-c search_path={config.DB_SCHEMA}")
        db_config = {
            'database': config.DB_DATABASE,
            'user': config.DB_USERNAME,
            'password': config.DB_PASSWORD,
            'host': config.DB_HOST,
            'port': config.DB_PORT,
            'options': f"-c search_path={config.DB_SCHEMA}"
        }
        connection_pool = pool.SimpleConnectionPool(1, 10, **db_config)
        conn = connection_pool.getconn()

        with conn.cursor() as cur:
    	# execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT * FROM eo_sales_location')

            # display the PostgreSQL database server version
            result = cur.fetchone()
            print(result)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            conn.closeall()
            print('Database connection closed.')

if __name__ == '__main__':
    connect_test()
