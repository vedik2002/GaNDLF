def preprocess_classification_metrics(cls, v):
        if v:
            v.setdefault('average', 'weighted')
            v.setdefault('multi_class', True)
            v.setdefault('mdmc_average', 'samplewise')
            v.setdefault('threshold', 0.5)
            if 'accuracy' in v:
                v.setdefault('subset_accuracy', False)
        return v