import pymysql
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'Lcj.456baronesa'
DB_NAME = 'restaurantes'
def connect_db():
    return pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)

