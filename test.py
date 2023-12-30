from peewee import SqliteDatabase, Model, CharField, IntegerField

# подключаемся к базе данных my_database.db
db = SqliteDatabase("my_database.db")


# создаём модель User
class User(Model):
    # имя пользователя, CharField -- строка
    name = CharField()
    # возраст пользователя, IntegerField -- целое число
    age = IntegerField()

    # во внутреннем классе Meta указываем нашу базу данных
    class Meta:
        database = db


# создаём таблицу users в базе данных
db.create_tables([User])
user1 = User(name="Дима", age=25)
user1.save()
user2 = User(name="Костя", age=30)
user2.save()
users = User.select() # получаем список пользователей

# Дима 25
# Костя 30
retrieved_user = User.get(User.name == "Дима")
retrieved_user.name = "Дмитрий"
retrieved_user.save()
user2.delete_instance("Дмитрий")
for user in users:
    print(user.name, user.age)