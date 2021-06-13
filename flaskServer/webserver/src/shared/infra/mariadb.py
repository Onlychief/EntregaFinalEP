import mariadb

config = {
    'host' : 'mariadbpython',
    'port' : 3306,
    'user' : 'root',
    'password' : '123456',
    'database' : 'control_asistencia',
}

DB = mariadb.connect(**config)
DB.autocommit = True