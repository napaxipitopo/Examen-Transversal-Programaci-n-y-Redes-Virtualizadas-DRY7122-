# Solicitar al usuario un número de VLAN
try:
    vlan = int(input("Ingrese el número de VLAN: "))

    # Verificación del rango
    if 1 <= vlan <= 1005:
        print(f"La VLAN {vlan} pertenece al RANGO NORMAL.")
    elif 1006 <= vlan <= 4094:
        print(f"La VLAN {vlan} pertenece al RANGO EXTENDIDO.")
    elif vlan == 0 or vlan == 4095:
        print(f"La VLAN {vlan} es reservada y no se puede usar.")
    else:
        print("El número ingresado no es válido para una VLAN (rango permitido: 1-4094).")
except ValueError:
    print("Por favor ingrese un número entero válido.")
