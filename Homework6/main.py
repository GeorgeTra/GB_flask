"""Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц:
товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY),
id товара (FOREIGN KEY), дата заказа и статус заказа.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API."""


import sqlalchemy, databases, uvicorn
from sqlalchemy import Column, String, Integer, Table, DECIMAL, DateTime, ForeignKey
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional
import enum, datetime


DATABASE_URL = "sqlite:///mydatabase.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = Table(
    'users2',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(32), nullable=False),
    Column('last_name', String(32), nullable=False),
    Column('email', String(128), nullable=False, unique=True),
    Column('password', String(128), nullable=False)
)

products = Table(
    'products2',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(32), nullable=False, unique=True),
    Column('description', String, nullable=False),
    Column('price', DECIMAL(10, 2), default=0)
)


class OrderStatus(enum.Enum):
    created = 'создан'
    in_progress = 'формируется'
    confirmed = 'подтвержден'
    in_delivery = 'доставляется'
    delivered = 'доставлен'
    closed = 'закрыт'


orders = Table(
    'orders2',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users2.id')),
    Column('product_id', Integer, ForeignKey('products2.id')),
    Column('order_date', DateTime),
    Column('status', String(32), default=OrderStatus.created)
)


engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class UserIn(BaseModel):
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)
    email: str
    password: str


class User(UserIn):
    id: int


class ProductIn(BaseModel):
    name: str
    description: str
    price: float


class Product(ProductIn):
    id: int


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    datetime_create: Optional[datetime.datetime] = Field(default_factory=lambda: datetime.datetime.now())
    status: Optional[OrderStatus] = Field(default=OrderStatus.created)


class Order(OrderIn):
    id: int


# @app.get('/users/{count}', tags=['Создаем фейковых пользователей'])
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(first_name=f'firstname{i}', last_name=f'lastname{i}',
#                                       email=f'user{i}@mail.ru', password=f'{i}qwerty')
#         await database.execute(query)
#     return {'message': f'{count} fake users were created'}


# @app.get('/products/{count}', tags=['Добавляем фейковые товары'])
# async def create_products(count: int):
#     for i in range(count):
#         query = products.insert().values(name=f'{i} product', description=f'Some description № {i}', price=i * 10)
#         await database.execute(query)
#     return {'message': f'{count} fake products created'}


@app.post('/users/', response_model=User, tags=['Добавляем пользователя'])
async def add_user(user: UserIn):
    query = users.insert().values(first_name=user.first_name, last_name=user.last_name, email=user.email,
                                  password=user.password)
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.post('/add_product/', response_model=Product, tags=['Добавляем товар'])
async def add_product(product: ProductIn):
    query = products.insert().values(name=product.name, description=product.description, price=product.price)
    last_product_id = await database.execute(query)
    return {**product.model_dump(), "product_id": last_product_id}


@app.post('/add_order/', response_model=Order, tags=['Добавляем заказ'])
async def create_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id, product_id=order.product_id,
                                   order_date=order.datetime_create, status=order.status)
    last_order_id = await database.execute(query)
    return {**order.model_dump(), 'order_id': last_order_id}


@app.get('/users/', response_model=List[User], tags=['Получаем список пользователей'])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/products/', response_model=List[Product], tags=['Получаем список всех товаров'])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User, tags=['Получаем пользователя по ID'])
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.get('/products/{product_id}', response_model=Product, tags=['Получаем товар по ID'])
async def read_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@app.put('/users/{user_id}', response_model=User, tags=['Обновляем данные пользователя по ID'])
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), 'id': user_id}


@app.put('/update_product/{product_id}', response_model=Product, tags=['Обновляем данные товара по ID'])
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.model_dump())
    await database.execute(query)
    return {**new_product.model_dump(), 'id': product_id}


@app.delete('/users/{user_id}', tags=['Удаляем пользователя по ID'])
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': f'user {user_id} has been deleted'}


@app.delete('/delete_products/{product_id}', tags=['Удаляем товар по ID'])
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': f'product № {product_id} has been deleted'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)



