#!/usr/bin/env python3
"""
Script para detectar hosts conectados en la red local
y obtener información como MAC e IPv4
"""

import subprocess
import socket
import re
import platform
import threading
from concurrent.futures import ThreadPoolExecutor
import time

class NetworkScanner:
    def __init__(self):
        self.hosts = []
        self.local_ip = self.get_local_ip()
        self.network = self.get_network_range()
    
    def get_local_ip(self):
        """Obtiene la IP local de la máquina"""
        try:
            # Conecta a una dirección externa para determinar la IP local
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except:
            return "127.0.0.1"
    
    def get_network_range(self):
        """Obtiene el rango de red basado en la IP local"""
        ip_parts = self.local_ip.split('.')
        return f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"
    
    def ping_host(self, ip):
        """Hace ping a una IP específica"""
        try:
            if platform.system().lower() == "windows":
                result = subprocess.run(['ping', '-n', '1', '-w', '1000', ip], 
                                      capture_output=True, text=True, timeout=3)
            else:
                result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], 
                                      capture_output=True, text=True, timeout=3)
            return result.returncode == 0
        except:
            return False
    
    def get_mac_address(self, ip):
        """Obtiene la dirección MAC de una IP"""
        try:
            if platform.system().lower() == "windows":
                result = subprocess.run(['arp', '-a', ip], capture_output=True, text=True)
            else:
                result = subprocess.run(['arp', '-n', ip], capture_output=True, text=True)
            
            # Buscar MAC en la salida
            mac_pattern = r'([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})'
            match = re.search(mac_pattern, result.stdout)
            if match:
                return match.group(0)
            return "No encontrada"
        except:
            return "Error"
    
    def get_hostname(self, ip):
        """Obtiene el hostname de una IP"""
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except:
            return "Desconocido"
    
    def scan_ip(self, ip):
        """Escanea una IP individual"""
        if self.ping_host(ip):
            mac = self.get_mac_address(ip)
            hostname = self.get_hostname(ip)
            self.hosts.append({
                'ip': ip,
                'mac': mac,
                'hostname': hostname,
                'status': 'Activo'
            })
            print(f"✓ Host encontrado: {ip} - {hostname}")
    
    def scan_network(self):
        """Escanea toda la red"""
        print(f"Escaneando red: {self.network}")
        print(f"IP local: {self.local_ip}")
        print("-" * 50)
        
        # Generar lista de IPs a escanear
        base_ip = self.network.split('/')[0]
        ip_parts = base_ip.split('.')
        
        # Usar ThreadPoolExecutor para escaneo paralelo
        with ThreadPoolExecutor(max_workers=50) as executor:
            for i in range(1, 255):
                ip = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{i}"
                executor.submit(self.scan_ip, ip)
        
        # Esperar un poco para que terminen los pings
        time.sleep(2)
    
    def display_results(self):
        """Muestra los resultados del escaneo"""
        print("\n" + "="*60)
        print("RESULTADOS DEL ESCANEO DE RED")
        print("="*60)
        
        if not self.hosts:
            print("No se encontraron hosts activos en la red.")
            return
        
        print(f"{'IP':<15} {'MAC':<18} {'Hostname':<20} {'Estado'}")
        print("-" * 60)
        
        for host in sorted(self.hosts, key=lambda x: socket.inet_aton(x['ip'])):
            print(f"{host['ip']:<15} {host['mac']:<18} {host['hostname']:<20} {host['status']}")
        
        print(f"\nTotal de hosts encontrados: {len(self.hosts)}")

def main():
    print("🔍 ESCÁNER DE RED LOCAL")
    print("=" * 30)
    
    scanner = NetworkScanner()
    
    try:
        scanner.scan_network()
        scanner.display_results()
    except KeyboardInterrupt:
        print("\n\nEscaneo interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError durante el escaneo: {e}")

if __name__ == "__main__":
    main()
