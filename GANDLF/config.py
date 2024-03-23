from validator import MyValidator 
from pydantic import BaseModel, validator
from typing import Optional

from typing import Union,List

class Model(BaseModel):
    dimension: Optional[int]

class PatchSize(BaseModel):
    patch_size: Union[int, float, List[Union[int, float]]]
    model: Model

    @validator('patch_size', pre=True)
    def preprocess_patch_size(cls, v):
        if isinstance(v, (int, float)):
            return [v]
        return v

    @validator('patch_size', pre=True)
    def handle_single_value_list(cls, v, values):
        if isinstance(v, list) and len(v) == 1:
            return [v[0]] * values.get('model').get('dimension')
        return v

    
    @validator('model', pre=True)
    def check_dimension(cls, v, values):
        if v.get('dimension') is None:
            v['dimension'] = len(values.get('patch_size', []))
        return v

    @validator('patch_size')
    def parse_patch_size(cls, v, values):
        return v




   



class MySchema:
    def __init__(self):
        self.schema = {
            'patch_size': {
                'type': ['integer', 'float','list'],
                'required': True,
                'minlength': 1,
                'maxlength': 3,
                'schema': {
                    'type': 'number',
                    'min': 1
                },
                'validator': MyValidator()._validate_patch_size
            },

            'modality':{
                'type': 'string', 'required': True, 'is_model': True

            },
            'loss_function':{
                'type':'dict',

            },

            'model': {
                'type': 'dict',
                'required': False,
                'schema': {
                    'dimension': {'type': 'integer', 'min': 1, 'max': 3}
                }
            }
        }
    
    def get_schema(self):

        return self.schema




