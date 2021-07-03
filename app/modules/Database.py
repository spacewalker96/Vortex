import psycopg2


class Database:
    def __init__(self, database):
        try:
            self.Connection = psycopg2.connect(user=database["user"],
                                               password=database["password"],
                                               host=database["host"],
                                               port=database["port"],
                                               database=database["database"])

            self.Cursor = self.Connection.cursor()
            # Print PostgreSQL Connection properties
            print(self.Connection.get_dsn_parameters(), "\n")

            # Print PostgreSQL version
            self.Cursor.execute("SELECT version();")
            record = self.Cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def fetch(self, sql_query, values=()):
        self.Cursor.execute(sql_query, values)
        record = self.Cursor.fetchone()
        print(record)

    def execute(self, sql_query, values=()):
        self.Cursor.execute(sql_query, values)
        self.Connection.commit()
        count = self.Cursor.rowcount
        print(count, "Record Updated successfully ")

    def disconnect(self):
        if self.Connection:
            self.Cursor.close()
            self.Connection.close()
            print("PostgreSQL connection is closed")
