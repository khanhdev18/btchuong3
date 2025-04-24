import sqlite3

# Tạo file cơ sở dữ liệu mẫu
database_file = "database.sqlite3"  # Tên file cơ sở dữ liệu
connection = sqlite3.connect(database_file)

# Tạo bảng mẫu
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sample_table (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

# Thêm dữ liệu mẫu
cursor.execute("INSERT INTO sample_table (name, age) VALUES ('Alice', 25), ('Bob', 30)")
connection.commit()

# Đóng kết nối
connection.close()

print(f"Đã tạo file cơ sở dữ liệu mẫu: {database_file}")
