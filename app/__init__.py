from support import configs
from support import strategies
from modules.database import Database
# from app.modules.mapper import Mapper
from app.modules.vortex import Vortex


def main():
    # vortex = Vortex(configs)
    # vortex.get_results()

    # print(vortex.articles)  # Get address
    # print(vortex.stats)

    # stg = strategies.TELECONTACT_STRATEGY
    # for a in stg:
    #     key = a
    #     print(stg[key])
    #     print(stg[key][0])
    #     print(stg[key][1][0])
    #     print(stg[key][1][1])

##

    db = Database(configs.DATABASE)
    #
    # db.execute("""  INSERT INTO companies (ID, NAME, CAPITAL) VALUES (%s,%s,%s) """, (1, 'One Plus', 20000))
    # db.fetch("""  SELECT 3 * 4; """)
    db.disconnect()

if __name__ == "__main__":
    main()
