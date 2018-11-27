from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'cs4400_group47'
app.config['MYSQL_DATABASE_PASSWORD'] = 'CgTvf9t1'
app.config['MYSQL_DATABASE_DB'] = 'cs4400_group47'
app.config['MYSQL_DATABASE_HOST'] = 'academic-mysql.cc.gatech.edu'
mysql.init_app(app)
