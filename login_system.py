# Program that allows a super user to create user and a password
# Remove users and allow a super user to see all users and passwords
# standard user can do a limited function

user_list = []

class User(object):
    """User object"""
    user_number = 0
    def __init__(self, name, password):
        self.name = name
        self.password = password
        user_list.append(self)
        User.user_number += 1

class superUser(User):
    """superUser Object"""
    def __init__(self, name, password):
        super(superUser, self).__init__(name, password)

    def printUserList(user_list):
        for user in user_list:
            print "Username: " + user.name + " Password: " + user.password

    def userInfo(User):
        print "Username: " + User.name
        print "Password: " + User.password

def totalCount():
        if User.user_number == 1:
            print "There is one total user: " + "%i" % User.user_number
        else:
            print "There are a total of %i users currently in the system "  % User.user_number
