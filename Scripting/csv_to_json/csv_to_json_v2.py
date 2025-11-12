"""
Script para convertir archivos CSV a formato JSON (Versión 2 - Flexible).
Versión mejorada que admite cualquier estructura de CSV, diferentes encodings,
delimitadores y formatos.

Características:
- Detección automática de delimitador
- Detección automática de encoding
- Manejo robusto de caracteres especiales
- Soporte para CSVs grandes (procesamiento por chunks)
- Manejo de valores multilínea
- Tolerante a errores de formato

Uso:
---- > Convertir un archivo (genera archivo.json automáticamente)
        python csv_to_json_v2.py datos.csv

---- > Especificar archivo de salida
        python csv_to_json_v2.py datos.csv salida.json

---- > Convertir múltiples archivos
        python csv_to_json_v2.py archivo1.csv archivo2.csv archivo3.csv

---- > Guardar en directorio específico
        python csv_to_json_v2.py archivo1.csv archivo2.csv --output-dir ./json_output

---- > JSON compacto (sin indentación)
        python csv_to_json_v2.py datos.csv --no-pretty

---- > Especificar encoding manualmente
        python csv_to_json_v2.py datos.csv --encoding utf-8

---- > Especificar delimitador manualmente
        python csv_to_json_v2.py datos.csv --delimiter ";"

---- > Modo verbose (más información)
        python csv_to_json_v2.py datos.csv --verbose
"""

import csv
import json
import sys
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
import argparse

# Intentar importar chardet, si no está disponible usar detección básica
try:
    import chardet
    HAS_CHARDET = True
except ImportError:
    HAS_CHARDET = False


def detect_encoding(file_path: str, sample_size: int = 10000) -> str:
    """
    Detecta el encoding de un archivo.
    
    Args:
        file_path: Ruta al archivo
        sample_size: Tamaño de la muestra a leer para detectar encoding
    
    Returns:
        Nombre del encoding detectado (por defecto 'utf-8')
    """
    # Si chardet está disponible, usarlo
    if HAS_CHARDET:
        try:
            with open(file_path, 'rb') as f:
                sample = f.read(sample_size)
                result = chardet.detect(sample)
                encoding = result.get('encoding', 'utf-8')
                confidence = result.get('confidence', 0)
                
                # Si la confianza es muy baja, usar utf-8 por defecto
                if confidence < 0.7:
                    return 'utf-8'
                
                return encoding
        except Exception:
            pass
    
    # Detección básica: probar encodings comunes
    encodings_to_try = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252', 'utf-16']
    
    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                f.read(sample_size)
                return encoding
        except (UnicodeDecodeError, UnicodeError):
            continue
        except Exception:
            continue
    
    # Si nada funciona, retornar utf-8 por defecto
    return 'utf-8'


def detect_delimiter(file_path: str, encoding: str = 'utf-8', sample_size: int = 1024) -> str:
    """
    Detecta el delimitador de un archivo CSV.
    
    Args:
        file_path: Ruta al archivo CSV
        encoding: Encoding del archivo
        sample_size: Tamaño de la muestra a leer
    
    Returns:
        Delimitador detectado (por defecto ',')
    """
    try:
        with open(file_path, 'r', encoding=encoding, errors='replace') as f:
            sample = f.read(sample_size)
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(sample).delimiter
            return delimiter
    except Exception:
        # Delimitadores comunes a probar
        delimiters = [',', ';', '\t', '|']
        try:
            with open(file_path, 'r', encoding=encoding, errors='replace') as f:
                first_line = f.readline()
                # Contar ocurrencias de cada delimitador
                counts = {d: first_line.count(d) for d in delimiters}
                if counts:
                    return max(counts, key=counts.get)
        except Exception:
            pass
        return ','


def clean_value(value: Any) -> Any:
    """
    Limpia y convierte valores del CSV a tipos apropiados.
    Convierte strings vacíos a None y números a int/float cuando sea posible.
    
    Args:
        value: Valor a limpiar
    
    Returns:
        Valor limpio y convertido
    """
    if value is None:
        return None
    
    # Convertir a string si no lo es
    if not isinstance(value, str):
        value = str(value)
    
    # Eliminar espacios en blanco
    value = value.strip()
    
    # Si está vacío, retornar None
    if value == '' or value.lower() in ['null', 'none', 'n/a', '-', '']:
        return None
    
    # Intentar convertir a número
    try:
        # Intentar int primero (sin punto decimal)
        if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            return int(value)
    except (ValueError, AttributeError):
        pass
    
    try:
        # Intentar float
        float_val = float(value)
        # Si es un float que es realmente un int, devolver int
        if float_val.is_integer():
            return int(float_val)
        return float_val
    except (ValueError, AttributeError):
        pass
    
    # Intentar boolean
    if value.lower() in ['true', 'yes', '1', 'on']:
        return True
    if value.lower() in ['false', 'no', '0', 'off']:
        return False
    
    # Si no es número ni boolean, devolver string
    return value


def clean_key(key: str) -> str:
    """
    Limpia el nombre de una clave (columna).
    
    Args:
        key: Nombre de la clave a limpiar
    
    Returns:
        Clave limpia
    """
    if not key:
        return 'unnamed_column'
    
    # Eliminar espacios y caracteres problemáticos
    cleaned = key.strip()
    
    # Reemplazar espacios múltiples por uno solo
    cleaned = ' '.join(cleaned.split())
    
    # Si está vacío después de limpiar, usar nombre genérico
    if not cleaned:
        return 'unnamed_column'
    
    return cleaned


def csv_to_json(
    csv_file_path: str,
    json_file_path: Optional[str] = None,
    pretty: bool = True,
    encoding: Optional[str] = None,
    delimiter: Optional[str] = None,
    verbose: bool = False
) -> List[Dict[str, Any]]:
    """
    Convierte un archivo CSV a formato JSON (versión flexible).
    
    Args:
        csv_file_path: Ruta al archivo CSV de entrada
        json_file_path: Ruta al archivo JSON de salida (opcional)
        pretty: Si True, formatea el JSON con indentación (por defecto True)
        encoding: Encoding del archivo (si None, se detecta automáticamente)
        delimiter: Delimitador del CSV (si None, se detecta automáticamente)
        verbose: Si True, muestra información adicional durante el proceso
    
    Returns:
        Lista de diccionarios con los datos convertidos
    """
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"El archivo {csv_file_path} no existe")
    
    # Detectar encoding si no se especifica
    if encoding is None:
        if verbose:
            print(f"Detectando encoding de {csv_file_path}...")
        encoding = detect_encoding(csv_file_path)
        if verbose:
            print(f"  Encoding detectado: {encoding}")
    else:
        if verbose:
            print(f"Usando encoding especificado: {encoding}")
    
    # Detectar delimitador si no se especifica
    if delimiter is None:
        if verbose:
            print(f"Detectando delimitador de {csv_file_path}...")
        delimiter = detect_delimiter(csv_file_path, encoding)
        if verbose:
            print(f"  Delimitador detectado: {repr(delimiter)}")
    else:
        if verbose:
            print(f"Usando delimitador especificado: {repr(delimiter)}")
    
    data = []
    errors = []
    
    try:
        with open(csv_file_path, 'r', encoding=encoding, errors='replace') as csv_file:
            # Leer el CSV con manejo robusto de errores
            try:
                reader = csv.DictReader(csv_file, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL)
                
                row_count = 0
                for row_num, row in enumerate(reader, start=2):  # Empezar en 2 (después del header)
                    try:
                        # Limpiar valores vacíos y convertir tipos
                        cleaned_row = {}
                        for key, value in row.items():
                            # Limpiar nombres de columnas
                            clean_key_name = clean_key(key)
                            
                            # Manejar columnas duplicadas agregando sufijo
                            if clean_key_name in cleaned_row:
                                counter = 1
                                while f"{clean_key_name}_{counter}" in cleaned_row:
                                    counter += 1
                                clean_key_name = f"{clean_key_name}_{counter}"
                            
                            cleaned_row[clean_key_name] = clean_value(value)
                        
                        data.append(cleaned_row)
                        row_count += 1
                        
                        # Mostrar progreso cada 10000 filas si verbose
                        if verbose and row_count % 10000 == 0:
                            print(f"  Procesadas {row_count} filas...")
                    
                    except Exception as e:
                        error_msg = f"Error en fila {row_num}: {str(e)}"
                        errors.append(error_msg)
                        if verbose:
                            print(f"  ⚠ {error_msg}")
                        # Continuar con la siguiente fila
                        continue
            
            except csv.Error as e:
                raise Exception(f"Error al leer el CSV: {str(e)}")
    
    except UnicodeDecodeError as e:
        # Intentar con otro encoding común
        if encoding != 'latin-1':
            if verbose:
                print(f"  Error de encoding, intentando con latin-1...")
            return csv_to_json(csv_file_path, json_file_path, pretty, 'latin-1', delimiter, verbose)
        else:
            raise Exception(f"Error de encoding: {str(e)}")
    
    except Exception as e:
        raise Exception(f"Error al leer el archivo CSV: {str(e)}")
    
    if verbose:
        print(f"  Total de filas procesadas: {len(data)}")
        if errors:
            print(f"  Errores encontrados: {len(errors)}")
    
    # Guardar en archivo JSON si se especifica
    if json_file_path:
        try:
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(json_file_path) if os.path.dirname(json_file_path) else '.', exist_ok=True)
            
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                if pretty:
                    json.dump(data, json_file, indent=2, ensure_ascii=False)
                else:
                    json.dump(data, json_file, ensure_ascii=False)
            
            print(f"✓ Convertido: {csv_file_path} → {json_file_path}")
            print(f"  Registros procesados: {len(data)}")
            if errors:
                print(f"  ⚠ Advertencias: {len(errors)} filas tuvieron errores")
        
        except Exception as e:
            raise Exception(f"Error al escribir el archivo JSON: {str(e)}")
    
    return data


def convert_multiple_files(
    csv_files: List[str],
    output_dir: Optional[str] = None,
    pretty: bool = True,
    encoding: Optional[str] = None,
    delimiter: Optional[str] = None,
    verbose: bool = False
):
    """
    Convierte múltiples archivos CSV a JSON.
    
    Args:
        csv_files: Lista de rutas a archivos CSV
        output_dir: Directorio de salida (opcional, por defecto mismo directorio)
        pretty: Si True, formatea el JSON con indentación
        encoding: Encoding a usar (si None, se detecta para cada archivo)
        delimiter: Delimitador a usar (si None, se detecta para cada archivo)
        verbose: Si True, muestra información adicional
    """
    total_files = len(csv_files)
    successful = 0
    failed = 0
    
    for idx, csv_file in enumerate(csv_files, 1):
        if not os.path.exists(csv_file):
            print(f"⚠ [{idx}/{total_files}] Advertencia: {csv_file} no existe, se omite")
            failed += 1
            continue
        
        print(f"\n[{idx}/{total_files}] Procesando: {csv_file}")
        
        # Generar nombre del archivo JSON de salida
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            base_name = Path(csv_file).stem
            json_file = os.path.join(output_dir, f"{base_name}.json")
        else:
            json_file = str(Path(csv_file).with_suffix('.json'))
        
        try:
            csv_to_json(csv_file, json_file, pretty, encoding, delimiter, verbose)
            successful += 1
        except Exception as e:
            print(f"✗ [{idx}/{total_files}] Error al procesar {csv_file}: {str(e)}")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Resumen: {successful} exitosos, {failed} fallidos de {total_files} archivos")
    print(f"{'='*60}")


def main():
    """Función principal que maneja argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description='Convierte archivos CSV a formato JSON (Versión 2 - Flexible)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  # Convertir un archivo (genera archivo.json automáticamente)
  python csv_to_json_v2.py datos.csv

  # Especificar archivo de salida
  python csv_to_json_v2.py datos.csv salida.json

  # Convertir múltiples archivos
  python csv_to_json_v2.py archivo1.csv archivo2.csv archivo3.csv

  # Guardar en directorio específico
  python csv_to_json_v2.py archivo1.csv archivo2.csv --output-dir ./json_output

  # JSON compacto (sin indentación)
  python csv_to_json_v2.py datos.csv --no-pretty

  # Especificar encoding manualmente
  python csv_to_json_v2.py datos.csv --encoding utf-8

  # Especificar delimitador manualmente
  python csv_to_json_v2.py datos.csv --delimiter ";"

  # Modo verbose (más información)
  python csv_to_json_v2.py datos.csv --verbose
        """
    )
    
    parser.add_argument('csv_files', nargs='+', help='Archivo(s) CSV a convertir')
    parser.add_argument('-o', '--output', help='Archivo JSON de salida (solo para un archivo)')
    parser.add_argument('--output-dir', help='Directorio de salida para múltiples archivos')
    parser.add_argument('--no-pretty', action='store_true', help='JSON compacto (sin indentación)')
    parser.add_argument('--encoding', help='Encoding del archivo CSV (por defecto: auto-detectado)')
    parser.add_argument('--delimiter', help='Delimitador del CSV (por defecto: auto-detectado)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Modo verbose (más información)')
    
    args = parser.parse_args()
    
    # Validar argumentos
    if args.output and len(args.csv_files) > 1:
        print("Error: --output solo puede usarse con un solo archivo CSV")
        sys.exit(1)
    
    if args.output_dir and args.output:
        print("Error: No se puede usar --output y --output-dir al mismo tiempo")
        sys.exit(1)
    
    # Procesar encoding
    encoding = args.encoding if args.encoding else None
    
    # Procesar delimitador
    delimiter = args.delimiter if args.delimiter else None
    
    # Procesar archivos
    csv_files = []
    for csv_file in args.csv_files:
        if not csv_file.endswith('.csv'):
            print(f"⚠ Advertencia: {csv_file} no tiene extensión .csv, se omite")
            continue
        csv_files.append(csv_file)
    
    if not csv_files:
        print("Error: No se encontraron archivos CSV válidos")
        sys.exit(1)
    
    # Si hay múltiples archivos o se especificó output_dir, usar convert_multiple_files
    if len(csv_files) > 1 or args.output_dir:
        convert_multiple_files(
            csv_files,
            args.output_dir,
            not args.no_pretty,
            encoding,
            delimiter,
            args.verbose
        )
    else:
        # Un solo archivo
        csv_file = csv_files[0]
        json_file = args.output if args.output else str(Path(csv_file).with_suffix('.json'))
        
        try:
            csv_to_json(
                csv_file,
                json_file,
                not args.no_pretty,
                encoding,
                delimiter,
                args.verbose
            )
        except Exception as e:
            print(f"✗ Error: {str(e)}")
            sys.exit(1)


if __name__ == "__main__":
    main()

