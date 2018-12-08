# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中  处理database 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase , QSqlQuery
# import 注册登录界面
def createDB(Name,Password):
	db = QSqlDatabase.addDatabase('QSQLITE')
	db.setDatabaseName('./db/database.db')
    
	if not db.open():
		QMessageBox.critical(None,  ("无法打开数据库"),
		( "无法建立到数据库的连接,这个例子需要SQLite 支持，请检查数据库配置。\n\n"
          "点击取消按钮退出应用。"),
			QMessageBox.Cancel )
		return False
	
	query = QSqlQuery()
	query.exec_("create table people(id int primary key, name varchar(20), address varchar(30))")
	query.exec_("insert into people values(%s, %s)",[Name,Password])
	db.close()
	return True

if __name__ == '__main__':
	app =  QApplication(sys.argv)
	# createDB() 
	s = createDB('name','Password') 
	print(s)
	sys.exit(app.exec_())

	
