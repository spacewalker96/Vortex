from configs import database
from strategies import telecontact
from modules.database import Database
# from app.modules.mapper import Mapper
from app.modules.vortex import Vortex


def main():
    vortex = Vortex(database, telecontact)
    vortex.get_results()
    print(vortex.stats)
    vortex.extract_data()

    # stg = strategies.TELECONTACT_STRATEGY
    # for a in stg:
    #     print(a)
    #     print(stg[a])
    #     print(stg[a][0])
    #     print(stg[a][1][0])
    #     print(stg[a][1][1])
    #     if stg[a][0] == "find_child":
    #         print(stg[a][2][0])
    #         print(stg[a][2][1])


##

    # db = Database(configs.DATABASE)
    # db.execute("""  INSERT INTO companies (NAME, DESCRIPTION, PRESTATIONS) VALUES (%s,%s,%s) """,
    #            ('One Plus', 'Blabla lorem ipsum', 'Cuisine, Menage'))
    # db.fetch(""" SELECT * FROM companies """)
    # db.disconnect()


if __name__ == "__main__":
    main()
