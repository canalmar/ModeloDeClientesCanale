import json
from typing import Any      #puede ser cualquier tipo

def load_json(filepath: str) ->list[Any]:
    """ Carga una lista de objetos desde un archivo JSON
    Devuelve la lista con datos del archivo o vacia si no existe """

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filepath}. Se creará uno nuevo al guardar.")
        return[]

    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {filepath}")
        return[]
    

def save_json(data:list[Any], filepath:str) ->None:
    """ Guarda una lista de objetos en un archivo JSON."""

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar en archivo JSON: {e}")