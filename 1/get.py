from sqlalchemy import create_engine, select, MetaData, Table, and_

engine = create_engine('sqlite:///example.db')
metadata = MetaData()

table = Table(
    'person',
    metadata,
)

stmt = select(table.columns.age).where(table.age > 8)

connection = engine.connect()
results = connection.execute(stmt).fetchall()

for r in results:
    print((r))