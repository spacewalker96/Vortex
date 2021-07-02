from docopt import docopt
import logging

#import configs
from telecontact import config
#import helpers
from telecontact.telecontact import get_results



def main():
    print(get_results())
    # '''Entry point'''
    # args = docopt(__doc__,version="Telecontact Scraper 0.1")
    # if args["mine"]:
    #     config.QUERY_PARAMS["string"] = args["auto"]
    #     config.QUERY_PARAMS["ou"] = args["casablanca"]
    #     results,stats = get_results(config)
    #     logging.info(stats)
    #     if args["--file_path"]:
    #         if results:
    #             save_results(results,args["--file_path"])
    #     else:
    #         print(results)


if __name__=="__main__":
    main()