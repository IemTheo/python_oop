from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password

    @property
    def email(self):
        print(f"Email accessed at {datetime.now()}")
        print(self._email)
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
    

user1 = User("Theo", "thma@gmail.com", "1234")
# user2 = User("Qetusi", "qemi@gmail.com", "1234")

user1.email

user1.email = "thma@irida.page"

user1.email


