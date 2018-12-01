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
def add_show_visit():
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
		_json = request.get_json()
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
		return str(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/note',methods=['POST'])
def add_note():
	try:
		_json = request.get_json()
		_animalname = _json['animal_name']
		_animalspecies = _json['animal_species']
		_username = _json['username']
		_time = _json['time']
		_text = _json['text']
		if _animalname and _animalspecies and _username and _time and _text and request.method == 'POST':
			sql = "INSERT INTO NOTE VALUES(%s, %s, %s, %s,%s);"
			data = (_animalname,_animalspecies,_username,_time,_text,)
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
		return str(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/animal',methods=['POST'])
def add_animal():
	try:
		_json = request.get_json()
		_animalname = _json['animal_name']
		_animalspecies = _json['animal_species']
		_animaltype = _json['animal_type']
		_age = _json['animal_age']
		_exhibitname = _json['exhibit_name']
		if _animalname and _animalspecies and _animaltype and _age and _exhibitname and request.method == 'POST':
			sql = "INSERT INTO ANIMAL VALUES(%s, %s, %s, %s,%s);"
			data = (_animalname,_animalspecies,_animaltype,_age,_exhibitname,)
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
		return str(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/show',methods=['POST'])
def add_show():
	try:
		_json = request.get_json()
		_showname = _json['showname']
		_time = _json['date_and_time']
		_host = _json['host']
		_locatedat = _json['located_at']
		if _showname and _time and _host and _locatedat and request.method == 'POST':
			sql = "INSERT INTO SHOW VALUES(%s, %s, %s, %s);"
			data = (_showname,_time,_host,_locatedat,)
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
		return str(e)
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
		_json = request.get_json()
		_exhibitname = _json.get('exhibit_name')
		if _exhibitname == None:
			_exhibitname = '%'
		_water = _json.get('water_feature')
		if _water == None:
			_water == '%'
		_minsize = _json('minsize')
		if _minsize == None:
			_minsize = 0;
		_maxsize = _json.get('maxsize')
		if _maxsize == None:
			_maxsize = 4294967295
		_minanimals = _json.get('minanimals')
		if _minanimals ==None:
			_minanimals = 0
		_maxanimals = _json.get('maxanimals')
		# validate the received values
		if request.method == 'SEARCH':
			#do not save password as a plain text
			# save edits
			sql = "	SELECT Exhibit.Name, Size, (SELECT COUNT(ANIMAL.Name) as NumAnimals FROM ANIMAL GROUP BY ANIMAL.Exhibit), Water_Feature FROM EXHIBIT INNER JOIN ANIMAL ON EXHIBIT.Name = ANIMAL.Exhibit WHERE EXHIBIT.Name LIKE %s AND Water_Feature LIKE %s AND (Size BETWEEN %s AND %s) AND (NumAnimals BETWEEN %s AND %s);"
			data = (_exhibitname,_water,_minsize,_maxsize,_minanimals,_maxanimals)
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
