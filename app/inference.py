import numpy as np
from app.utils import preprocess_input

def run_inference(models, input_data):
    data = preprocess_input(input_data)

    embedded = models['embedder'].predict(data)
    encoded = models['encoder'].predict(embedded)
    watermarked = models['watermarking'].predict(encoded)
    decoded = models['decoder'].predict(watermarked)

    return {
        'embedded': embedded.tolist(),
        'encoded': encoded.tolist(),
        'watermarked': watermarked.tolist(),
        'decoded': decoded.tolist()
    }