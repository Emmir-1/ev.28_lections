from register import RegisterMixin, LoginMixin

class User(RegisterMixin, LoginMixin):
    pass

obj = User()

# print(obj.register("JohnSnnow", "John", "Snow", "bastard123", "bastard123"))
print(obj.login("JohnSnnow", "bastard123"))


