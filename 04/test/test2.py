user,passwd = 'huyd','123'

def auth(auth_type):     # 判断装饰器的参数
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if username == user and password == passwd:
                    print("\033[32;1mLogin successful!\033[0m")
                    res = func(*args,**kwargs)
                    return res
                else:
                    print("\033[31;1mInvalid username or password!\033[0m")
            elif auth_type == "ldap":
                print("Home page must be LDAP type Login！")
        return wrapper
    return outer_wrapper



@auth(auth_type="local")
def index():
    print("Welcome to index page!")
    return "Index"

@auth(auth_type="ldap")
def home():
    print("Welcome to home page!")
    return "Home"

# index()    # 进入index页面时使用本地验证登录
home()       # 进入home页面时使用LDAP验证登录
