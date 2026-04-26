import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',  # Add your MySQL password
            db='resume_analyzer'
        )
        self.cursor = self.connection.cursor()
        self.create_database()
        self.create_table()

    def create_database(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS resume_analyzer")
        self.cursor.execute("USE resume_analyzer")

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS user_data (
            ID INT NOT NULL AUTO_INCREMENT,
            Name VARCHAR(100) NOT NULL,
            Email VARCHAR(100) NOT NULL,
            resume_score VARCHAR(8) NOT NULL,
            Timestamp VARCHAR(50) NOT NULL,
            Page_no VARCHAR(5) NOT NULL,
            Predicted_Field VARCHAR(50) NOT NULL,
            User_level VARCHAR(50) NOT NULL,
            Actual_skills TEXT NOT NULL,
            Recommended_skills TEXT NOT NULL,
            Recommended_courses TEXT NOT NULL,
            PRIMARY KEY (ID)
        );
        """
        self.cursor.execute(query)

    def insert_data(self, name, email, score, timestamp, pages, field, level, skills, recommended_skills, courses):
        insert_sql = """INSERT INTO user_data 
        (Name, Email, resume_score, Timestamp, Page_no, Predicted_Field, User_level, Actual_skills, Recommended_skills, Recommended_courses)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (name, email, score, timestamp, pages, field, level, skills, recommended_skills, courses)
        self.cursor.execute(insert_sql, values)
        self.connection.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM user_data")
        return self.cursor.fetchall()