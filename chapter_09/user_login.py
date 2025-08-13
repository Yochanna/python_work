class User:
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first.title()} {self.last.title()}, age {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



if __name__ == "__main__":
    u = User("ada", "lovelace", 36)
    u.describe_user()
    for _ in range(3):
        u.increment_login_attempts()
    print("Login attempts:", u.login_attempts)
    u.reset_login_attempts()
    print("Login attempts after reset:", u.login_attempts)
