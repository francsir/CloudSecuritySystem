import sqlite3

class GroupDataBase:
    def __init__(self):
        self.conn = sqlite3.connect('groups.db')
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('''CREATE TABLE groups (groups TEXT PRIMARY KEY, password TEXT, pubKey TEXT, privKey TEXT, id INTEGER NOT NULL)''')
        except:
            pass

        try:
            self.cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, group_id TEXT NOT NULL, FOREIGN KEY (group_id) REFERENCES groups(groups))''')
        except:
            pass

    def getUserGroup(self, user):
        self.cursor.execute('''SELECT group_id FROM users WHERE name = ?''', (user,))
        return self.cursor.fetchone()[0]

    def getID(self, group):
        self.cursor.execute('''SELECT id FROM groups WHERE groups = ?''', (group,))
        return self.cursor.fetchone()[0]
    
    def getKey(self, group, password):

        self.cursor.execute('''SELECT pubKey, privKey FROM groups WHERE groups = ? AND password = ?''', (group, password))
        return self.cursor.fetchone()
    
    def getPassword(self, group):
        self.cursor.execute('''SELECT password FROM groups WHERE groups = ?''', (group,))
        return self.cursor.fetchone()[0]
    
    def getGroup(self, name):
        self.cursor.execute('''SELECT groups FROM groups WHERE groups = ?''', (name,))
        return self.cursor.fetchone()[0]
    
    def getIndex(self, password):
        self.cursor.execute('''SELECT rowid FROM groups WHERE password = ?''', (password,))
        return self.cursor.fetchone()[0]
    

    def insertGroup(self, group, password, priv, pub, id):
        self.cursor.execute('''INSERT INTO groups VALUES (?, ?, ?, ?, ?)''', (group, password, priv, pub, id))
        self.conn.commit()

    def insertUser(self, name, group):
        self.cursor.execute('''INSERT INTO users VALUES (NULL, ?, ?)''', (name, group))
        self.conn.commit()
    
    def deleteGroup(self, group):
        self.cursor.execute('''DELETE FROM groups WHERE groups = ?''', (group,))
        self.conn.commit()

    def deleteUser(self, name):
        self.cursor.execute('''DELETE FROM users WHERE name = ?''', (name,))
        self.conn.commit()

    def getLength(self):
        self.cursor.execute('''SELECT COUNT(*) FROM groups''')
        return self.cursor.fetchone()[0]