"""empty message

Revision ID: c74d64cbbb99
Revises: 08e1d3bbcd8d
Create Date: 2022-07-01 13:51:17.816187

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c74d64cbbb99'
down_revision = '08e1d3bbcd8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_test',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=200), nullable=False),
    sa.Column('nickname', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('phonenumber', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phonenumber'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_data',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False, comment='用户id，唯一标识'),
    sa.Column('name', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=30), nullable=False, comment='用户名'),
    sa.Column('nickname', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=30), nullable=True, comment='用户昵称，可重名'),
    sa.Column('passwd', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=20), nullable=False, comment='用户登录密码'),
    sa.Column('gender', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=6), nullable=True, comment='用户性别'),
    sa.Column('balance', mysql.INTEGER(unsigned=True), server_default=sa.text("'0'"), autoincrement=False, nullable=True, comment='账户余额，单位为人民币'),
    sa.Column('create_time', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True, comment='用户创建时间'),
    sa.Column('viplevel', mysql.INTEGER(), server_default=sa.text("'0'"), autoincrement=False, nullable=True, comment='vip等级'),
    sa.Column('avatar', mysql.MEDIUMBLOB(), nullable=True, comment='用户头像'),
    sa.Column('phonenumber', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=11), nullable=True, comment='用户手机号码'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB',
    mysql_row_format='DYNAMIC'
    )
    op.create_index('name', 'user_data', ['name'], unique=False)
    op.drop_table('user_test')
    # ### end Alembic commands ###
