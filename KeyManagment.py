import GenerateKey
import os

##currently, if we remove a key, and then add another one, the index will overlap
class KeyManager:
    def __init__(self):
        self.keys = []
        self.groups = []
        self.passwords = []
        
    
    def add_key(self, group, password):
        if group not in self.groups:
            self.groups.append(group)
            self.passwords.append(password)
            i = self.groups.index(group)
            keys = GenerateKey.generateKeys(i)
            self.keys.append(keys)
        else:
            print("Group Key Pair Already Exists")

    def remove_key(self, group, password):
        if group in self.groups:
            i = self.groups.index(group)
            if self.passwords[i] == password:
                self.groups.pop(i)
                self.passwords.pop(i)
                self.keys.pop(i)
                self.deleteKey(i)
            else:
                print("incorrect password")
        else:
            print("key does not exist")
            

    def get_key(self, group, password):
        if group in self.groups:
            I = self.groups.index(group)
            if self.passwords[I] == password:
                return self.keys[I]
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
        
