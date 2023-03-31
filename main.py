import KeyManagment
import EncryptFile
import DecryptFile


##Have to intialize the key managment system
if __name__ == "__main__":
    keyManager = KeyManagment.KeyManager()
    main = True
    i = 0
    print("Welcome to Secure File Storage")
    while(main):
        print("Press \n 1 to add a Group \n 2 to remove a Group \n 3 to encrypt a file \n 4 to decrypt a file \n 5 to exit")    
        i = int(input())
        if i < 1 | i > 5:
            print("Invalid Input")
        else:       
            if i == 1:
                print("Enter the name of the group")
                group = input()
                print("Enter the password")
                password = input()
                keyManager.add_key(group, password)
            elif i == 2:
                print("Enter the name of the group")
                group = input()
                print("Enter the password")
                password = input()
                print("Are you sure you want to delete this group? (y/n)")
                answer = input()
                if answer == "y":
                    keyManager.remove_key(group, password)
                else:
                    print("Group not deleted")
            elif i == 3:
                print("Enter the name of the group")
                group = input()
                print("Enter the password")
                password = input()
                print("Enter the name of the file")
                filename = input()
                key = keyManager.get_key(group, password)
                print(key)
                if(key == None):
                    print("Invalid Password")
                else:
                    EncryptFile.encrypt(filename, key)
            elif i == 4:
                print("Enter the name of the group")
                group = input()
                print("Enter the password")
                password = input()
                print("Enter the name of the file")
                filename = input()
                DecryptFile.decrypt(filename, keyManager.get_key(group, password))
            else:
                print("Goodbye")
                exit()