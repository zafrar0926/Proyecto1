# preprocessing.py
import tensorflow_transform as tft
import tensorflow as tf

# Declarar constantes: define cuáles son las columnas numéricas y categóricas.
NUMERIC_FEATURE_KEYS = ['Hillshade_9am', 'Hillshade_Noon', 'Slope']
CATEGORICAL_FEATURE_KEYS = ['Cover_Type']

def preprocessing_fn(inputs):
    """Función de preprocesamiento para transformar las características.
    
    Args:
        inputs: Diccionario con las columnas de características en su forma original.
    
    Returns:
        Diccionario con las características transformadas.
    """
    outputs = {}
    
    # Escalar características numéricas
    for key in NUMERIC_FEATURE_KEYS:
        outputs[key + '_scaled'] = tft.scale_to_z_score(inputs[key])
    
    # Convertir características categóricas en índices
    for key in CATEGORICAL_FEATURE_KEYS:
        outputs[key + '_indexed'] = tft.compute_and_apply_vocabulary(inputs[key])
    
    return outputs

