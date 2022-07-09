#03 user database

class User:
    def __init__(self, user_name, name, email):
        self.user_name = user_name
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(user_name = {self.user_name}, name = '{self.name}', email = '{self.email}')"

    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self, name):
        self.name = name
        self.database = []

    def insert(self, user):
        i = 0
        while i < len(self.database):
            if self.database[i].user_name > user.user_name:
                break
            i += 1
        self.database.insert(i, user)

    def find(self, user):
        i = 0
        while i < len(self.database):
            if self.database[i].user_name == user:
                return self.database[i]
            i += 1
        return f'user {user} not found!'   #type = str

    def update(self, user, name, email):
        found = self.find(user)
        if type(found) != str:
            found.name, found.email = name, email
            return found
        else:
            return f'user {user} not updated！'  #type = str

    def list_all(self):
        return self.database


def get_data_from_csv(csv_file):
    csv_data = open(csv_file, 'r')     #csv name
    global user_list
    user_list = []
    for u in csv_data:
        user_list.append(User(u.split(',')[0],u.split(',')[1],u.split(',')[2]))
    csv_data.close()
    return  user_list


def manipulate_database():
    #create database for a company
    global google
    google = UserDatabase('google')

    #insert data into database
    for u in user_list:
        google.insert(u)
    print(google.list_all())

    #find a user in the database
    print(google.find('syy'))
    print(google.find('kkk')) #not found

    #update a user's details
    print(google.update('syy', 'sia you yang', 'syy@hotmail.com'))
    print(google.update('kkk', 'koo kian kiet', 'kkk@hotmail.com')) #not updated

    #list out the final database
    print(google.list_all())

if __name__ == "__main__":
    get_data_from_csv("user_data.csv")
    manipulate_database()

