# import pymysql

# class Database:
#     def __init__(self):
#         self.mydb = pymysql.connect(
#             host="localhost",
#             user="root",
#             password="",
#             database="hotel_management",
#             port=3306  # default port for MySQL
#         )
#         self.cursor = self.mydb.cursor()

#     def execute_query(self, query, values=None):
#         self.cursor.execute(query, values)
#         self.mydb.commit()

#     def fetch_data(self, query, values=None):
#         self.cursor.execute(query, values)
#         return self.cursor.fetchall()
