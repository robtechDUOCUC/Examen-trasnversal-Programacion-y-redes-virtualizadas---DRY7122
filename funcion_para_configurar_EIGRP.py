from netmiko import ConnectHandler


# Detalles de conexión SSH
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.138',
    'username': 'cisco',
    'password': 'cisco123!',
}


# Función para configurar EIGRP nombrado en IPv4 y IPv6
def configure_eigrp(sshCli, as_number):
    config_commands = [
        f'router eigrp {as_number}',
        'address-family ipv4 autonomous-system 100',
        'network 0.0.0.0',
        'passive-interface default',
        'no passive-interface Loopback0',
        'exit-address-family',
        'address-family ipv6 autonomous-system 100',
        'network ::/0',
        'passive-interface default',
        'no passive-interface Loopback0',
        'exit-address-family',
    ]
    output = sshCli.send_config_set(config_commands)
    print(f"Configurado EIGRP con AS {as_number}")


# Función para obtener información de las interfaces IP y estado
def show_ip_interface_brief(sshCli):
    output = sshCli.send_command("show ip interface brief")
    print(f"Estado y configuración de las interfaces IP:\n{output}\n")


# Función para obtener el show running-config
def show_running_config(sshCli):
    output = sshCli.send_command("show running-config")
    print(f"Configuración actual del dispositivo:\n{output}\n")


# Función para obtener el show version
def show_version(sshCli):
    output = sshCli.send_command("show version")
    print(f"Información de versión del dispositivo:\n{output}\n")


# Conexión SSH
sshCli = ConnectHandler(**device)


# Tarea 1: Configurar EIGRP nombrado
configure_eigrp(sshCli, 100)


# Tarea 2: Obtener información de las interfaces IP y estado
show_ip_interface_brief(sshCli)


# Tarea 3: Obtener el show running-config
show_running_config(sshCli)


# Tarea 4: Obtener el show version
show_version(sshCli)


# Cerrar la sesión SSH
sshCli.disconnect()