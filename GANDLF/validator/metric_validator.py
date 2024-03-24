class MetricValidator:
     
    @staticmethod
    def preprocess_metric(v):
        if v is None:
            return {}
        elif isinstance(v, str):
            return {v: {}}
        elif isinstance(v, dict):
            return v
        else:
            raise ValueError(f"Invalid format for metric configuration: {v}")
        
    @staticmethod
    def preprocess_classification_metrics(v):
        if v:
            v.setdefault('average', 'weighted')
            v.setdefault('multi_class', True)
            v.setdefault('mdmc_average', 'samplewise')
            v.setdefault('threshold', 0.5)
            if 'accuracy' in v:
                v.setdefault('subset_accuracy', False)
        return v
    
    @staticmethod
    def preprocess_iou_metric(v):
        if v:
            v.setdefault('reduction', 'elementwise_mean')
            v.setdefault('threshold', 0.5)
        return v

