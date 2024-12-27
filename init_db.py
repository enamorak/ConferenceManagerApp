import mysql.connector

# Подключение к базе данных (для создания базы данных)
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Укажите ваш логин
    password="password"  # Укажите ваш пароль
)

cursor = db_connection.cursor()

# Создание базы данных, если она не существует
cursor.execute("CREATE DATABASE IF NOT EXISTS conference_manager")

# Подключение к только что созданной базе данных
db_connection.database = "conference_manager"

# Создание таблиц, если их нет
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        password VARCHAR(255),
        role ENUM('organizer', 'speaker', 'participant', 'admin') NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Events (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        description TEXT,
        date DATETIME,
        speaker_id INT,
        FOREIGN KEY (speaker_id) REFERENCES Users(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Surveys (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        description TEXT,
        created_at DATETIME,
        event_id INT,
        FOREIGN KEY (event_id) REFERENCES Events(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Reports (
        id INT AUTO_INCREMENT PRIMARY KEY,
        content TEXT,
        created_at DATETIME
    )
""")

# Завершаем выполнение запросов и закрываем соединение
db_connection.commit()
cursor.close()
db_connection.close()

print("Database and tables are successfully created or already exist.")
