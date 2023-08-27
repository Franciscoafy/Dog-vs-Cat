import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt



def cargar_imagenes(ruta_carpeta):
    imagenes = []
    extensiones_validas = ['.jpg', '.jpeg', '.png']  # Agrega las extensiones válidas
    for nombre_archivo in os.listdir(ruta_carpeta):
        if any(nombre_archivo.lower().endswith(ext) for ext in extensiones_validas):
            ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)
            imagen = Image.open(ruta_completa)
            imagen = imagen.resize((150, 150))  # Redimension a 150x150 píxeles
            arreglo_imagen = np.array(imagen) / 255.0  # Normaliza los valores de píxeles
            imagenes.append(arreglo_imagen)
    return imagenes