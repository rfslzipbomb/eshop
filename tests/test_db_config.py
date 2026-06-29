import os

from app import create_app


def test_database_uri_is_absolute_and_sqlite_path_exists():
    app = create_app()
    uri = app.config['SQLALCHEMY_DATABASE_URI']

    assert uri.startswith('sqlite:///')
    assert uri.endswith('eshop.db')

    database_path = uri.replace('sqlite:///', '', 1)
    assert os.path.exists(database_path)
    assert os.path.exists(os.path.dirname(database_path))
