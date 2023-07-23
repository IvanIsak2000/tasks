import sqlalchemy as db

engine = db.create_engine('sqlite:///products.db')

connection = engine.connect()

metadata = db.MetaData()

products = db.Table('products', metadata, 
    db.Column('product_id', db.Integer, primary_key=True, nullable=False),
    db.Column('product_name', db.Text),
    db.Column('supplier_name', db.Text),
    db.Column('product_price', db.Integer)
)

metadata.create_all(engine)

insertion_query = products.insert().values([
    {'product_name':'Banana', 'supplier_name':'Balanaland', 'product_price':1000},
    {'product_name':'Apples', 'supplier_name':'Applesland', 'product_price':5000}
])

# connection.execute(insertion_query)

select_all_data = db.select([products])
select_all_result = connection.execute(select_all_data)

print(select_all_result.fetchall())

#Error

# Traceback (most recent call last):
#   File "/home/iwan/GITHUB/PY/sqlalchemy/2/test.py", line 25, in <module>
#     select_all_data = db.select([products])
#   File "/home/iwan/.local/lib/python3.10/site-packages/sqlalchemy/sql/_selectable_constructors.py", line 489, in select
#     return Select(*entities)
#   File "/home/iwan/.local/lib/python3.10/site-packages/sqlalchemy/sql/selectable.py", line 5130, in __init__
#     self._raw_columns = [
#   File "/home/iwan/.local/lib/python3.10/site-packages/sqlalchemy/sql/selectable.py", line 5131, in <listcomp>
#     coercions.expect(
#   File "/home/iwan/.local/lib/python3.10/site-packages/sqlalchemy/sql/coercions.py", line 413, in expect
#     resolved = impl._literal_coercion(
#   File "/home/iwan/.local/lib/python3.10/site-packages/sqlalchemy/sql/coercions.py", line 651, in _literal_coercion
#     self._raise_for_expected(element, argname)
#   File "/home/iwan/.local/lib/python3.10/site-packages/sqlalchemy/sql/coercions.py", line 1139, in _raise_for_expected
#     return super()._raise_for_expected(
#   File "/home/iwan/.local/lib/python3.10/site-packages/sqlalchemy/sql/coercions.py", line 710, in _raise_for_expected
#     super()._raise_for_expected(
#   File "/home/iwan/.local/lib/python3.10/site-packages/sqlalchemy/sql/coercions.py", line 535, in _raise_for_expected
#     raise exc.ArgumentError(msg, code=code) from err
# sqlalchemy.exc.ArgumentError: Column expression, FROM clause, or other columns clause element expected, got [Table('products', MetaData(), Column('product_id', Integer(), table=<products>, primary_key=True, nullable=False), Column('product_name', Text(), table=<products>), Column('supplier_name', Text(), table=<products>), Column('product_price', Integer(), table=<products>), schema=None)]. Did you mean to say select(Table('products', MetaData(), Column('product_id', Integer(), table=<products>, primary_key=True, nullable=False), Column('product_name', Text(), table=<products>), Column('supplier_name', Text(), table=<products>), Column('product_price', Integer(), table=<products>), schema=None))?
