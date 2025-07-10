Este proyecto permite analizar las calificaciones de encuestas sobre distintos contenidos.
Se pueden agregar nuevas encuestas, visualizar todas las registradas e identificar cuáles tienen calificaciones bajas (≤ 2).
Estructura del proyecto
encuestas_bajas/
│
├── main.py                 # Script principal
├── analisis.py              # Funciones del programa
├── encuestas.json           # Base de datos en formato JSON
├── registros.log            # Archivo de logs
├── requirements.txt         # Librerías necesarias
└── README.md                # Documentación del proyecto
Librerías utilizadas
json (estándar de Python)

datetime (estándar de Python)

colorama (externa, para dar color a los textos)
Ejecucion
python -m venv venv
Instalar dependencias
pip install -r requirements.txt
Ejecutar el programa
python main.py
Zen de Python aplicado
"Simple es mejor que complejo."

El código está dividido en funciones simples y legibles, cada una con un único propósito.

Se aplican docstrings y buenas prácticas PEP8 para mantener claridad y orden.