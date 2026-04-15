from __future__ import annotations


def test_get_default_db_reuses_single_connection(monkeypatch):
    import database.database as dbmod

    connect_calls = {"count": 0}

    class FakeCursor:
        def execute(self, _query, _params=()):
            return None

        def fetchone(self):
            return None

        def fetchall(self):
            return []

        def close(self):
            return None

    class FakeConn:
        def __init__(self):
            self.row_factory = None

        def execute(self, _query):
            return None

        def cursor(self):
            return FakeCursor()

        def commit(self):
            return None

        def rollback(self):
            return None

        def close(self):
            return None

    def fake_connect(_path):
        connect_calls["count"] += 1
        return FakeConn()

    monkeypatch.setattr(dbmod.os, "makedirs", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(dbmod.sqlite3, "connect", fake_connect)

    dbmod.close_default_db()
    db1 = dbmod.get_default_db()
    db2 = dbmod.get_default_db()

    assert db1 is db2
    assert connect_calls["count"] == 1

    dbmod.close_default_db()
    _db3 = dbmod.get_default_db()
    assert connect_calls["count"] == 2

