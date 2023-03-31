import GenerateKey

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

    def remove_key(self, group, key, password):
        if group in self.groups:
            i = self.groups.index(group)
            if self.passwords[i] == password:
                self.groups.pop(i)
                self.passwords.pop(i)
                self.keys.pop(i)
            else:
                print("incorrect password")
        else:
            print("key does not exist")
            

    def get_key(self, group, password):
        if group in self.keys:
            I = self.groups.index(group)
            if self.passwords[I] == password:
                return self.keys[group][1]
        else:
            print("Wrong Password")
            return None