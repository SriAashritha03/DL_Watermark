from tensorflow.keras.models import load_model

def load_all_models():
    return {
        'watermarking': load_model('models/watermarking_model.h5'),
        'encoder': load_model('models/encode_model.h5'),
        'embedder': load_model('models/embedder_model.h5'),
        'decoder': load_model('models/decoder_model.h5')
    }