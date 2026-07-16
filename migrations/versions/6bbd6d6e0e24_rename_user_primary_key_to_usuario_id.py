"""rename user primary key to usuario_id

Revision ID: 6bbd6d6e0e24
Revises: 7f1ce8dd1792
Create Date: 2026-06-29 15:50:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = '6bbd6d6e0e24'
down_revision = '7f1ce8dd1792'
branch_labels = None
depends_on = None


def upgrade():
    if op.get_context().dialect.name == 'sqlite':
        inspector = sa.inspect(op.get_bind())
        if 'usuario' in inspector.get_table_names():
            op.rename_table('usuario', 'usuarios')
            op.alter_column('usuarios', 'id', new_column_name='usuario_id')
        elif 'usuarios' in inspector.get_table_names() and 'usuario_id' not in [c['name'] for c in inspector.get_columns('usuarios')]:
            op.alter_column('usuarios', 'id', new_column_name='usuario_id')
    else:
        if 'usuario' in op.get_context().inspect_options.get('table_names', []):
            op.rename_table('usuario', 'usuarios')
        op.alter_column('usuarios', 'id', new_column_name='usuario_id')


def downgrade():
    if op.get_context().dialect.name == 'sqlite':
        inspector = sa.inspect(op.get_bind())
        if 'usuarios' in inspector.get_table_names() and 'usuario_id' in [c['name'] for c in inspector.get_columns('usuarios')]:
            op.alter_column('usuarios', 'usuario_id', new_column_name='id')
            if 'usuario' not in inspector.get_table_names():
                op.rename_table('usuarios', 'usuario')
    else:
        op.alter_column('usuarios', 'usuario_id', new_column_name='id')
        op.rename_table('usuarios', 'usuario')
