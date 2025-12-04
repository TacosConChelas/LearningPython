# Ejecuta esto una sola vez para crear los archivos de tarea
def setup_files():
    # Archivo para el Ejercicio 1 (Logs)
    with open("server_logs.txt", "w") as f:
        f.write("[INFO] System boot started\n")
        f.write("[WARNING] High memory usage detected\n")
        f.write("[ERROR] Connection to DB failed\n")
        f.write("[INFO] User admin logged in\n")
        f.write("[ERROR] Timeout waiting for response\n")
        f.write("[INFO] Service heartbeat OK\n")
    
    # Archivo para el Ejercicio 2 (Configuración de Red)
    with open("router_config.conf", "w") as f:
        f.write("# Router Configuration File\n")
        f.write("\n") # Línea vacía
        f.write("hostname=CoreRouter01\n")
        f.write("# Interface settings below\n")
        f.write("interface=GigabitEthernet0/1\n")
        f.write("ip_address=192.168.1.1\n")
        f.write("\n")
        f.write("status=active")

if __name__ == "__main__":
    setup_files()
    print("Files created successfully!")