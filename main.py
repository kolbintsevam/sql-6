import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Book, Publisher, Shop, Stock, Sale

login = input("Введите логин: ")
password = input("Пароль: ")
name_base = input("Название БД: ")
DSN = f'postgresql://{login}:{password}@localhost:5432/{name_base}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

name = input("Введите имя автора для просмотра информации: ")

result = session.query(Stock, Book.title, Shop.name, Sale.price, Sale.date_sale)
result = result.join(Sale)
result = result.join(Shop)
result = result.join(Book)
result = result.join(Publisher)
result = result.filter(Publisher.name == name)
for c in result:
    print(*c[1:], sep="|")
session.close()