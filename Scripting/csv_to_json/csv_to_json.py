"""
Script para convertir archivos CSV a formato JSON.
Facilita el análisis de datos de logs de seguridad/red.

---- > Convertir un archivo (genera archivo.json automáticamente)
        python Scripting/csv_to_json.py datos.csv

---- > Especificar archivo de salida
        python Scripting/csv_to_json.py datos.csv salida.json

---- > Convertir múltiples archivos
        python Scripting/csv_to_json.py archivo1.csv archivo2.csv archivo3.csv

---- > Guardar en directorio específico
        python Scripting/csv_to_json.py archivo1.csv archivo2.csv --output-dir ./json_output

---- > JSON compacto (sin indentación)
        python Scripting/csv_to_json.py datos.csv --no-pretty
"""

import csv
import json
import sys
import os
from pathlib import Path
from typing import List, Dict, Any


def clean_value(value: str) -> Any:
    """
    Limpia y convierte valores del CSV a tipos apropiados.
    Convierte strings vacíos a None y números a int/float cuando sea posible.
    """
    if value is None or value.strip() == '':
        return None
    
    value = value.strip()
    
    # Intentar convertir a número
    try:
        # Intentar int primero
        if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            return int(value)
    except ValueError:
        pass
    
    try:
        # Intentar float
        return float(value)
    except ValueError:
        pass
    
    # Si no es número, devolver string
    return value


def csv_to_json(csv_file_path: str, json_file_path: str = None, pretty: bool = True) -> List[Dict[str, Any]]:
    """
    Convierte un archivo CSV a formato JSON.
    
    Args:
        csv_file_path: Ruta al archivo CSV de entrada
        json_file_path: Ruta al archivo JSON de salida (opcional)
        pretty: Si True, formatea el JSON con indentación (por defecto True)
    
    Returns:
        Lista de diccionarios con los datos convertidos
    """
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"El archivo {csv_file_path} no existe")
    
    data = []
    
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            # Detectar delimitador automáticamente
            sample = csv_file.read(1024)
            csv_file.seek(0)
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(sample).delimiter
            
            reader = csv.DictReader(csv_file, delimiter=delimiter)
            
            for row in reader:
                # Limpiar valores vacíos y convertir tipos
                cleaned_row = {}
                for key, value in row.items():
                    # Limpiar nombres de columnas (eliminar espacios)
                    clean_key = key.strip() if key else key
                    cleaned_row[clean_key] = clean_value(value)
                
                data.append(cleaned_row)
    
    except Exception as e:
        raise Exception(f"Error al leer el archivo CSV: {str(e)}")
    
    # Guardar en archivo JSON si se especifica
    if json_file_path:
        try:
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                if pretty:
                    json.dump(data, json_file, indent=2, ensure_ascii=False)
                else:
                    json.dump(data, json_file, ensure_ascii=False)
            print(f"✓ Convertido: {csv_file_path} → {json_file_path}")
            print(f"  Registros procesados: {len(data)}")
        except Exception as e:
            raise Exception(f"Error al escribir el archivo JSON: {str(e)}")
    
    return data


def convert_multiple_files(csv_files: List[str], output_dir: str = None, pretty: bool = True):
    """
    Convierte múltiples archivos CSV a JSON.
    
    Args:
        csv_files: Lista de rutas a archivos CSV
        output_dir: Directorio de salida (opcional, por defecto mismo directorio)
        pretty: Si True, formatea el JSON con indentación
    """
    for csv_file in csv_files:
        if not os.path.exists(csv_file):
            print(f"⚠ Advertencia: {csv_file} no existe, se omite")
            continue
        
        # Generar nombre del archivo JSON de salida
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            base_name = Path(csv_file).stem
            json_file = os.path.join(output_dir, f"{base_name}.json")
        else:
            json_file = str(Path(csv_file).with_suffix('.json'))
        
        try:
            csv_to_json(csv_file, json_file, pretty)
        except Exception as e:
            print(f"✗ Error al procesar {csv_file}: {str(e)}")


def main():
    """
    Función principal que maneja argumentos de línea de comandos.
    """
    if len(sys.argv) < 2:
        print("Uso: python csv_to_json.py <archivo_csv> [archivo_json_salida]")
        print("   o: python csv_to_json.py <archivo_csv1> <archivo_csv2> ... [--output-dir <directorio>]")
        print("\nEjemplos:")
        print("  python csv_to_json.py datos.csv")
        print("  python csv_to_json.py datos.csv salida.json")
        print("  python csv_to_json.py archivo1.csv archivo2.csv --output-dir ./json_output")
        sys.exit(1)
    
    # Procesar argumentos
    args = sys.argv[1:]
    output_dir = None
    pretty = True
    
    # Buscar flag --output-dir
    if '--output-dir' in args:
        idx = args.index('--output-dir')
        if idx + 1 < len(args):
            output_dir = args[idx + 1]
            args = args[:idx] + args[idx + 2:]
    
    # Buscar flag --no-pretty
    if '--no-pretty' in args:
        pretty = False
        args.remove('--no-pretty')
    
    csv_files = [arg for arg in args if arg.endswith('.csv')]
    
    if not csv_files:
        print("Error: No se encontraron archivos CSV en los argumentos")
        sys.exit(1)
    
    # Si hay múltiples archivos o se especificó output_dir, usar convert_multiple_files
    if len(csv_files) > 1 or output_dir:
        convert_multiple_files(csv_files, output_dir, pretty)
    else:
        # Un solo archivo
        csv_file = csv_files[0]
        json_file = None
        
        # Verificar si el segundo argumento es un archivo JSON de salida
        if len(args) > 1 and args[1].endswith('.json'):
            json_file = args[1]
        else:
            # Generar nombre automáticamente
            json_file = str(Path(csv_file).with_suffix('.json'))
        
        try:
            csv_to_json(csv_file, json_file, pretty)
        except Exception as e:
            print(f"✗ Error: {str(e)}")
            sys.exit(1)


if __name__ == "__main__":
    main()

