class PatchSizeValidator:
    @classmethod
    def preprocess_patch_size(cls, v):
        if isinstance(v, (int, float)):
            return [v]
        return v

    @classmethod
    def handle_single_value_list(cls, v, values):
        if isinstance(v, list) and len(v) == 1:
            dimension = values.get('model').dimension
            if dimension is not None:
                return [v[0]] * dimension
        return v

    @classmethod
    def parse_patch_size(cls, v, values):
        return v