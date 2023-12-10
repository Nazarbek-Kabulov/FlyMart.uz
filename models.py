from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Text,
    MetaData,
    TIMESTAMP,
    Boolean,
    ForeignKey,
    DECIMAL
)

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('phone', String),
    Column('password', String),
    Column('gender', Boolean),
    Column('date_of_birth', TIMESTAMP),
    Column('user_pic', String)
)

product_sizes = Table(
    'product_sizes',
    metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('size_id', Integer, ForeignKey('size.id'))
)

products = Table(
    'products',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('about', Text),
    Column('description', Text),
    Column('price', DECIMAL(precision=10, scale=2)),
    Column('brand_id', ForeignKey('brand.id')),
    Column('vendor_id', ForeignKey('vendor.id')),
    Column('status', ForeignKey('status.id')),
    Column('image', String)
)

product_size_relationship = relationship("size", secondary=product_sizes, backref='products')

vendor = Table(
    'vendor',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('image', String)
)

brand = Table(
    'brand',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('image', String)
)

status = Table(
    'status',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String)
)

size = Table(
    'size',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('size', String)
)

category = Table(
    'category',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String)
)

subcategory = Table(
    'subcategory',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('subcategory', ForeignKey('category.id'))
)

user_cart = Table(
    'user_cart',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)
