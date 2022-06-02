import functools

login = False
def dec(func):
    @functools.wraps(func)
    def abc():
        if login:
            func()
        else:
            print("login first")
    return abc

@dec
def dashboard():
    print("dashboard")

@dec
def loogin():
    print("loogin")

dashboard()