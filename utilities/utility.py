import mysql.connector
from bs4 import BeautifulSoup

class Util:

    def start_connection():
        try:
            connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='project2')
            my_cursor = connection.cursor()
            return (connection, my_cursor)
        except:
            print("\n---Some Error occured while setting up link to database---\n")

    def fetch_data(sql_command):
        connection, my_cursor = Util.start_connection()
        my_cursor.execute(sql_command)
        result = my_cursor.fetchall()
        connection.close()
        return result

    def write_data(sql_command):
        connection, my_cursor = Util.start_connection()
        my_cursor.execute(sql_command)
        connection.commit()
        connection.close()

    def find_id(id):
        sql_command=Util.get_sql_command("GET_USER_RECORDS").format(str(id))
        return Util.fetch_data(sql_command)

    def get_number_of_records(table_name):
        sql_command=Util.get_sql_command("GET_COUNT_OF_RECORDS").format(table_name)
        return Util.fetch_data(sql_command)

    def add_new_record(user_record):
        sql_command=Util.get_sql_command("ADD_USER").format(user_record[0],user_record[1],user_record[2],user_record[3],user_record[4],user_record[5],user_record[6],user_record[7],user_record[8],user_record[9])
        Util.write_data(sql_command)
        sql_command=Util.get_sql_command("ADD_ROLE").format(user_record[0],0)
        Util.write_data(sql_command)
        sql_command=Util.get_sql_command("ADD_APPROVAL").format(user_record[0],0)
        Util.write_data(sql_command)
        return True

    def get_user_type(id):
        sql_command=Util.get_sql_command("GET_ROLE").format(id)
        return Util.fetch_data(sql_command)

    def check_is_user_approved(id):
        sql_command = Util.get_sql_command("GET_APPROVAL").format(id) 
        return Util.fetch_data(sql_command)
    
    def get_sql_command(command):
        with open('Voting-System//configuration//queries.xml', 'r') as f:
            data = f.read()
        Bs_data = BeautifulSoup(data, "xml")
        full_sql_command = Bs_data.select(command)
        return full_sql_command[0].get_text()