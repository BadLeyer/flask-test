# -*- coding: utf-8 -*-
import sqlite3

class SignDAO:

    def __init__(self):
        dbName = 'testdb.sqlite'

    def insertName(self,id,pw):
        #conn = mysql.connector.connect(host=self.host,user=self.user,password=self.pw,database=self.database)
        conn = sqlite3.connect(self.dbName)
        cur = conn.cursor()
        try:
            data =[(id,pw)]
            cur.execute("INSERT INTO signs VALUES (?,?)",data)
            conn.commit()
        except:
            conn.rollback()
            print('失敗')
        finally:
            conn.close()

    def selectName(self,name):
        conn = sqlite3.connect(self.dbName)
        cur = conn.cursor()
        result = ""
        try :
            data = [(name)]
            result = execute("select * from signs where id = ?",data)
            conn.commit()
        except :
            conn.rollback()
            print('失敗')
        finally :
            conn.close()
        return result


def main():
    db = SignDAO()
    db.insertName('sasebo','nagasaki')
    print('登録完了')
    rows = db.selectName('sasebo')
    for r in rows:
        print(r)

if __name__ == '__main__':
    main()