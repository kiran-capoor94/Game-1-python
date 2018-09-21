#!/usr/bin/env python
""" Intro file"""
import sys


class User:
    """ class"""
    name = ""
    age = 0
    height = 0
    weight = 0

    def display(self):
        """Display data"""
        print('')
        print('User Information:')
        print('User Name  :', self.name)
        print('User Age   :', self.age)
        print('User Height:', self.height)
        print('User Weight:', self.weight)

    def loadFromInput(self):
        """Take input"""
        self.name = input('Enter User Name: ')
        self.age = int(input('Enter Age: '))
        self.height = float(input('Enter Height (in feet): '))
        self.weight = int(input('Enter Weight: '))

    def save(self):
        """Saving on a file"""
        f = open('user.info', 'w')
        f.write(self.name + '\n')
        f.write(str(self.age) + '\n')
        f.write(str(self.height) + '\n')
        f.write(str(self.weight) + '\n')
        f.close()

    def loadFromFile(self):
        """Load frm file"""
        f = open('user.info', 'r')
        self.name = f.readline().rstrip()
        self.age = int(f.readline())
        self.height = float(f.readline())
        self.weight = float(f.readline())
        
theUser = None

if len(sys.argv) > 1 and sys.argv[1] == 'READ':
    theUser = User()
    theUser.loadFromFile()
else:
    theUser = User()
    theUser.loadFromInput()
    theUser.save()

theUser.display()
