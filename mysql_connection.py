import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
            host = 'yh.cpos3ccatavx.ap-northeast-2.rds.amazonaws.com',
            database = 'Uzoo',
            user = 'admin',
            password = 'gkswogns12')
    
    return connection