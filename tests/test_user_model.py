from app.models import Pedido, Usuario


def test_usuario_uses_usuario_id_as_primary_key_and_fk_reference():
    assert hasattr(Usuario, "usuario_id")
    assert Usuario.__table__.columns["usuario_id"].primary_key is True

    usuario_id_column = Pedido.__table__.columns["usuario_id"]
    assert usuario_id_column is not None

    foreign_keys = list(usuario_id_column.foreign_keys)
    assert len(foreign_keys) == 1
    assert foreign_keys[0].target_fullname == "usuarios.usuario_id"
