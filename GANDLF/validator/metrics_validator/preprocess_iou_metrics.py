def preprocess_iou_metric(cls, v):
        if v:
            v.setdefault('reduction', 'elementwise_mean')
            v.setdefault('threshold', 0.5)
        return v