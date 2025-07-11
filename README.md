#  Gestor de Encuestas con Calificaciones Bajas

Este proyecto permite analizar las calificaciones de encuestas sobre distintos contenidos.  
Se pueden agregar nuevas encuestas, visualizar todas las registradas e identificar cuáles tienen calificaciones bajas (≤ 2).

---

##  Estructura del proyecto

encuestas_bajas/
├── main.py # Script principal
├── analisis.py # Funciones del programa
├── encuestas.json # Base de datos en formato JSON
├── registros.log # Archivo de logs
├── requirements.txt # Librerías necesarias
└── README.md # Documentación del proyecto


---

##  Librerías utilizadas

- `json` (estándar de Python)
- `datetime` (estándar de Python)
- `colorama` (externa, para dar color a los textos)

---

## ▶ Cómo ejecutar

### Crear entorno virtual:

```bash
python -m venv venv


---

##  Librerías utilizadas

- `json` (estándar de Python)
- `datetime` (estándar de Python)
- `colorama` (externa, para dar color a los textos)

---

## ▶ Cómo ejecutar

### Crear entorno virtual:

```bash
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python main.py

 Zen of Python aplicado
Se tomó como referencia el principio del Zen of Python:
"Simple es mejor que complejo", logrando un código claro y con pocas líneas por función, evitando la complejidad innecesaria.

 Uso del entorno virtual (venv)
Se creó y utilizó un entorno virtual (venv) para aislar las dependencias del proyecto.
Esto permite que otros puedan instalar las mismas versiones de las librerías utilizadas (ej: colorama) simplemente con el archivo requirements.txt.

 Contenido del archivo README.md
El archivo README.md incluye:

Descripción del proyecto y su propósito.

Estructura del proyecto.

Pasos claros para ejecutar el programa y crear el entorno virtual.

Detalle de las librerías usadas.

Ejemplo del menú interactivo del programa.

Buenas prácticas aplicadas.