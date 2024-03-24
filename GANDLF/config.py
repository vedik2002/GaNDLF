
from pydantic import BaseModel, validator
from typing import Optional,Union,List,Dict
from validator.loss_function_validator import LossFunctionValidator
from validator.patch_size_validator import PatchSizeValidator
from validator.model_validator import ModelValidator
from validator.metric_validator import MetricValidator


class Model(BaseModel):
    dimension: Optional[int]

class MetricsConfig(BaseModel):
    accuracy: Optional[Dict[str, bool]] = None
    f1: Optional[Dict[str, bool]] = None
    precision: Optional[Dict[str, bool]] = None
    recall: Optional[Dict[str, bool]] = None
    specificity: Optional[Dict[str, bool]] = None
    iou: Optional[Dict[str, str]] = None

    @validator('accuracy', 'f1', 'precision', 'recall', 'specificity', 'iou')
    def preprocess_metric(cls,v):
        return MetricValidator.preprocess_metric(v)

    @validator('accuracy', 'f1', 'precision', 'recall', 'specificity')
    def preprocess_classification_metrics(cls, v):
        return MetricValidator.preprocess_classification_metrics(v)

    @validator('iou')
    def preprocess_iou_metric(cls, v):
        return MetricValidator.preprocess_iou_metric(v)



class Params(BaseModel):
    patch_size: Union[int, float, List[Union[int, float]]]
    model: Model
    modality: str
    loss_function: Union[str, Dict[str, Union[Dict[str, Union[str, float]], None]]]
    metrics : MetricsConfig

    @validator('modality')
    def validate_modality(cls, v):
        assert v.lower() in ["rad", "histo", "path"], "Modality should be either 'rad' or 'path'"
        return v.lower()

    @validator('loss_function')
    def preprocess_loss_function(cls, v):
        return LossFunctionValidator.preprocess_loss_function(v)

    @validator('patch_size', pre=True)
    def preprocess_patch_size(cls, v):
        return PatchSizeValidator.preprocess_patch_size(v)

    @validator('patch_size', pre=True)
    def handle_single_value_list(cls, v, values):
        return PatchSizeValidator.handle_single_value_list(v, values)

    @validator('model', pre=True)
    def check_dimension(cls, v, values):
        return ModelValidator.check_dimension(v, values)

    @validator('patch_size')
    def parse_patch_size(cls, v, values):
        return PatchSizeValidator.parse_patch_size(v, values)
    
    @validator('metrics')
    def preprocess_metrics(cls,v):
        if not v:
            raise ValueError("'metrics' needs to be defined in the config file")
        return v