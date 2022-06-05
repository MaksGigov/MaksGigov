level = 0

login = ""
while not login:
    login = input("Логин: ")
password = ""
while not password:
    password = input("Пароль: ")

if login == "root" and password == "123":
    level = 10
elif login == "maks" and password == "321":
    level = 5
if level:
    print("Привет ", login)
    print("Ваш уровень доступа", level)

else:
    print("Неверный ввод")
