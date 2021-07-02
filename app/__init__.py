from modules.Database import Database
from modules.Schema import Schema
from modules.Vortex import Vortex


def main():
    db = Database('postgres', 'toor', 'localhost', '5432', 'Vortex')
    db.disconnect()

    # vortex = Vortex
    # result = vortex.get_results()
    # print(result)


if __name__ == "__main__":
    main()
