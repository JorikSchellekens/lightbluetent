"""Replace references to societies with groups

Revision ID: 5575f9279bcb
Revises: 01f32af97678
Create Date: 2020-09-28 16:07:47.657106

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5575f9279bcb'
down_revision = '01f32af97678'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('short_name', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('short_description', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('socials', sa.JSON(), nullable=False),
    sa.Column('sessions', sa.JSON(), nullable=True),
    sa.Column('welcome_text', sa.String(), nullable=True),
    sa.Column('logo', sa.String(), nullable=False),
    sa.Column('bbb_logo', sa.String(), nullable=False),
    sa.Column('banner_text', sa.String(), nullable=True),
    sa.Column('banner_color', sa.String(), nullable=True),
    sa.Column('mute_on_start', sa.Boolean(), nullable=False),
    sa.Column('disable_private_chat', sa.Boolean(), nullable=False),
    sa.Column('attendee_pw', sa.String(), nullable=False),
    sa.Column('moderator_pw', sa.String(), nullable=False),
    sa.Column('uid', sa.String(), nullable=False),
    sa.Column('bbb_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('attendee_pw'),
    sa.UniqueConstraint('bbb_id'),
    sa.UniqueConstraint('moderator_pw'),
    sa.UniqueConstraint('short_name'),
    sa.UniqueConstraint('uid')
    )
    op.create_table('user_group',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'group_id')
    )
    op.drop_table('societies')
    op.drop_table('user_society')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_society',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('society_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['society_id'], ['societies.id'], name='user_society_society_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='user_society_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', 'society_id', name='user_society_pkey')
    )
    op.create_table('societies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('short_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('website', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('welcome_text', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('logo', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('banner_text', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('banner_color', sa.VARCHAR(), server_default=sa.text("'#e8e8e8'::character varying"), autoincrement=False, nullable=True),
    sa.Column('mute_on_start', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('disable_private_chat', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('attendee_pw', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('moderator_pw', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('uid', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('bbb_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('time_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('bbb_logo', sa.VARCHAR(), server_default=sa.text("'default_bbb_logo.png'::character varying"), autoincrement=False, nullable=False),
    sa.Column('sessions', postgresql.JSON(astext_type=sa.Text()), server_default=sa.text("'[]'::json"), autoincrement=False, nullable=True),
    sa.Column('short_description', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('socials', postgresql.JSON(astext_type=sa.Text()), server_default=sa.text("'[]'::json"), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='societies_pkey'),
    sa.UniqueConstraint('attendee_pw', name='societies_attendee_pw_key'),
    sa.UniqueConstraint('bbb_id', name='societies_bbb_id_key'),
    sa.UniqueConstraint('moderator_pw', name='societies_moderator_pw_key'),
    sa.UniqueConstraint('short_name', name='societies_short_name_key'),
    sa.UniqueConstraint('uid', name='societies_uid_key')
    )
    op.drop_table('user_group')
    op.drop_table('groups')
    # ### end Alembic commands ###
