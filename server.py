Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/njf.p.py", line 7, in <module>
    database="mydatabase"
  File "C:\Python34\lib\site-packages\mysql\connector\__init__.py", line 179, in connect
    return MySQLConnection(*args, **kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 95, in __init__
    self.connect(**kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\abstracts.py", line 719, in connect
    self._open_connection()
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 210, in _open_connection
    self._ssl)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 144, in _do_auth
    self._auth_switch_request(username, password)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 177, in _auth_switch_request
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1045 (28000): Access denied for user 'yourusername'@'localhost' (using password: YES)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/njf.p.py", line 7, in <module>
    database="mydata"
  File "C:\Python34\lib\site-packages\mysql\connector\__init__.py", line 179, in connect
    return MySQLConnection(*args, **kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 95, in __init__
    self.connect(**kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\abstracts.py", line 719, in connect
    self._open_connection()
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 210, in _open_connection
    self._ssl)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 144, in _do_auth
    self._auth_switch_request(username, password)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 177, in _auth_switch_request
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1045 (28000): Access denied for user 'youruser'@'localhost' (using password: YES)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/njf.p.py", line 7, in <module>
    database="mydatabase"
  File "C:\Python34\lib\site-packages\mysql\connector\__init__.py", line 179, in connect
    return MySQLConnection(*args, **kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 95, in __init__
    self.connect(**kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\abstracts.py", line 719, in connect
    self._open_connection()
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 210, in _open_connection
    self._ssl)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 144, in _do_auth
    self._auth_switch_request(username, password)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 177, in _auth_switch_request
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1045 (28000): Access denied for user 'yourusername'@'localhost' (using password: YES)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/njf.p.py", line 7, in <module>
    database="mydatabase"
  File "C:\Python34\lib\site-packages\mysql\connector\__init__.py", line 179, in connect
    return MySQLConnection(*args, **kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 95, in __init__
    self.connect(**kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\abstracts.py", line 719, in connect
    self._open_connection()
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 210, in _open_connection
    self._ssl)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 144, in _do_auth
    self._auth_switch_request(username, password)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 177, in _auth_switch_request
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1049 (42000): Unknown database 'mydatabase'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/njf.p.py", line 7, in <module>
    database="mydatabase"
  File "C:\Python34\lib\site-packages\mysql\connector\__init__.py", line 179, in connect
    return MySQLConnection(*args, **kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 95, in __init__
    self.connect(**kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\abstracts.py", line 719, in connect
    self._open_connection()
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 210, in _open_connection
    self._ssl)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 144, in _do_auth
    self._auth_switch_request(username, password)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 177, in _auth_switch_request
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1049 (42000): Unknown database 'mydatabase'
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/njf.p.py", line 5, in <module>
    cursor.execute(sql)
  File "C:\Python34\lib\site-packages\mysql\connector\cursor.py", line 515, in execute
    self._handle_result(self._connection.cmd_query(stmt))
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 488, in cmd_query
    result = self._handle_result(self._send_cmd(ServerCmd.QUERY, query))
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 395, in _handle_result
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1050 (42S01): Table 'student' already exists
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/njf.p.py", line 2, in <module>
    conn = mysql.connector.connect(user="root",password="mkaif347",host="127.0.0.1",database="fy1")
  File "C:\Python34\lib\site-packages\mysql\connector\__init__.py", line 179, in connect
    return MySQLConnection(*args, **kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 95, in __init__
    self.connect(**kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\abstracts.py", line 719, in connect
    self._open_connection()
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 210, in _open_connection
    self._ssl)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 144, in _do_auth
    self._auth_switch_request(username, password)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 177, in _auth_switch_request
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1049 (42000): Unknown database 'fy1'
>>> ================================ RESTART ================================
>>> 
Connection Sucessful
List Of Data Base
[('information_schema',), ('db2',), ('db3',), ('fy2',), ('mysql',), ('test',)]
>>> ================================ RESTART ================================
>>> 
Table Created Sucessfully
>>> ================================ RESTART ================================
>>> 
Data Inserted Sucessfully
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/njf.p.py", line 2, in <module>
    conn= mysql.connector.connect(user="root",password="sachin",host="127.0.0.1",database="fy2")
  File "C:\Python34\lib\site-packages\mysql\connector\__init__.py", line 179, in connect
    return MySQLConnection(*args, **kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 95, in __init__
    self.connect(**kwargs)
  File "C:\Python34\lib\site-packages\mysql\connector\abstracts.py", line 719, in connect
    self._open_connection()
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 210, in _open_connection
    self._ssl)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 144, in _do_auth
    self._auth_switch_request(username, password)
  File "C:\Python34\lib\site-packages\mysql\connector\connection.py", line 177, in _auth_switch_request
    raise errors.get_exception(packet)
mysql.connector.errors.ProgrammingError: 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
>>> ================================ RESTART ================================
>>> 
Data insert Sucessfully
>>> ================================ RESTART ================================
>>> 
Updated Sucessfully
[('kaif', 76, 'BSC-CS', '1st', 'Pass'), ('Krishna', 19, 'BSC-CS', 'F_year', 'Pass'), ('Ramya', 25, 'BSC-CHEM', 'S_year', 'Pass'), ('Ram', 42, 'Bsc-cs', 'S_year', 'Fail')]
>>> ================================ RESTART ================================
>>> 
Updated Sucessfully
[('kaif', 76, 'BSC-CS', '1st', 'Pass'), ('Krishna', 19, 'BSC-CS', 'F_year', 'Pass'), ('Ramya', 25, 'BSC-CHEM', 'S_year', 'Pass'), ('Ram', 42, 'Bsc-cs', 'S_year', 'Fail')]
>>> ================================ RESTART ================================
>>> 
Updated Sucessfully
[('kaif', 76, 'BSC-CS', '1st', 'Pass'), ('Krishna', 19, 'BSC-CS', 'F_year', 'Pass'), ('Ramya', 25, 'BSC-CHEM', 'S_year', 'Pass'), ('Ram', 32, 'Bsc-cs', 'S_year', 'Fail')]
>>> ================================ RESTART ================================
>>> 
Updated Sucessfully
[('kaif', 76, 'BSC-CS', '1st', 'Pass'), ('Krishna', 19, 'BSC-CS', 'F_year', 'Pass'), ('Ramya', 25, 'BSC-CHEM', 'S_year', 'Pass'), ('Ram', 32, 'Bsc-cs', 'S_year', 'Fail')]
>>> ================================ RESTART ================================
>>> 
Content of Table:
[('kaif', 76, 'BSC-CS', '1st', 'Pass'), ('Krishna', 19, 'BSC-CS', 'F_year', 'Pass'), ('Ramya', 25, 'BSC-CHEM', 'S_year', 'Pass'), ('Ram', 32, 'Bsc-cs', 'S_year', 'Fail')]
>>> ================================ RESTART ================================
>>> 
Content of Table:
[('kaif', 76, 'BSC-CS', '1st', 'Pass'), ('Krishna', 19, 'BSC-CS', 'F_year', 'Pass'), ('Ramya', 25, 'BSC-CHEM', 'S_year', 'Pass')]
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
Data insert Sucessfully
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/njf.p.py", line 17, in <module>
    if _name_ == "_ main _":
NameError: name '_name_' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Python34/njf.p.py", line 17, in <module>
    if _name_ == "_ main _":
NameError: name '_name_' is not defined
>>> ================================ RESTART ================================
>>> 
Has connected the client
>>> 
