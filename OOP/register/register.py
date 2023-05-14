import json
import hashlib
import os

DIR_PATH = os.getcwd()
FILE_PATH = DIR_PATH + "/user.json"

class HashClassMixin:
    def _hash_password(self, password, salt = None):
        if not salt:
            salt = os.urandom(32)
        hashed_password = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
        return hashed_password



class RegisterMixin(HashClassMixin):
    """Миксин для регистраций"""
    
    def _validare_password(self, password, password2):
        if len(password) < 8:
            raise ValueError("Password is too short! must be at least 8 symbols!")
        elif password.isdigit() or password.isalpha():
            raise ValueError("Password must contain digits and characters!")
        elif password != password2:
            raise ValueError("Password didn\'t match!")
    
    def register(self, username, first_name, last_name, password, password2):
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            try:
                id = data[-1]["id"] + 1
            except (IndexError, ValueError):
                data = []
                id = 1
            is_username_used = any([x["username"] == username for x in data])

        self._validare_password(password, password2)
        salt = os.urandom(32)
        hashed_password = {"password": self._hash_password(password, salt).decode('latin-1'), "salt": salt.decode("latin-1")}
        # print(hashed_password["password"].decode("latin-1"))

        with open(FILE_PATH, "w") as file:
            if is_username_used:
                json.dump(data, file, indent=4)
                raise ValueError("Username is already taken!")
            user = {"id":id, "username": username, "first_name": first_name, "last_name": last_name, "password": hashed_password}
            data.append(user)
            json.dump(data, file, indent=4)
        return {"status": 201, "msg": "Seccessfully registered"}

class LoginMixin(HashClassMixin):
    """Миксин для логина"""
    def login(self, username, password):
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            try:
                user = list(filter(lambda x: x["username"] == username, data))[0]
            except IndexError:
                raise ValueError("Invalid password or useranme!")
            
            user_password = user["password"]["password"].encode("latin-1")
            salt = user["password"]["salt"].encode("latin-1")

            hashed_password = self._hash_password(password, salt)

            if user_password != hashed_password:
                raise ValueError("Invalid password!")
            
        return {"status": 200, "msg": "Successfully loggend in!", "user": user ["username"]}
    

# obj = RegisterMixin()
# obj_login = LoginMixin()
# # print(obj.register("JohnSnow25", "John", "Snow", "bastard123", "bastard123"))
# print(obj_login.login("JohnSnow28", "bastard123"))



