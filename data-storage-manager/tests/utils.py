import sqlalchemy as sa

def create_tables(url, engine=None):
    from simcore_service_dsm.models import users

    meta = sa.MetaData()
    if not engine:
        engine = sa.create_engine(url)

    meta.create_all(bind=engine, tables=[users])