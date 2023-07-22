from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Text
from sqlalchemy.orm import mapper, sessionmaker
import datetime
class ServerStorage:
    '''
        Class - application for working with the server database.
        Uses SQLite database, works with
        SQLAlchemy ORM takes a classic approach.
        '''
    class AllUsers:
        '''Class - display table of all users.'''

        def __init__(self,username,passwd_hash):
            self.name=username
            self.last_login=datetime.datetime.now()
            self.passwd_hash=passwd_hash
            self.pubkey=None
            self.id=None
    class ActiveUsers:
        '''Class - display table of active users.'''
        def __init__(self,user_id,ip_address,port,login_time):
            self.user=user_id
            self.ip_address=ip_address
            self.port=port
            self.login_time=login_time
            self.id=None
    class LoginHistory:
        '''Class - displaying the login history table.'''
        def __init__(self,name,date,ip,port):
            self.id=None
            self.name=name
            self.date_time=date
            self.ip=ip
            self.port=port
    class UsersContacts:
        '''Class - display the table of user contacts.'''

        def __init__(self, user, contact):
            self.id = None
            self.user = user
            self.contact = contact

