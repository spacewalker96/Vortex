from modules.Database import Database
from modules.Entity import Entity
from modules.Vortex import Vortex
from configs import configs


def main():
    # db = Database(configs.DATABASE)
    #
    # # db.execute("""  INSERT INTO Vortex (ID, NAME, CAPITAL) VALUES (%s,%s,%s) """, (1, 'One Plus', 20000))
    # db.fetch("""  SELECT 3 * 4; """)
    # db.disconnect()

    schema = {
        "name": None,
        "address": None,
        "description": None,
        "prestation": None,
        "phone_number": None,
        "website": None
    }

    entity = Entity(schema)

    vortex = Vortex(configs)
    vortex.get_results(entity)
    print(vortex.Results)
    print(vortex.Stats)


if __name__ == "__main__":
    main()
