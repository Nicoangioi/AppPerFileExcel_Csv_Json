from Login import Login

class MainApp:
    def __init__(self):
        self.login = Login()

    def run(self):
        self.login.run()


if __name__ == "__main__":
    Login().run()

