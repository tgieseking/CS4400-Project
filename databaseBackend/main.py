import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash

@app.route('/visitor', methods=['POST'])
def add_visitor():
	try:
		_json = request.get_json()
		_username = _json['username']
		_email = _json['email']
		_password = _json['pwd']
		# validate the received values
		if _username and _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO USER VALUES(%s, %s, %s);"
			sql2 = "INSERT INTO VISITOR VALUES(%s);"
			data = (_username, _email, _hashed_password,)
			data2 =(_username,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			cursor.execute(sql2,data2)
			conn.commit()
			resp = jsonify('Success')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
		return str(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/visits_show', methods=['POST'])
def add_show():
	try:
		_json = request.get_json()
		_username = _json['username']
		_showname = _json['showname']
		_date = _json['date']
		# validate the received values
		if _username and _showname and _date and request.method == 'POST':
			# save edits
			sql = "INSERT INTO VISITS_SHOW VALUES(%s, %s, %s);"
			sql2 = "INSERT INTO VISITOR VALUES(%s);"
			data = (_username, _showname, _date,)
			data2 =(_username,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			cursor.execute(sql2,data2)
			conn.commit()
			resp = jsonify('Success')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
		return str(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/staff', methods=['POST'])
def add_staff():
	try:
		_json = request.get_json()
		_username = _json['username']
		_email = _json['email']
		_password = _json['pwd']
		# validate the received values
		if _username and _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO USER VALUES(%s, %s, %s);"
			sql2 = "INSERT INTO STAFF VALUES(%s);"
			data = (_username, _email, _hashed_password,)
			data2 =(_username,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			cursor.execute(sql2,data2)
			conn.commit()
			resp = jsonify('Success')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
		return str(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/visitor', methods=['GET'])
def get_visitors():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM VISITOR")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
		return str(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/visits_exhibit', methods=['POST'])
def add_visit():
	try:
		_json = request.json
		_username = _json['username']
		_exhibitname = _json['exhibit_name']
		_dateandtime = _json['date_and_time']
		# validate the received values
		if _username and _exhibitname and _dateandtime and request.method == 'POST':
			#do not save password as a plain text
			# save edits
			sql = "	INSERT INTO VISITS_EXHIBIT VALUES(%s,%s,%s);"
			data = (_username, _exhibitname, _dateandtime,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Success')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/visits_exhibit', methods=['GET'])
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM VISITS_EXHIBIT")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
### Add secret key for tokanizable login


@app.route('/exhibit', methods=['SEARCH'])
def search_exhibit():
	try:
		_json = request.json
		_exhibitname = _json['name']
		# validate the received values
		if _exhibitname and request.method == 'SEARCH':
			#do not save password as a plain text
			# save edits
			sql = "	SELECT Name, Size, (SELECT COUNT(ANIMAL.Name) as NumAnimals FROM ANIMAL GROUP BY ANIMAL.Exhibit), Water_Feature FROM Exhibit INNER JOIN Animal ON EXHIBIT.Name = ANIMAL.Exhibit WHERE Name = %s;"
			data = (_exhibitname,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Success')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()



if __name__ == "__main__":
    app.run()
