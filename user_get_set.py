import datetime


class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password
    
    def set_pass(self):
        old_pass = input("Introduce your previous password: ")

        if old_pass == self.__password:
            self.__password = input("Introduce your new password: ")
            print(f'Password was successfully changed at {datetime.now()}')
        else:
            print("Your privious password is not correct")
        print(self.__password)

    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email

    def get_email(self):
        return self._email

    def say_hi_to_user(self, user):
        print(
            f"{self.username}: Hi {user.username}, it's {self.username}"
        )


user1 = User("Theo", "thma@gmail.com", "1234")
# user2 = User("Qetusi", "qemi@gmail.com", "1234")
# user1.say_hi_to_user(user2)


user1.set_email("thma@gmail.com")

print(user1.get_email)

