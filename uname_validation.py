# Import System package to enable scripting and inputs.
import sys
# Define A class User and setup username validations.

class User:
    # Take Input from user
    uname = ""
    argv = ""
    def loadInput(self):
        self.uname = input("Enter your Username : ")
        saveInfo()

    def saveInfo(self):
        f =open('userinfo.txt', 'w')
        f.write(self.uname)
        f.close()
    
    def readInfo(self):
        f = open('userinfo.txt','r')
        self.uname = f.readLine().rstrip()
        f.close()
        return self.uname
    
    def validation(self):
        readInfo()
        print("Username" + self.uname)
    
    loadInput(argv)
