import pytest
import utils

def test_table_creation(postgres_service):
    utils.create_tables(url=postgres_service)
    a=12