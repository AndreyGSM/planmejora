import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import current_app

def configurar_cloudinary():
    """
    Configura Cloudinary usando las credenciales de la aplicación Flask.
    """
    cloudinary_url = current_app.config.get('CLOUDINARY_URL')
    if not cloudinary_url:
        raise ValueError("CLOUDINARY_URL no está configurada en las variables de entorno.")

    # Parsear las credenciales desde CLOUDINARY_URL
    cloud_name = cloudinary_url.split('@')[1]
    api_key = cloudinary_url.split('://')[1].split(':')[0]
    api_secret = cloudinary_url.split(':')[2].split('@')[0]

    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )

def subir_imagen(imagen, carpeta=None):
    """
    Sube una imagen a Cloudinary.

    Args:
        imagen: Un archivo de imagen (por ejemplo, request.files['archivo']).
        carpeta: (Opcional) La carpeta en Cloudinary donde se guardará la imagen.
    
    Returns:
        dict: Información sobre la imagen subida (incluyendo la URL).
    """
    configurar_cloudinary()

    # Opciones para Cloudinary
    opciones = {"folder": carpeta} if carpeta else {}
    
    try:
        resultado = cloudinary.uploader.upload(imagen, **opciones)
        return resultado
    except Exception as e:
        raise RuntimeError(f"Error al subir la imagen: {str(e)}")
