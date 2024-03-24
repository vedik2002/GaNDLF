def preprocess_metric(cls, v):
        if v is None:
            return {}
        elif isinstance(v, str):
            return {v: {}}
        elif isinstance(v, dict):
            return v
        else:
            raise ValueError(f"Invalid format for metric configuration: {v}")