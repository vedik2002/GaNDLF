from cerberus import Validator
import yaml
from typing import Optional, Union

from config import MySchema
from validator import MyValidator
from config import PatchSize

def _parse_config(config_file_path: Union[str, dict]):

    params = config_file_path

    ###Reading yaml file #######
    if not isinstance(config_file_path,dict):
        params = yaml.safe_load(open(config_file_path,"r"))
    
    result = PatchSize(**params)
    print(result)

def ConfigManager(config_file_path: Union[str, dict]):

    return _parse_config(config_file_path=config_file_path)

ConfigManager("./example.yaml")





    



