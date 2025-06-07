from prettytable import PrettyTable

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(user_id = "001", username = "Gabriel")
user_2 = User(user_id = "002", username = "Kace")

user_1.follow(user_2)

table = PrettyTable()
table.field_names = ["User ID", "Username", "Followers", "Following"]
table.add_row(list(user_1.__dict__.values()))
table.add_row(list(user_2.__dict__.values()))
print(table)