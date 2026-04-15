from __future__ import annotations


def test_database_connection_creates_new_connection_per_instance(monkeypatch):
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

    db1 = dbmod.DatabaseConnection()
    db2 = dbmod.DatabaseConnection()

    assert connect_calls["count"] == 2
    assert db1.conn is not db2.conn
