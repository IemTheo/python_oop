class User:
    user_count = 0
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1
    
    @staticmethod
    def display_user(self):
        print(f"Username: {self.username}, email: {self.email}")

user1 = User("Theo Mates", "thma@gmail.com")
user2 = User("Qetusi", "qemi@gmail.com")

user1.display_user()
print(user2.user_count)

