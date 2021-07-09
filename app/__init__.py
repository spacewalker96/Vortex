from configs import database
from strategies import telecontact, charika
from modules.database import Database
from app.modules.vortex import Vortex


def main():
    vortex_telecontact = Vortex(telecontact)
    vortex_telecontact.get_results(3, 4)
    print(vortex_telecontact.stats)
    vortex_telecontact.extract_data()
    print(vortex_telecontact.records)

    vortex_charika = Vortex(charika)
    vortex_charika.get_results(1, 2)
    print(vortex_charika.stats)
    vortex_charika.extract_data()
    print(vortex_charika.records)

    db = Database(database.DATABASE)
    db.store_multiple_dict(vortex_telecontact.records, telecontact.NAME)
    db.store_multiple_dict(vortex_charika.records, charika.NAME)
    db.fetch(""" SELECT * FROM companies """)
    db.disconnect()


if __name__ == "__main__":
    main()
