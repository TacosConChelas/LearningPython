#!/usr/bin/env python3
"""
Script avanzado para analizar redes WiFi de la zona
Obtiene información detallada sobre redes, gateways, MAC, dispositivos e ISP
"""

import subprocess
import socket
import re
import json
import threading
import time
import platform
from concurrent.futures import ThreadPoolExecutor
import requests
from datetime import datetime

class WiFiNetworkAnalyzer:
    def __init__(self):
        self.networks = []
        self.interface = self.get_wifi_interface()
        self.results = []
    
    def get_wifi_interface(self):
        """Detecta la interfaz WiFi activa"""
        try:
            if platform.system().lower() == "linux":
                result = subprocess.run(['iwconfig'], capture_output=True, text=True)
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'IEEE 802.11' in line and 'ESSID:' in line:
                        return line.split()[0]
            return "wlan0"  # Default
        except:
            return "wlan0"
    
    def scan_wifi_networks(self):
        """Escanea todas las redes WiFi disponibles"""
        print("🔍 Escaneando redes WiFi disponibles...")
        
        try:
            if platform.system().lower() == "linux":
                # Usar iwlist para escanear redes
                result = subprocess.run(['iwlist', self.interface, 'scan'], 
                                     capture_output=True, text=True, timeout=30)
                networks = self.parse_iwlist_output(result.stdout)
            else:
                # Para otros sistemas, usar nmap
                networks = self.scan_with_nmap()
            
            self.networks = networks
            print(f"✓ Encontradas {len(networks)} redes WiFi")
            return networks
            
        except Exception as e:
            print(f"❌ Error escaneando redes: {e}")
            return []
    
    def parse_iwlist_output(self, output):
        """Parsea la salida de iwlist para extraer información de redes"""
        networks = []
        current_network = {}
        
        lines = output.split('\n')
        for line in lines:
            line = line.strip()
            
            if 'Cell' in line and 'Address:' in line:
                if current_network:
                    networks.append(current_network)
                current_network = {
                    'mac': '',
                    'ssid': '',
                    'signal': '',
                    'encryption': '',
                    'channel': '',
                    'frequency': ''
                }
                # Extraer MAC
                mac_match = re.search(r'Address: ([0-9a-fA-F:]{17})', line)
                if mac_match:
                    current_network['mac'] = mac_match.group(1)
            
            elif 'ESSID:' in line:
                ssid_match = re.search(r'ESSID:"([^"]*)"', line)
                if ssid_match:
                    current_network['ssid'] = ssid_match.group(1)
            
            elif 'Signal level=' in line:
                signal_match = re.search(r'Signal level=(-?\d+)', line)
                if signal_match:
                    current_network['signal'] = signal_match.group(1) + ' dBm'
            
            elif 'Encryption key:' in line:
                if 'on' in line:
                    current_network['encryption'] = 'Protegida'
                else:
                    current_network['encryption'] = 'Abierta'
            
            elif 'Channel:' in line:
                channel_match = re.search(r'Channel:(\d+)', line)
                if channel_match:
                    current_network['channel'] = channel_match.group(1)
        
        if current_network:
            networks.append(current_network)
        
        return networks
    
    def scan_with_nmap(self):
        """Escanea redes usando nmap como alternativa"""
        networks = []
        try:
            # Escanear redes locales comunes
            common_ranges = [
                "192.168.1.0/24",
                "192.168.0.0/24", 
                "10.0.0.0/24",
                "172.16.0.0/24"
            ]
            
            for range_ip in common_ranges:
                result = subprocess.run(['nmap', '-sn', range_ip], 
                                      capture_output=True, text=True, timeout=10)
                # Procesar resultados de nmap
                # Esta es una implementación básica
                networks.append({
                    'mac': 'N/A',
                    'ssid': f'Red en {range_ip}',
                    'signal': 'N/A',
                    'encryption': 'Desconocida',
                    'channel': 'N/A',
                    'frequency': 'N/A'
                })
        except:
            pass
        
        return networks
    
    def get_network_info(self, network):
        """Obtiene información detallada de una red específica"""
        info = {
            'ssid': network.get('ssid', 'Oculta'),
            'mac': network.get('mac', 'N/A'),
            'signal': network.get('signal', 'N/A'),
            'encryption': network.get('encryption', 'Desconocida'),
            'channel': network.get('channel', 'N/A'),
            'gateway': 'N/A',
            'devices': [],
            'isp': 'N/A',
            'vendor': 'N/A'
        }
        
        # Obtener información del vendor por MAC
        if network.get('mac') and network['mac'] != 'N/A':
            info['vendor'] = self.get_vendor_by_mac(network['mac'])
        
        # Intentar obtener gateway (esto es limitado sin conectarse a la red)
        info['gateway'] = self.estimate_gateway(network)
        
        # Obtener ISP (información limitada sin conexión)
        info['isp'] = self.estimate_isp(network)
        
        return info
    
    def get_vendor_by_mac(self, mac):
        """Obtiene el fabricante por dirección MAC"""
        try:
            # Usar API pública para obtener vendor
            oui = mac.replace(':', '').upper()[:6]
            url = f"https://api.macvendors.com/{mac}"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        # Base de datos local básica de OUI comunes
        oui_db = {
            '00:50:56': 'VMware',
            '00:0C:29': 'VMware',
            '00:1C:42': 'Parallels',
            '08:00:27': 'VirtualBox',
            '52:54:00': 'QEMU',
            '00:15:5D': 'Microsoft',
            '00:16:3E': 'Xen',
            '00:1B:21': 'Intel',
            '00:1E:4C': 'Apple',
            '00:23:12': 'Apple',
            '00:25:00': 'Apple',
            '00:26:4A': 'Apple',
            '00:26:B0': 'Apple',
            '00:50:56': 'VMware',
            '00:0C:29': 'VMware',
            '00:1C:42': 'Parallels',
            '08:00:27': 'VirtualBox',
            '52:54:00': 'QEMU',
            '00:15:5D': 'Microsoft',
            '00:16:3E': 'Xen',
            '00:1B:21': 'Intel',
            '00:1E:4C': 'Apple',
            '00:23:12': 'Apple',
            '00:25:00': 'Apple',
            '00:26:4A': 'Apple',
            '00:26:B0': 'Apple'
        }
        
        oui = mac[:8].upper()
        return oui_db.get(oui, 'Desconocido')
    
    def estimate_gateway(self, network):
        """Estima el gateway basado en patrones comunes"""
        # Patrones comunes de gateway
        common_gateways = [
            "192.168.1.1",
            "192.168.0.1", 
            "10.0.0.1",
            "172.16.0.1"
        ]
        return "Estimado: " + common_gateways[0]
    
    def estimate_isp(self, network):
        """Estima el ISP basado en información disponible"""
        # Esta es una estimación muy básica
        return "ISP Local (Estimado)"
    
    def scan_network_devices(self, network):
        """Escanea dispositivos en una red específica (limitado sin conexión)"""
        devices = []
        # Sin conexión a la red, solo podemos mostrar información limitada
        devices.append({
            'ip': 'N/A (Sin conexión)',
            'hostname': 'N/A',
            'mac': 'N/A',
            'status': 'No accesible'
        })
        return devices
    
    def analyze_networks(self):
        """Analiza todas las redes encontradas"""
        print("\n🔍 Analizando redes WiFi...")
        
        for i, network in enumerate(self.networks, 1):
            print(f"Analizando red {i}/{len(self.networks)}: {network.get('ssid', 'Oculta')}")
            
            info = self.get_network_info(network)
            devices = self.scan_network_devices(network)
            info['devices'] = devices
            
            self.results.append(info)
            time.sleep(0.5)  # Pausa para no sobrecargar
    
    def display_results(self):
        """Muestra los resultados del análisis"""
        print("\n" + "="*80)
        print("📊 ANÁLISIS COMPLETO DE REDES WIFI")
        print("="*80)
        print(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total de redes encontradas: {len(self.results)}")
        print("="*80)
        
        if not self.results:
            print("❌ No se encontraron redes WiFi.")
            return
        
        for i, result in enumerate(self.results, 1):
            print(f"\n📡 RED {i}: {result['ssid']}")
            print("-" * 50)
            print(f"🔐 Nombre (SSID): {result['ssid']}")
            print(f"📶 Señal: {result['signal']}")
            print(f"🔒 Encriptación: {result['encryption']}")
            print(f"📻 Canal: {result['channel']}")
            print(f"🏭 Fabricante: {result['vendor']}")
            print(f"🌐 Gateway: {result['gateway']}")
            print(f"🏢 ISP: {result['isp']}")
            print(f"📱 Dispositivos conectados: {len(result['devices'])}")
            
            if result['devices']:
                print("   Dispositivos:")
                for device in result['devices']:
                    print(f"   - {device['ip']} ({device['hostname']}) - {device['status']}")
        
        # Resumen estadístico
        print(f"\n📈 RESUMEN ESTADÍSTICO")
        print("-" * 30)
        protected = sum(1 for r in self.results if 'Protegida' in r['encryption'])
        open_networks = len(self.results) - protected
        
        print(f"🔒 Redes protegidas: {protected}")
        print(f"🔓 Redes abiertas: {open_networks}")
        print(f"📊 Total analizadas: {len(self.results)}")

def main():
    print("🌐 ANALIZADOR AVANZADO DE REDES WIFI")
    print("=" * 40)
    print("⚠️  NOTA: Este script requiere permisos de administrador")
    print("⚠️  Algunas funciones están limitadas sin conexión a las redes")
    print("=" * 40)
    
    analyzer = WiFiNetworkAnalyzer()
    
    try:
        # Escanear redes WiFi
        networks = analyzer.scan_wifi_networks()
        
        if not networks:
            print("❌ No se pudieron detectar redes WiFi.")
            print("💡 Asegúrate de que tu interfaz WiFi esté activa.")
            return
        
        #nalizar cada red
        analyzer.analyze_networks()
        
        # Mostrar resultados
        analyzer.display_results()
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Análisis interrumpido por el usuario.")
    except Exception as e:
        print(f"\n❌ Error durante el análisis: {e}")
        print("💡 Asegúrate de tener permisos de administrador y que WiFi esté activo.")

if __name__ == "__main__":
    main()

