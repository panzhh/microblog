"""empty message

Revision ID: c3b3262ce235
Revises: 21f13bc21054
Create Date: 2024-06-08 23:42:18.267878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3b3262ce235'
down_revision = '21f13bc21054'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('borrowed_book',
    sa.Column('bid', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('borrow_date', sa.String(length=140), nullable=False),
    sa.Column('due_date', sa.String(length=140), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('bid')
    )
    with op.batch_alter_table('borrowed_book', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_borrowed_book_book_id'), ['book_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_borrowed_book_user_id'), ['user_id'], unique=False)

    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.VARCHAR(length=140),
               type_=sa.String(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=140),
               existing_nullable=False)

    with op.batch_alter_table('borrowed_book', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_borrowed_book_user_id'))
        batch_op.drop_index(batch_op.f('ix_borrowed_book_book_id'))

    op.drop_table('borrowed_book')
    # ### end Alembic commands ###