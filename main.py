import KeyManagment
import EncryptFile
import DecryptFile
import groupDataBase



def editGroup():
    print("Enter the name of the group you want to edit")
    group = input()
    print("Enter the password")
    password = input()

    if  not keyManager.verifyGroup(group, password, db):
        print("Invalid Password")
        return
    
    print("Press \n 1 to add a user \n 2 to remove a user \n 3 to delete the group")
    i = int(input())
    if i < 1 | i > 3:
        print("Invalid Input")
    else:
        ##Add a user
        if i == 1:
            print("Enter the name of the user")
            user = input()
            password = input()
            db.insertUser(user, group)
        ##Remove a user
        elif i == 2:
            print("Enter the name of the user")
            user = input()
            print("Are you sure you want to delete this user? (y/n)")
            answer = input()
            if answer == "y":
                db.deleteUser(user)
            else:
                print("User not deleted")
            db.deleteUser(user)
        elif i == 3:
            print("Are you sure you want to delete this group? (y/n)")
            answer = input()
            if answer == "y":
                keyManager.remove_key(group, password, db)
            else:
                print("Group not deleted")
            db.deleteGroup(group)

if __name__ == "__main__":
    keyManager = KeyManagment.KeyManager()
    db = groupDataBase.GroupDataBase()
    main = True
    i = 0
    print("Welcome to Secure File Storage")
    while(main):
        print("Press \n 1 to add a Group \n 2 to remove a Group \n 3 to encrypt a file \n 4 to decrypt a file \n 5 to edit a group \n 6 to exit")    
        i = int(input())
        if i < 1 or i > 6:
            print("Invalid Input")
        else: 
            ##Add a group      
            if i == 1:
                print("Enter the name of the group")
                group = input()
                print("Enter the password")
                password = input()
                keyManager.add_key(group, password, db)
                ##db.insertGroup(group, password)
            ##Remove a group
            elif i == 2:
                print("Enter the name of the group")
                group = input()
                print("Enter the password")
                password = input()
                print("Are you sure you want to delete this group? (y/n)")
                answer = input()
                if answer == "y":
                    keyManager.remove_key(group, password, db)
                else:
                    print("Group not deleted")
                db.deleteGroup(group)
            ##Encrypt a file
            elif i == 3:
                print("Enter your username")
                username = input()
                print("Enter the password")
                password = input()
                
                verify, group = keyManager.verifyUser(username, password, db)
                if verify == False:
                    print("Invalid Password")
                else:
                    print("Enter the name of the file")
                    filename = input()
                    key = keyManager.get_key(group, password, db)
                    ##if(key == None):
                    ##    print("Invalid Password")
                    ##else:
                    EncryptFile.encrypt(filename, key[1])


            ##Decrypt a file
            elif i == 4:
                print("Enter your username")
                username = input()
                print("Enter the password")
                password = input()
                verify, group = keyManager.verifyUser(username, password, db)

                if verify == False:
                    print("Invalid Password")
                else:
                    print("Enter the name of the file")
                    filename = input()
                    key = keyManager.get_key(group, password, db)    
                    DecryptFile.decrypt(filename, key[0])
            elif i == 5:
                editGroup()
            else:
                print("Goodbye")
                exit()