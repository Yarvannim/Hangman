from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select,insert
import bcrypt

# create engine to connect to db
_engine = create_engine("mariadb+mariadbconnector://root@127.0.0.1:3306/my_db")
_meta = MetaData()

#create table with sqlalchemy
users = Table(
'users', _meta, 
Column('id', Integer, primary_key = True, nullable=False, autoincrement=True), 
Column('username', String(45), nullable=False, unique=True), 
Column('password', String(128), nullable=False), 
)
_meta.create_all(_engine)

# register function that creates a new user and hashes their password with bcrypt as long as the username isnt taken yet
def register(_username, _password):
    _stmt = select(users).where(users.c.username == _username)
    _conn = _engine.connect()
    _result = _conn.execute(_stmt)
    if(_result.rowcount == 1):
        return False
    else:
        _hashedPassword = bcrypt.hashpw(_password.encode('utf8'), bcrypt.gensalt())
        _stmt = insert(users).values(username = _username, password = _hashedPassword)
        _conn = _engine.connect()
        _conn.execute(_stmt)
        _conn.commit()
        _conn.close()
        return True
    
# login function that looks for the username, and checks the hashed password if it has found a user since password is hashed i cant use the variable in select statement
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