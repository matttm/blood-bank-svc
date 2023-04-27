import os
import sys

class UtilityService:
    def __init__(self) -> None:
        pass
    @staticmethod
    def populate_config_from_environment(config_map):
        for var in config_map:
            tmp = os.environ.get(var)
            if tmp is None:
                print(f'Error: {var} is not defined')
                sys.exit()
            config_map[var] = tmp
