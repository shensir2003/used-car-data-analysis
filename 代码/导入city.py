import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('city.csv')

# 替换以下信息为你的数据库连接信息
db_connection_info = {
    "host": "127.0.0.1",
    "database": "gp13",
    "user": "a2513210104",
    "password": "xawl-9905",
    "port": "9929"
}
# 读取CSV文件，手动指定每列的数据类型
columns_and_types = {
    "region_id": int,
    "parent_id": int,
    "name": str,
}
# 连接到数据库
engine = create_engine(
    f"postgresql://{db_connection_info['user']}:{db_connection_info['password']}@{db_connection_info['host']}:{db_connection_info['port']}/{db_connection_info['database']}")

# 将数据写入数据库
df.to_sql("city", engine, if_exists="replace", index=False, method="multi")

# 关闭数据库连接
engine.dispose()

print('success!')
