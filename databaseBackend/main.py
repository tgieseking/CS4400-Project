import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash

@app.route('/visitor', methods=['POST'])
def add_visitor():
	try:
		_json = request.json
		_username = _json['name']
		_email = _json['email']
		_password = _json['pwd']
		# validate the received values
		if _name and _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO User VALUES(%s, %s, %s, UserType=“Visitor”);"
			sql2 = "INSERT INTO Visitor VALUES(%s);"
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
	finally:
		cursor.close() 
		conn.close()
