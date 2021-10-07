import unittest
from inspect import signature
import sqlite3
from functools import reduce
import operator as op
import re
import os


def __get_tables_fields__(cursor: sqlite3.Cursor) -> dict:
    obj_tables = cursor.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall()
    data = {}
    for table in obj_tables:  # type: sqlite3.Row
        table_name = table['name']
        data[table_name] = [x['name'] for x in cursor.execute("PRAGMA table_info(%s)" % table_name).fetchall()]

    return data


def __get_table_number_of_rows__(cursor: sqlite3.Cursor) -> dict:
    obj_tables = cursor.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall()
    data = {}
    for table in obj_tables:  # type: sqlite3.Row
        table_name = table['name']
        data[table_name] = cursor.execute("SELECT COUNT(*) FROM %s" % table_name).fetchone()['COUNT(*)']

    return data


def __get_primary_keys__(cursor: sqlite3.Cursor):
    obj_tables = cursor.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall()
    data = {}
    for table in obj_tables:  # type: sqlite3.Row
        table_name = table['name']
        data[table_name] = [{'name': x['name'], 'is_pk': x['pk']} for x in cursor.execute("PRAGMA table_info(%s)" % table_name).fetchall()]

    return data


def __get_foreign_key_count__(cursor: sqlite3.Cursor):
    obj_tables = cursor.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall()
    data = {}
    for table in obj_tables:  # type: sqlite3.Row
        table_name = table['name']
        data[table_name] = len(cursor.execute("PRAGMA foreign_key_list(%s)" % table_name).fetchall())

    return data


class Testador(unittest.TestCase):
    def test_number_tables(self):
        """
        Checa o número de tabelas
        """
        from banco import main, SQLite
        main(path='banco', db_name='test.db')

        with SQLite(os.path.join('banco', 'test.db')) as cursor:
            fields = __get_tables_fields__(cursor)  # type: dict

            self.assertGreaterEqual(len(fields), 4, "O banco de dados precisa ter ao menos quatro tabelas!")

    def test_minimum_columns(self):
        """
        Checa o número de colunas por tabelas
        """
        from banco import main, SQLite
        main(path='banco', db_name='test.db')

        with SQLite(os.path.join('banco', 'test.db')) as cursor:
            tables = __get_tables_fields__(cursor)  # type: dict

            for k, v in tables.items():
                self.assertGreaterEqual(len(v), 2, "O banco de dados precisa ter ao menos duas colunas por tabela!")

    def test_optimal_columns(self):
        """
        Checa se ao menos uma tabela tem 4 colunas
        """
        from banco import main, SQLite
        main(path='banco', db_name='test.db')

        with SQLite(os.path.join('banco', 'test.db')) as cursor:
            tables = __get_tables_fields__(cursor)  # type: dict

            max_columns = 0
            for k, v in tables.items():
                max_columns = max(max_columns, len(v))

            self.assertGreaterEqual(max_columns, 4, "Pelo menos uma tabela precisa ter quatro colunas!")

    def test_minimum_tuples(self):
        """
        Checa se as tabelas possuem ao menos duas tuplas
        """
        from banco import main, SQLite
        main(path='banco', db_name='test.db')

        with SQLite(os.path.join('banco', 'test.db')) as cursor:
            rows = __get_table_number_of_rows__(cursor)  # type: dict

            for k, v in rows.items():
                self.assertGreaterEqual(v, 2, "Todas as tabelas do banco precisam ter ao menos duas tuplas!")

    def test_optimal_tuples(self):
        """
        Checa se ao menos uma tabela possui 10 tuplas
        """
        from banco import main, SQLite
        main(path='banco', db_name='test.db')

        with SQLite(os.path.join('banco', 'test.db')) as cursor:
            rows = __get_table_number_of_rows__(cursor)  # type: dict

            max_tuples = 0
            for k, v in rows.items():
                max_tuples = max(max_tuples, v)

            self.assertGreaterEqual(max_tuples, 10, "Pelo menos uma tabela precisa ter 10 tuplas!")

    def test_primary_keys(self):
        """
        Testa se todas as tabelas possuem primary keys.
        """
        from banco import main, SQLite
        main(path='banco', db_name='test.db')

        with SQLite(os.path.join('banco', 'test.db')) as cursor:
            pks = __get_primary_keys__(cursor)

            for k, v in pks.items():
                found = False
                for field in v:
                    if field['is_pk'] > 0:
                        found = True
                        break
                self.assertTrue(found, "Todas as tabelas precisam ter ao menos uma primary key!")

    def test_composite_primary_keys(self):
        """
        Testa se ao menos uma tabela possui chave primária composta.
        """
        from banco import main, SQLite
        main(path='banco', db_name='test.db')

        with SQLite(os.path.join('banco', 'test.db')) as cursor:
            pks = __get_primary_keys__(cursor)

            found = False
            for k, v in pks.items():
                for field in v:
                    if field['is_pk'] > 1:
                        found = True
                        break
                if found:
                    break
            self.assertTrue(found, "Pelo menos uma tabela precisa ter chave primária composta!")

    def test_foreign_keys(self):
        """
        Testa se ao menos uma tabela possui chave estrangeira
        """
        from banco import main, SQLite
        main(path='banco', db_name='test.db')

        with SQLite(os.path.join('banco', 'test.db')) as cursor:
            pks = __get_foreign_key_count__(cursor)

            count = 0
            for k, v in pks.items():
                count += v
            self.assertGreaterEqual(count, 1, "Pelo menos uma tabela precisa ter chave estrangeira!")


if __name__ == '__main__':
    unittest.main()
