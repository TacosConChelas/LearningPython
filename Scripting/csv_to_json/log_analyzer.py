"""
Script de análisis de logs de seguridad/honeypot.
Permite realizar múltiples tipos de análisis sobre archivos JSON generados desde CSV.

----> Análisis completo de todos los tipos
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --all

---> Análisis específicos
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --ips
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --countries
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --ports
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --protocols

---> Búsquedas específicas
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --search-country "Mexico"
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --search-protocol "HTTP"
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --search-ip "192.168.1.1"

---> Análisis temporal
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --temporal hour
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --temporal day

---> Guardar resultados en JSON
        python Scripting/csv_to_json/log_analyzer.py Mailoney-Logs_7nov.json --all --output resultados.json
"""

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import argparse


class LogAnalyzer:
    """Clase principal para analizar logs de seguridad."""
    
    def __init__(self, json_file: str):
        """
        Inicializa el analizador con un archivo JSON.
        
        Args:
            json_file: Ruta al archivo JSON con los logs
        """
        self.json_file = json_file
        self.data = self._load_data()
        self.ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
        self.internal_ip_pattern = re.compile(r'^(192\.168\.|10\.|172\.(1[6-9]|2[0-9]|3[0-1])\.)')
    
    def _load_data(self) -> List[Dict[str, Any]]:
        """Carga los datos del archivo JSON."""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: El archivo {self.json_file} no existe")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            sys.exit(1)
    
    def _extract_ips_from_value(self, value: Any) -> List[str]:
        """Extrae todas las IPs de un valor (puede ser string, número, etc.)."""
        if value is None:
            return []
        
        value_str = str(value)
        return self.ip_pattern.findall(value_str)
    
    def _is_internal_ip(self, ip: str) -> bool:
        """Verifica si una IP es interna."""
        return bool(self.internal_ip_pattern.match(ip))
    
    def analyze_ips(self) -> Dict[str, Any]:
        """
        Análisis por IP: extrae todas las IPs y las clasifica en internas/externas.
        
        Returns:
            Diccionario con estadísticas de IPs
        """
        ip_fields = [
            'host', 'src_ip', 'dest_ip', 'geoip.ip', 'geoip_ext.ip',
            't-pot_ip_ext', 't-pot_ip_int'
        ]
        
        all_ips = []
        internal_ips = []
        external_ips = []
        ip_occurrences = Counter()
        
        for record in self.data:
            for field in ip_fields:
                value = record.get(field)
                if value:
                    ips = self._extract_ips_from_value(value)
                    for ip in ips:
                        all_ips.append(ip)
                        ip_occurrences[ip] += 1
                        
                        if self._is_internal_ip(ip):
                            internal_ips.append(ip)
                        else:
                            external_ips.append(ip)
        
        return {
            'total_unique_ips': len(set(all_ips)),
            'total_occurrences': len(all_ips),
            'internal_unique': len(set(internal_ips)),
            'external_unique': len(set(external_ips)),
            'top_ips': dict(ip_occurrences.most_common(20)),
            'internal_ips': dict(Counter(internal_ips).most_common(10)),
            'external_ips': dict(Counter(external_ips).most_common(10))
        }
    
    def analyze_protocols(self) -> Dict[str, Any]:
        """
        Análisis por protocolo: analiza connection.protocol, connection.transport, etc.
        
        Returns:
            Diccionario con estadísticas de protocolos
        """
        protocol_fields = [
            'connection.protocol', 'connection.transport', 'connection.type',
            'headers.http_version', 'headers.request_method'
        ]
        
        protocols = Counter()
        transports = Counter()
        connection_types = Counter()
        http_versions = Counter()
        request_methods = Counter()
        
        for record in self.data:
            if record.get('connection.protocol'):
                protocols[record['connection.protocol']] += 1
            if record.get('connection.transport'):
                transports[record['connection.transport']] += 1
            if record.get('connection.type'):
                connection_types[record['connection.type']] += 1
            if record.get('headers.http_version'):
                http_versions[record['headers.http_version']] += 1
            if record.get('headers.request_method'):
                request_methods[record['headers.request_method']] += 1
        
        return {
            'protocols': dict(protocols.most_common()),
            'transports': dict(transports.most_common()),
            'connection_types': dict(connection_types.most_common()),
            'http_versions': dict(http_versions.most_common()),
            'request_methods': dict(request_methods.most_common())
        }
    
    def analyze_countries(self) -> Dict[str, Any]:
        """
        Análisis por país: extrae geoip.country_name y geoip_ext.country_name.
        
        Returns:
            Diccionario con estadísticas por país
        """
        countries = Counter()
        countries_ext = Counter()
        
        for record in self.data:
            country = record.get('geoip.country_name')
            if country:
                countries[country] += 1
            
            country_ext = record.get('geoip_ext.country_name')
            if country_ext:
                countries_ext[country_ext] += 1
        
        # Combinar ambos contadores
        all_countries = countries + countries_ext
        
        return {
            'by_country': dict(all_countries.most_common()),
            'top_countries': dict(all_countries.most_common(20)),
            'total_countries': len(all_countries)
        }
    
    def analyze_ports(self) -> Dict[str, Any]:
        """
        Análisis por puertos: analiza DestPort y src_port.
        
        Returns:
            Diccionario con estadísticas de puertos
        """
        dest_ports = Counter()
        src_ports = Counter()
        
        for record in self.data:
            dest_port = record.get('DestPort (dest_port)')
            if dest_port is not None:
                try:
                    port = int(dest_port)
                    dest_ports[port] += 1
                except (ValueError, TypeError):
                    pass
            
            src_port = record.get('src_port')
            if src_port is not None:
                try:
                    port = int(src_port)
                    src_ports[port] += 1
                except (ValueError, TypeError):
                    pass
        
        return {
            'dest_ports': dict(dest_ports.most_common(20)),
            'src_ports': dict(src_ports.most_common(20)),
            'total_unique_dest_ports': len(dest_ports),
            'total_unique_src_ports': len(src_ports)
        }
    
    def analyze_honeypot_types(self) -> Dict[str, Any]:
        """
        Análisis por tipo de honeypot: analiza Type (type) y type.keyword.
        
        Returns:
            Diccionario con estadísticas de tipos de honeypot
        """
        types = Counter()
        
        for record in self.data:
            honeypot_type = record.get('Type (type)') or record.get('type.keyword')
            if honeypot_type:
                types[honeypot_type] += 1
        
        return {
            'honeypot_types': dict(types.most_common()),
            'total_types': len(types)
        }
    
    def _parse_timestamp(self, timestamp_str: str) -> Optional[datetime]:
        """Intenta parsear un timestamp en diferentes formatos."""
        if not timestamp_str:
            return None
        
        formats = [
            "%b %d, %Y @ %H:%M:%S.%f",
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%dT%H:%M:%S.%f",
            "%Y-%m-%d %H:%M:%S",
            "%b %d, %Y @ %H:%M:%S"
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(timestamp_str, fmt)
            except ValueError:
                continue
        
        return None
    
    def analyze_temporal(self, group_by: str = 'hour') -> Dict[str, Any]:
        """
        Análisis temporal: agrupa por hora, día o mes.
        
        Args:
            group_by: 'hour', 'day', o 'month'
        
        Returns:
            Diccionario con estadísticas temporales
        """
        time_groups = Counter()
        timestamps = []
        
        for record in self.data:
            ts_str = record.get('@timestamp') or record.get('timestamp')
            if ts_str:
                dt = self._parse_timestamp(ts_str)
                if dt:
                    timestamps.append(dt)
                    
                    if group_by == 'hour':
                        key = dt.strftime('%Y-%m-%d %H:00')
                    elif group_by == 'day':
                        key = dt.strftime('%Y-%m-%d')
                    elif group_by == 'month':
                        key = dt.strftime('%Y-%m')
                    else:
                        key = dt.strftime('%Y-%m-%d %H:00')
                    
                    time_groups[key] += 1
        
        return {
            'group_by': group_by,
            'time_distribution': dict(time_groups.most_common()),
            'total_records_with_timestamp': len(timestamps),
            'earliest': min(timestamps).isoformat() if timestamps else None,
            'latest': max(timestamps).isoformat() if timestamps else None
        }
    
    def analyze_user_agents(self) -> Dict[str, Any]:
        """
        Análisis por User-Agent: extrae headers.http_user_agent.
        
        Returns:
            Diccionario con estadísticas de User-Agents
        """
        user_agents = Counter()
        
        for record in self.data:
            ua = record.get('headers.http_user_agent')
            if ua:
                user_agents[ua] += 1
        
        return {
            'user_agents': dict(user_agents.most_common(30)),
            'total_unique_agents': len(user_agents)
        }
    
    def analyze_asn(self) -> Dict[str, Any]:
        """
        Análisis por organización (ASN): analiza geoip.as_org y geoip_ext.as_org.
        
        Returns:
            Diccionario con estadísticas de organizaciones
        """
        as_orgs = Counter()
        asns = Counter()
        
        for record in self.data:
            org = record.get('geoip.as_org')
            if org:
                as_orgs[org] += 1
            
            org_ext = record.get('geoip_ext.as_org')
            if org_ext:
                as_orgs[org_ext] += 1
            
            asn = record.get('geoip.asn')
            if asn:
                asns[asn] += 1
            
            asn_ext = record.get('geoip_ext.asn')
            if asn_ext:
                # Limpiar formato "7,184" -> 7184
                try:
                    asn_clean = str(asn_ext).replace(',', '')
                    asns[int(asn_clean)] += 1
                except (ValueError, TypeError):
                    pass
        
        return {
            'organizations': dict(as_orgs.most_common(20)),
            'asns': dict(asns.most_common(20)),
            'total_organizations': len(as_orgs)
        }
    
    def analyze_http_headers(self) -> Dict[str, Any]:
        """
        Análisis de cabeceras HTTP: request_method, content_type, http_host.
        
        Returns:
            Diccionario con estadísticas de cabeceras HTTP
        """
        methods = Counter()
        content_types = Counter()
        hosts = Counter()
        
        for record in self.data:
            method = record.get('headers.request_method')
            if method:
                methods[method] += 1
            
            content_type = record.get('headers.content_type')
            if content_type:
                content_types[content_type] += 1
            
            host = record.get('headers.http_host')
            if host:
                hosts[host] += 1
        
        return {
            'request_methods': dict(methods.most_common()),
            'content_types': dict(content_types.most_common()),
            'http_hosts': dict(hosts.most_common(20))
        }
    
    def analyze_combined(self) -> Dict[str, Any]:
        """
        Análisis combinado: país + tipo de honeypot + puerto.
        
        Returns:
            Diccionario con estadísticas combinadas
        """
        combinations = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        
        for record in self.data:
            country = record.get('geoip.country_name') or record.get('geoip_ext.country_name') or 'Unknown'
            honeypot_type = record.get('Type (type)') or record.get('type.keyword') or 'Unknown'
            dest_port = record.get('DestPort (dest_port)')
            
            if dest_port is not None:
                try:
                    port = int(dest_port)
                    combinations[country][honeypot_type][port] += 1
                except (ValueError, TypeError):
                    pass
        
        # Convertir a formato más legible
        result = {}
        for country, types in combinations.items():
            result[country] = {}
            for htype, ports in types.items():
                result[country][htype] = dict(sorted(ports.items(), key=lambda x: x[1], reverse=True)[:10])
        
        return {
            'country_honeypot_port': result,
            'top_combinations': self._get_top_combinations(combinations)
        }
    
    def _get_top_combinations(self, combinations: Dict) -> List[Dict]:
        """Extrae las combinaciones más frecuentes."""
        flat = []
        for country, types in combinations.items():
            for htype, ports in types.items():
                for port, count in ports.items():
                    flat.append({
                        'country': country,
                        'honeypot_type': htype,
                        'port': port,
                        'count': count
                    })
        
        return sorted(flat, key=lambda x: x['count'], reverse=True)[:30]
    
    def search_by_country(self, country: str) -> List[Dict[str, Any]]:
        """
        Busca todos los registros relacionados con un país específico.
        
        Args:
            country: Nombre del país a buscar
        
        Returns:
            Lista de registros que coinciden
        """
        results = []
        country_lower = country.lower()
        
        for record in self.data:
            country_name = record.get('geoip.country_name') or record.get('geoip_ext.country_name')
            if country_name and country_lower in country_name.lower():
                results.append(record)
        
        return results
    
    def search_by_protocol(self, protocol: str) -> List[Dict[str, Any]]:
        """
        Busca todos los registros relacionados con un protocolo específico.
        
        Args:
            protocol: Protocolo a buscar (HTTP, TCP, SMTP, etc.)
        
        Returns:
            Lista de registros que coinciden
        """
        results = []
        protocol_lower = protocol.lower()
        
        for record in self.data:
            conn_protocol = record.get('connection.protocol')
            if conn_protocol and protocol_lower in str(conn_protocol).lower():
                results.append(record)
                continue
            
            transport = record.get('connection.transport')
            if transport and protocol_lower in str(transport).lower():
                results.append(record)
        
        return results
    
    def search_by_ip(self, ip: str) -> List[Dict[str, Any]]:
        """
        Busca todos los registros relacionados con una IP específica.
        
        Args:
            ip: IP a buscar
        
        Returns:
            Lista de registros que coinciden
        """
        results = []
        ip_fields = ['host', 'src_ip', 'dest_ip', 'geoip.ip', 'geoip_ext.ip', 
                     't-pot_ip_ext', 't-pot_ip_int']
        
        for record in self.data:
            for field in ip_fields:
                value = record.get(field)
                if value and ip in str(value):
                    results.append(record)
                    break
        
        return results


def print_analysis(title: str, data: Dict[str, Any], limit: int = None):
    """Imprime los resultados de un análisis de forma legible."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")
    
    if isinstance(data, dict):
        for key, value in list(data.items())[:limit] if limit else data.items():
            if isinstance(value, dict):
                print(f"{key}:")
                for subkey, subvalue in list(value.items())[:10]:
                    print(f"  {subkey}: {subvalue}")
                if len(value) > 10:
                    print(f"  ... y {len(value) - 10} más")
            elif isinstance(value, list):
                print(f"{key}:")
                for item in value[:10]:
                    print(f"  {item}")
                if len(value) > 10:
                    print(f"  ... y {len(value) - 10} más")
            else:
                print(f"{key}: {value}")
    else:
        print(data)


def main():
    """Función principal con interfaz de línea de comandos."""
    parser = argparse.ArgumentParser(
        description='Analizador de logs de seguridad/honeypot',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  # Análisis completo
  python log_analyzer.py logs.json --all
  
  # Análisis específico
  python log_analyzer.py logs.json --ips
  python log_analyzer.py logs.json --countries
  python log_analyzer.py logs.json --ports
  
  # Búsquedas
  python log_analyzer.py logs.json --search-country "Mexico"
  python log_analyzer.py logs.json --search-protocol "HTTP"
  python log_analyzer.py logs.json --search-ip "192.168.1.1"
  
  # Análisis temporal
  python log_analyzer.py logs.json --temporal hour
  python log_analyzer.py logs.json --temporal day
        """
    )
    
    parser.add_argument('json_file', help='Archivo JSON con los logs')
    parser.add_argument('--all', action='store_true', help='Realizar todos los análisis')
    parser.add_argument('--ips', action='store_true', help='Análisis por IP')
    parser.add_argument('--protocols', action='store_true', help='Análisis por protocolo')
    parser.add_argument('--countries', action='store_true', help='Análisis por país')
    parser.add_argument('--ports', action='store_true', help='Análisis por puertos')
    parser.add_argument('--honeypots', action='store_true', help='Análisis por tipo de honeypot')
    parser.add_argument('--temporal', choices=['hour', 'day', 'month'], help='Análisis temporal')
    parser.add_argument('--user-agents', action='store_true', help='Análisis por User-Agent')
    parser.add_argument('--asn', action='store_true', help='Análisis por organización (ASN)')
    parser.add_argument('--http-headers', action='store_true', help='Análisis de cabeceras HTTP')
    parser.add_argument('--combined', action='store_true', help='Análisis combinado (país+tipo+puerto)')
    parser.add_argument('--search-country', help='Buscar registros por país')
    parser.add_argument('--search-protocol', help='Buscar registros por protocolo')
    parser.add_argument('--search-ip', help='Buscar registros por IP')
    parser.add_argument('--output', help='Guardar resultados en archivo JSON')
    
    args = parser.parse_args()
    
    # Inicializar analizador
    analyzer = LogAnalyzer(args.json_file)
    print(f"Cargando {len(analyzer.data)} registros de {args.json_file}...")
    
    results = {}
    
    # Realizar análisis según los argumentos
    if args.all or not any([args.ips, args.protocols, args.countries, args.ports,
                           args.honeypots, args.temporal, args.user_agents, args.asn,
                           args.http_headers, args.combined, args.search_country,
                           args.search_protocol, args.search_ip]):
        # Si no se especifica nada, hacer análisis completo
        args.all = True
    
    if args.all or args.ips:
        results['ips'] = analyzer.analyze_ips()
        print_analysis("ANÁLISIS POR IP", results['ips'])
    
    if args.all or args.protocols:
        results['protocols'] = analyzer.analyze_protocols()
        print_analysis("ANÁLISIS POR PROTOCOLO", results['protocols'])
    
    if args.all or args.countries:
        results['countries'] = analyzer.analyze_countries()
        print_analysis("ANÁLISIS POR PAÍS", results['countries'])
    
    if args.all or args.ports:
        results['ports'] = analyzer.analyze_ports()
        print_analysis("ANÁLISIS POR PUERTOS", results['ports'])
    
    if args.all or args.honeypots:
        results['honeypots'] = analyzer.analyze_honeypot_types()
        print_analysis("ANÁLISIS POR TIPO DE HONEYPOT", results['honeypots'])
    
    if args.temporal:
        results['temporal'] = analyzer.analyze_temporal(args.temporal)
        print_analysis(f"ANÁLISIS TEMPORAL (por {args.temporal})", results['temporal'])
    
    if args.all or args.user_agents:
        results['user_agents'] = analyzer.analyze_user_agents()
        print_analysis("ANÁLISIS POR USER-AGENT", results['user_agents'])
    
    if args.all or args.asn:
        results['asn'] = analyzer.analyze_asn()
        print_analysis("ANÁLISIS POR ORGANIZACIÓN (ASN)", results['asn'])
    
    if args.all or args.http_headers:
        results['http_headers'] = analyzer.analyze_http_headers()
        print_analysis("ANÁLISIS DE CABECERAS HTTP", results['http_headers'])
    
    if args.all or args.combined:
        results['combined'] = analyzer.analyze_combined()
        print_analysis("ANÁLISIS COMBINADO (País + Tipo + Puerto)", results['combined'])
    
    # Búsquedas
    if args.search_country:
        search_results = analyzer.search_by_country(args.search_country)
        print_analysis(f"BÚSQUEDA POR PAÍS: {args.search_country}", {
            'total_results': len(search_results),
            'sample': search_results[:5]
        })
        results['search_country'] = {
            'query': args.search_country,
            'total_results': len(search_results),
            'results': search_results[:100]  # Limitar para no hacer el JSON muy grande
        }
    
    if args.search_protocol:
        search_results = analyzer.search_by_protocol(args.search_protocol)
        print_analysis(f"BÚSQUEDA POR PROTOCOLO: {args.search_protocol}", {
            'total_results': len(search_results),
            'sample': search_results[:5]
        })
        results['search_protocol'] = {
            'query': args.search_protocol,
            'total_results': len(search_results),
            'results': search_results[:100]
        }
    
    if args.search_ip:
        search_results = analyzer.search_by_ip(args.search_ip)
        print_analysis(f"BÚSQUEDA POR IP: {args.search_ip}", {
            'total_results': len(search_results),
            'sample': search_results[:5]
        })
        results['search_ip'] = {
            'query': args.search_ip,
            'total_results': len(search_results),
            'results': search_results[:100]
        }
    
    # Guardar resultados si se especifica
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False, default=str)
        print(f"\n✓ Resultados guardados en {args.output}")


if __name__ == "__main__":
    main()

