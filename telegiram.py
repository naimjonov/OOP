class Telegram:
    def __init__(self, user_name):
        self.user_name = user_name
        self.accept_chat_text = ""
        self.chat_status = ""
        self.chat_time = ""

    def input_data(self):
        self.user_name = input("foydalanuvchi nomini kiriting: ")

    def display_data(self):
        print(f"foydalanuvchi: {self.user_name} xabar: {self.accept_chat_text} status: {self.chat_status}")

    def send(self, other_user):
        message = input(f"{self.user_name} dan xabar kiriting: ")
        other_user.accept_chat_text = message
        other_user.chat_status = "sending"
        print(f"{self.user_name} yubordi: {message} -> {other_user.user_name}")

    def read(self):
        self.chat_status = "reading"
        print(f"{self.user_name} xabarni oqidi: {self.accept_chat_text}")

    def delete(self):
        self.accept_chat_text=""
        self.chat_status = "deleted"
        print(f"{self.user_name} xabarni ochirdi")

user1=Telegram("")
user2=Telegram("")

user1.input_data()
user2.input_data()

user1.send(user2)
user2.read()
user2.delete()

user1.display_data()
user2.display_data()
