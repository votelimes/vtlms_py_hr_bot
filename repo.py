import psycopg2

class RpConnection:
    
    host = 'localhost'
    database = 'db_hr'
    user = 'db_hr_mg'
    password = '496hjoijef246'

    def __init__(self):
        pass

    def createConnection():
        _connection = psycpopg2.connect(
            host = host
            database = database
            user = user
            password = password
        )

    def getEmployee(self, phone):
        try:
            createConnection()
            cursor = _connection.cursor()
            query = "SELECT * FROM employees WHERE phone = %s;"
            cursor.execute(query, (phone,))
            rows = cursor.fetchall()
            if len(rows) > 0:
                return rows[0]
         except Exception as e:
            print(f'Ошибка: {e}')
        finally:
            if cursor:
                cursor.close()
            if _connection
                _connection.close()   

