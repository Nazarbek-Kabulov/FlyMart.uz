"""Create flymart models.

Revision ID: 0564ce84fae9
Revises: 
Create Date: 2023-12-10 17:44:28.690790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0564ce84fae9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('size',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('size', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('gender', sa.Boolean(), nullable=True),
    sa.Column('date_of_birth', sa.TIMESTAMP(), nullable=True),
    sa.Column('user_pic', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('about', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['status'], ['status.id'], ),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subcategory',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('subcategory', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subcategory'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_sizes',
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('size_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['size_id'], ['size.id'], )
    )
    op.create_table('user_cart',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_cart')
    op.drop_table('product_sizes')
    op.drop_table('subcategory')
    op.drop_table('products')
    op.drop_table('vendor')
    op.drop_table('users')
    op.drop_table('status')
    op.drop_table('size')
    op.drop_table('category')
    op.drop_table('brand')
    # ### end Alembic commands ###
