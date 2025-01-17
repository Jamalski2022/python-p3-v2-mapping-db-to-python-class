# from __init__ import CURSOR, CONN


# class Department:

#     def __init__(self, name, location, id=None):
#         self.id = id
#         self.name = name
#         self.location = location

#     def __repr__(self):
#         return f"<Department {self.id}: {self.name}, {self.location}>"

#     @classmethod
#     def create_table(cls):
#         """ Create a new table to persist the attributes of Department instances """
#         sql = """
#             CREATE TABLE IF NOT EXISTS departments (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             location TEXT)
#         """
#         CURSOR.execute(sql)
#         CONN.commit()

#     @classmethod
#     def drop_table(cls):
#         """ Drop the table that persists Department instances """
#         sql = """
#             DROP TABLE IF EXISTS departments;
#         """
#         CURSOR.execute(sql)
#         CONN.commit()

#     def save(self):
#         """ Insert a new row with the name and location values of the current Department instance.
#         Update object id attribute using the primary key value of new row.
#         """
#         sql = """
#             INSERT INTO departments (name, location)
#             VALUES (?, ?)
#         """

#         CURSOR.execute(sql, (self.name, self.location))
#         CONN.commit()

#         self.id = CURSOR.lastrowid

#     @classmethod
#     def create(cls, name, location):
#         """ Initialize a new Department instance and save the object to the database """
#         department = cls(name, location)
#         department.save()
#         return department

#     def update(self):
#         """Update the table row corresponding to the current Department instance."""
#         sql = """
#             UPDATE departments
#             SET name = ?, location = ?
#             WHERE id = ?
#         """
#         CURSOR.execute(sql, (self.name, self.location, self.id))
#         CONN.commit()

#     def delete(self):
#         """Delete the table row corresponding to the current Department instance"""
#         sql = """
#             DELETE FROM departments
#             WHERE id = ?
#         """

#         CURSOR.execute(sql, (self.id,))
#         CONN.commit()

from __init__ import CURSOR, CONN

class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO departments (name, location)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid  # Get the last inserted id

    @classmethod
    def create(cls, name, location):
        department = cls(name, location)
        department.save()
        return department

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM departments WHERE id = ?"
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return cls(name=row[1], location=row[2], id=row[0])
        return None

    @classmethod
    def instance_from_db(cls, row):
        return cls(name=row[1], location=row[2], id=row[0])  # Assumes row format is (id, name, location)

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM departments"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]  
        

    @classmethod
    def find_by_name(cls, name):
        """ Find a Department instance by its name. """
        sql = "SELECT * FROM departments WHERE name = ?"
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()
        if row:
            return cls.instance_from_db(row)  
        return None

    def update(self):
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM departments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None  




