# import sqlite3
# connect = sqlite3.connect("Petshop.db")
# cursor = connect.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS Users (Id INTEGER PRIMARY KEY AUTOINCREMENT,Name varchar(30),Surname varchar(30),Email varchar(200),Username varchar(30),Password varchar(6),IsAdmin bit)")
# connect.close()
# #
# import sqlite3
# connect = sqlite3.connect("Petshop.db")
# cursor = connect.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS Mails (Id INTEGER PRIMARY KEY AUTOINCREMENT,Name varchar(30),Phone varchar(30),Email varchar(200),Message varchar(300))")
# connect.close()

# import sqlite3
# connect = sqlite3.connect("Petshop.db")
# cursor = connect.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS About (Id INTEGER PRIMARY KEY AUTOINCREMENT,Text varchar(30))")
# connect.close()



from User import User

class Database:
    @staticmethod
    def Login(username, password):
        import sqlite3
        connect = sqlite3.connect("Petshop.db")
        cursor = connect.cursor()
        query = "SELECT * FROM Users WHERE Username=? AND Password=?"
        cursor.execute(query, (username, password))
        return cursor.fetchone()

    @staticmethod
    def Register(user):
        import sqlite3
        connect = sqlite3.connect("Petshop.db")
        cursor = connect.cursor()
        query=  "INSERT INTO Users (Name,Surname,Email,Username,Password,IsAdmin) values (?,?,?,?,?,?)"
        cursor.execute(query,(user.Name,user.Surname,user.Email,user.Username,user.Password,user.IsAdmin))
        connect.commit()
        return 1

    def UniqueUsername(username):
        import sqlite3
        connect = sqlite3.connect("Petshop.db")
        cursor = connect.cursor()
        query = "SELECT * FROM Users WHERE Username=?"
        cursor.execute(query, (username,))
        # fetchall() ile dönen sonuçların uzunluğunu kontrol edelim
        if len(cursor.fetchall()) != 0:
            connect.close()  # Veritabanı bağlantısını kapat
            return True  # Kullanıcı adı mevcut
        else:
            connect.close()  # Veritabanı bağlantısını kapat
            return False  # Kullanıcı adı benzersiz

    def UniqueEmail(email):
        import sqlite3
        connect = sqlite3.connect("Petshop.db")
        cursor = connect.cursor()
        query = "SELECT * FROM Users WHERE Email=?"
        cursor.execute(query, (email,))
        # fetchall() ile dönen sonuçların uzunluğunu kontrol edelim
        if len(cursor.fetchall()) != 0:
            connect.close()  # Veritabanı bağlantısını kapat
            return True  # Kullanıcı adı mevcut
        else:
            connect.close()  # Veritabanı bağlantısını kapat
            return False  # Kullanıcı adı benzersiz

    @classmethod
    def EmailSave(cls,name,email,phone,message):
        import sqlite3
        connect = sqlite3.connect("Petshop.db")
        cursor = connect.cursor()
        query = "INSERT INTO Mails (Name,Phone,Email,Message) values (?,?,?,?)"
        cursor.execute(query, (name, phone, email, message))
        connect.commit()
        connect.close()

    @classmethod
    def GetMails(cls):
        import sqlite3
        connect = sqlite3.connect("Petshop.db")
        cursor = connect.cursor()
        query="Select * from Mails"
        cursor.execute(query)
        return cursor.fetchall()

    @classmethod
    def GetAbout(cls):
        import sqlite3
        connect = sqlite3.connect("Petshop.db")
        cursor = connect.cursor()
        query = "Select * from About where Id=1"
        cursor.execute(query)
        return cursor.fetchone()

    @classmethod
    def UpdateAbout(cls,text):
        import sqlite3
        connect = sqlite3.connect("Petshop.db")
        cursor = connect.cursor()
        query="Update About set Text=? where Id=1"
        cursor.execute(query,(text,))
        connect.commit()
        return Database.GetAbout()