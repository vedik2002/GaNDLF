class ModelValidator:
    @classmethod
    def check_dimension(cls, v, values):
        if v.get('dimension') is None:
            v['dimension'] = len(values.get('patch_size', []))
        return v