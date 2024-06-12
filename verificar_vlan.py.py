# Query: 
# ContextLines: 1

def verificar_vlan(vlan_id):
    """Verifica el rango de una VLAN y retorna su clasificación."""
    if 1 <= vlan_id <= 1005:
        return "VLAN de rango normal"
    elif 1006 <= vlan_id <= 4094:
        return "VLAN de rango extendido"
    else:
        return "VLAN fuera de rango"

def main():
    try:
        vlan_id = int(input("Ingrese el número de VLAN: "))
        resultado = verificar_vlan(vlan_id)
        print(resultado)
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
