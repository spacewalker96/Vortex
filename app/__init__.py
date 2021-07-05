from support import configs
from support import strategies
from modules.database import Database
# from app.modules.mapper import Mapper
from app.modules.vortex import Vortex


def main():
    vortex = Vortex(configs)
    vortex.get_results()

    print(vortex.articles)  # Get address
    print(vortex.stats)

    stg = strategies.TELECONTACT_STRATEGY
    # print(stg)
    # for a in stg:
    #     key = a
    #     print(stg[key])


if __name__ == "__main__":
    main()
