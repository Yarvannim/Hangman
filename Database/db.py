from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, inspect, select,insert
from sqlalchemy.orm import Session
import bcrypt
# from sqlalchemy.ext.declarative import declarative_base
_engine = create_engine("mariadb+mariadbconnector://root@127.0.0.1:3306/my_db")
_meta = MetaData()

# if(inspect(_engine).has_table("users") == False):
users = Table(
'users', _meta, 
Column('id', Integer, primary_key = True, nullable=False, autoincrement=True), 
Column('username', String(45), nullable=False, unique=True), 
Column('password', String(128), nullable=False), 
)
_meta.create_all(_engine)

# stmt = users.select()
# _conn = _engine.connect()
# _result = _conn.execute(stmt)
# print(_result)
# for row in _result:
#     print(row[1])
# _conn.close()

def register(_username, _password):
    _stmt = select(users).where(users.c.username == _username)
    _conn = _engine.connect()
    _result = _conn.execute(_stmt)
    if(_result.rowcount == 1):
        _error = 'Your username has already been taken'
        return False,_error
    else:
        _hashedPassword = bcrypt.hashpw(_password.encode('utf8'), bcrypt.gensalt())
        _stmt = insert(users).values(username = _username, password = _hashedPassword)
        _conn = _engine.connect()
        _conn.execute(_stmt)
        _conn.commit()
        _conn.close()
    

def login(_username, _password):
    _stmt = select(users).where(users.c.username == _username)
    _conn = _engine.connect()
    _result = _conn.execute(_stmt)
    if(_result.rowcount == 1):
        for row in _result:
            _pwInDb = row[2]
        if bcrypt.checkpw(_password.encode('utf8'), _pwInDb.encode('utf8')):
            _loginStatus = True
            _conn.close()
            return _loginStatus, _username
        else:
            _loginStatus = False
            _conn.close()
            return _loginStatus, _username
    else:
        _loginStatus = False
        _conn.close()
        return _loginStatus, _username


login('Kevin', 'password123')