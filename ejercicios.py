"""
Actividad                                                   Factor
Sedentario (poca o ninguna actividad)	                    1.2
Ligero (ejercicio leve 1-3 días/semana)	                    1.375
Moderado (ejercicio moderado 3-5 días/semana)	            1.55
Activo (ejercicio intenso 6-7 días/semana)	                1.725
Muy activo (entrenamiento fuerte o trabajo físico intenso)	1.9


Objetivo            codigo
Bajar de peso       0
Mantener peso       1
Subir de peso       2
"""

def calcular_get(peso, altura, edad, sexo, actividad, objetivo):
    if sexo == 'H':
        tmb = (10*peso)+(6.25*altura)-(5*edad)+5
    else:
        tmb = (10*peso)+(6.25*altura)-(5*edad)-161
    
    if objetivo == 0:
        return (tmb * actividad) - 500

    if objetivo == 2:
        return (tmb * actividad) + 300
    
    return tmb * actividad

print(f"Las calorias necesarias para su objetivo son de: {calcular_get(70, 170, 26, 'H', 1.55, 1)}")

def dibujar_hola_mundo():
# Definir las letras de cada palabra
    letras_hola = {
        "H": ["*   *", "*   *", "*****", "*   *", "*   *"],
        "O": [" *** ", "*   *", "*   *", "*   *", " *** "],
        "L": ["*    ", "*    ", "*    ", "*    ", "*****"],
        "A": [" *****", "*     *", "*****", "*     *", "*     *"]
    }

    letras_mundo = {
        "M": ["*     *", "**   **", "* * * *", "*  *  *", "*     *"],
        "U": ["*     *", "*     *", "*     *", "*     *", " *****"],
        "N": ["*     *", "**    *", "* *   *", "*  *  *", "*   ** *"],
        "D": ["***** ", "*    *", "*    *", "*    *", "***** "],
        "O": [" *** ", "*   *", "*   *", "*   *", " *** "]
    }

    for i in range(5): 
        print(letras_hola["H"][i] + "  " + letras_hola["O"][i] + "  " + letras_hola["L"][i] + "  " + letras_hola["A"][i])

    print() 

    for i in range(5):  
        print(letras_mundo["M"][i] + "  " + letras_mundo["U"][i] + "  " + letras_mundo["N"][i] + "  " + letras_mundo["D"][i] + "  " + letras_mundo["O"][i])

dibujar_hola_mundo()


def calcular_get(peso, altura, edad, sexo, actividad, objetivo):
    """
    Calcula el Gasto Energético Total (GET) en función del peso, altura, edad, sexo, nivel de actividad y objetivo.

    Parámetros:
        peso (float): Peso en kg.
        altura (float): Altura en cm.
        edad (int): Edad en años.
        sexo (str): 'H' para hombre, 'M' para mujer.
        actividad (str): Clave del nivel de actividad.
        objetivo (str): Clave del objetivo ('bajar', 'mantener', 'subir').

    Retorna:
        float: Calorías diarias recomendadas.
    """

    # Factores de actividad
    factores_actividad = {
        "sedentario": 1.2,
        "ligero": 1.375,
        "moderado": 1.55,
        "activo": 1.725,
        "muy_activo": 1.9
    }

    # Ajustes calóricos según el objetivo
    ajuste_calorico = {
        "bajar": -500,
        "mantener": 0,
        "subir": 300
    }

    # Validación del sexo
    sexo = sexo.lower()
    if sexo not in ['h', 'm']:
        raise ValueError("El parámetro 'sexo' debe ser 'H' (hombre) o 'M' (mujer).")

    # Validación de actividad
    if actividad not in factores_actividad:
        raise ValueError(f"Nivel de actividad inválido. Opciones: {list(factores_actividad.keys())}")

    # Validación del objetivo
    if objetivo not in ajuste_calorico:
        raise ValueError(f"Objetivo inválido. Opciones: {list(ajuste_calorico.keys())}")

    # Cálculo de TMB (Tasa Metabólica Basal)
    if sexo == 'h':
        tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
    else:
        tmb = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

    # Cálculo de GET con ajuste por objetivo
    get = (tmb * factores_actividad[actividad]) + ajuste_calorico[objetivo]

    return round(get, 2)  # Redondear para mayor claridad


# Ejemplo de uso
peso = 70
altura = 170
edad = 26
sexo = "H"
actividad = "moderado"
objetivo = "mantener"

calorias = calcular_get(peso, altura, edad, sexo, actividad, objetivo)
print(f"Las calorías necesarias para su objetivo son: {calorias}")

import json
import re

class UserManager:
    def __init__(self):
        self.users = {}

    def agregar_usuario(self, id, nombre, correo):
        """Agrega un usuario si el ID no está repetido y el correo es válido."""
        if id in self.users:
            return {"error": "El ID ya existe."}

        if not self.validar_correo(correo):
            return {"error": "Correo inválido."}

        self.users[id] = {"nombre": nombre, "correo": correo}
        return {"mensaje": "Usuario agregado correctamente."}

    def eliminar_usuario(self, id):
        """Elimina un usuario por su ID si existe."""
        if id not in self.users:
            return {"error": "Usuario no encontrado."}

        del self.users[id]
        return {"mensaje": "Usuario eliminado correctamente."}

    def buscar_usuario(self, id):
        """Busca un usuario por su ID y lo retorna."""
        return self.users.get(id, {"error": "Usuario no encontrado."})

    def listar_usuarios(self):
        """Lista todos los usuarios ordenados alfabéticamente por nombre."""
        usuarios_ordenados = sorted(self.users.values(), key=lambda x: x["nombre"])
        return json.dumps(usuarios_ordenados, indent=4, ensure_ascii=False)

    @staticmethod
    def validar_correo(correo):
        """Valida que el correo tenga un formato válido usando regex."""
        patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(patron, correo) is not None

# Ejemplo de uso
gestor = UserManager()
print(gestor.agregar_usuario(1, "Carlos Pérez", "carlos@example.com"))
print(gestor.agregar_usuario(2, "Ana López", "ana_lopez@example.com"))
print(gestor.agregar_usuario(1, "Juan Torres", "juan@example.com"))  # Error ID duplicado
print(gestor.buscar_usuario(1))
print(gestor.eliminar_usuario(3))  # Error: Usuario no encontrado
print(gestor.listar_usuarios())

import hashlib

class SistemaAutenticacion:
    def __init__(self):
        self.usuarios = {}  # Diccionario para almacenar usuarios y contraseñas encriptadas

    def _hash_password(self, password):
        """Convierte la contraseña en un hash seguro usando SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def registrar_usuario(self, username, password):
        """Registra un nuevo usuario si no existe ya en la base de datos."""
        if username in self.usuarios:
            return "Error: El usuario ya está registrado."

        self.usuarios[username] = self._hash_password(password)
        return "Usuario registrado exitosamente."

    def iniciar_sesion(self, username, password):
        """Verifica si las credenciales son correctas y permite iniciar sesión."""
        if username not in self.usuarios:
            return "Error: Usuario no encontrado."

        if self.usuarios[username] == self._hash_password(password):
            return "Inicio de sesión exitoso. ¡Bienvenido!"
        else:
            return "Error: Contraseña incorrecta."

# Ejemplo de uso
auth = SistemaAutenticacion()

print(auth.registrar_usuario("jorge", "mi_contraseña_segura"))  # Registro exitoso
print(auth.registrar_usuario("jorge", "otra_contraseña"))       # Error: usuario ya registrado
print(auth.iniciar_sesion("jorge", "mi_contraseña_segura"))     # Inicio de sesión exitoso
print(auth.iniciar_sesion("jorge", "incorrecta"))               # Error: Contraseña incorrecta
print(auth.iniciar_sesion("juan", "1234"))                      # Error: Usuario no encontrado



#El problema de los numeros duplicados
"""
Tenemos una lista de numeros enteros donde cada numero aparece 2 veces exeptuando uno, la tarea del siguiente
algoritmo es encontrar el numero unico.

Para resolver este problema, podemos aprovechar la propiedad de los números XOR. El operador XOR (^) tiene la propiedad de que:

a ^ a = 0 (si un número se XOR con él mismo, da 0)
a ^ 0 = a (si un número se XOR con 0, da el mismo número)
Por lo tanto, si aplicamos XOR a todos los números de la lista, los que se repiten se cancelarán entre sí y el único número que quedará será el número que no tiene duplicados.
"""
def encontrar_unico(nums):
    unico = 0
    for num in nums:
        unico ^= num  # Aplicamos XOR a todos los elementos
    return unico

# Ejemplo de uso
nums = [4, 1, 2, 1, 2]
resultado = encontrar_unico(nums)
print(f"El número único es: {resultado}")
