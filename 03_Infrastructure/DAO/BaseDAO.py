import os
import sys
sys.path.insert(
    0, 
    os.path.abspath('..') + "\\")

import config
import pymysql.cursors

class BaseDAO:

    @property
    def server(self):
        return self._server
    
    @server.setter
    def server(self, value):
        self._server = value

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, value):
        self._database = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, value):
        self._connection = value

    def __init__(self):
        self.server = config.mysqlServer
        self.database = config.mysqlDatabase
        self.user = config.mysqlUser
        self.password = config.mysqlPassword

    def Open(self):
        self.connection = pymysql.connect(
            host = self.server,
            password = self.password,
            user = self.user,
            db = self.database,
            charset = "utf8mb4",
            cursorclass = pymysql.cursors.DictCursor
        )

    def Close(self):
        if self.connection != None:
            self.connection.close()

    def Select(self, query, args):
        lines = None
        self.Open()
        with self.connection.cursor() as cursor:
            cursor.execute(query, args)
            lines = cursor.fetchall()
        self.Close()
        return lines

    def Execute(self, query, args):
        self.Open()
        with self.connection.cursor() as cursor:
            cursor.execute(query, args)
            self.connection.commit()
        self.Close()