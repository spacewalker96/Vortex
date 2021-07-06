import psycopg2


class Database:
    def __init__(self, database):
        try:
            self.connection = psycopg2.connect(user=database["user"],
                                               password=database["password"],
                                               host=database["host"],
                                               port=database["port"],
                                               database=database["database"])

            self.cursor = self.connection.cursor()
            # Print PostgreSQL Connection properties
            print(self.connection.get_dsn_parameters(), "\n")

            # Print PostgreSQL version
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def fetch(self, sql_query, values=()):
        self.cursor.execute(sql_query, values)
        record = self.cursor.fetchone()
        print(record)

    def execute(self, sql_query, values=()):
        self.cursor.execute(sql_query, values)
        self.connection.commit()
        count = self.cursor.rowcount
        print(count, "Record Updated successfully ")

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")


