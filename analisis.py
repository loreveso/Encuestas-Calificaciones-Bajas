import json
from typing import List, Dict
from datetime import datetime
def cargar_encuestas(archivo: str) -> List[Dict]:
    """
    Carga las encuestas desde un archivo JSON.
    
    Args:
        archivo (str): Ruta del archivo JSON.
    
    Returns:
        List[Dict]: Lista de encuestas cargadas.
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Si no existe el archivo, devolvemos una lista vacía.
def guardar_encuestas(archivo: str, encuestas: List[Dict]) -> None:
    """
    Guarda las encuestas en un archivo JSON.
    
    Args:
        archivo (str): Ruta del archivo JSON.
        encuestas (List[Dict]): Lista de encuestas.
    """
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(encuestas, f, indent=4, ensure_ascii=False)
def agregar_encuesta(encuestas: List[Dict], contenido: str, calificacion: int) -> None:
    """
    Agrega una nueva encuesta a la lista.

    Args:
        encuestas (List[Dict]): Lista actual de encuestas.
        contenido (str): Nombre o tema del contenido evaluado.
        calificacion (int): Calificación entre 1 y 5.
    """
    nueva_encuesta = {
        "id": len(encuestas) + 1,
        "contenido": contenido,
        "calificacion": calificacion,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    encuestas.append(nueva_encuesta)
def obtener_calificaciones_bajas(encuestas: List[Dict]) -> List[Dict]:
    """
    Obtiene las encuestas con calificaciones bajas (1 o 2).

    Args:
        encuestas (List[Dict]): Lista de encuestas.

    Returns:
        List[Dict]: Lista filtrada con las encuestas bajas.
    """
    return [encuesta for encuesta in encuestas if encuesta["calificacion"] <= 2]
def registrar_log(archivo_log: str, accion: str) -> None:
    """
    Registra una acción en el archivo de logs.

    Args:
        archivo_log (str): Ruta del archivo de logs.
        accion (str): Mensaje descriptivo de la acción realizada.
    """
    with open(archivo_log, 'a', encoding='utf-8') as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {accion}\n")
