import GenerateKey
import os

class KeyManager:
    def __init__(self):
        self.groups = []    
        
    def add_key(self, group, password,db):
        if group not in self.groups:
            self.groups.append(group)
            i = db.getLength()
            keys = GenerateKey.generateKeys(i)
            db.insertGroup(group, password, keys[0], keys[1], i)
        else:
            print("Group Key Pair Already Exists")

    def remove_key(self, group, password, db):
        if group in self.groups:
            passwordX = db.getPassword(group)
            i = db.getID(group) 
            if passwordX == password:
                self.groups.remove(group)
                self.deleteKey(i)
                db.deleteGroup(group)
            else:
                print("incorrect password")
        else:
            print("group does not exist")
            

    def get_key(self, group, password, db):
        group = db.getGroup(group)
        if group != None:
            p = db.getPassword(group)
            if p == password:
                return db.getKey(group, password)
        else:
            print("Wrong Password")
            return None
        
    def deleteKey(self, i):
        priv = "./privateKeys/private_key.pem" + str(i)
        pub = "./publicKeys/public_key.pem" + str(i)
        if os.path.exists(priv):
            os.remove(priv)
        else:
            print(priv + "The file does not exist")
        if os.path.exists(pub):
            os.remove(pub)
        else:
            print(pub +"The file does not exist")
    
    def verifyGroup(self, group, password, db):
        p = db.getPassword(group)
        if p == password:
            return True
        else:
            return False
        
    def verifyUser(self, user, password, db):
        group  = db.getUserGroup(user)
        p = db.getPassword(group)

        if p == password:
            return True, group
        else:
            return False, None
        
