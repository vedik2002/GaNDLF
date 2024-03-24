class LossFunctionValidator:
    
    @classmethod
    def preprocess_loss_function(cls, v):
        if isinstance(v, dict):
            for key in v:
                if key == "mse":
                    if v[key] is None or 'reduction' not in v[key]:
                        v[key] = {'reduction': 'mean'}
                else:
                    v = key
        else:
            if v == "mse":
                v = {'mse': {'reduction': 'mean'}}
            elif v == "focal":
                v = {'focal': {'gamma': 2.0, 'size_average': True}}
        return v