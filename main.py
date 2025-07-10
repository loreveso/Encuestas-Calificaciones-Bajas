from analisis import (
    cargar_encuestas,
    guardar_encuestas,
    agregar_encuesta,
    obtener_calificaciones_bajas,
    registrar_log
)

ARCHIVO_ENCUESTAS = "encuestas.json"
ARCHIVO_LOG = "registro.log"
def mostrar_menu() -> None:
    """Muestra el menú principal."""
    print("\n--- MENÚ DE ENCUESTAS ---")
    print("1. Ver todas las encuestas")
    print("2. Agregar nueva encuesta")
    print("3. Mostrar calificaciones bajas")
    print("4. Salir")
def main() -> None:
    """Función principal que ejecuta el programa."""
    encuestas = cargar_encuestas(ARCHIVO_ENCUESTAS)

    while True:
        mostrar_menu()
        opcion = input("Seleccioná una opción (1-4): ")

        if opcion == "1":
            for encuesta in encuestas:
                print(f"[{encuesta['id']}] {encuesta['contenido']} - Calificación: {encuesta['calificacion']} - Fecha: {encuesta['fecha']}")

        elif opcion == "2":
            contenido = input("Ingresá el nombre del contenido: ")
            try:
                calificacion = int(input("Ingresá la calificación (1 a 5): "))
                if calificacion < 1 or calificacion > 5:
                    print(" La calificación debe estar entre 1 y 5.")
                    continue
                agregar_encuesta(encuestas, contenido, calificacion)
                registrar_log(ARCHIVO_LOG, f"Se agregó una encuesta: '{contenido}' con calificación {calificacion}")
                guardar_encuestas(ARCHIVO_ENCUESTAS, encuestas)
                print(" Encuesta agregada correctamente.")
            except ValueError:
                print(" La calificación debe ser un número.")

        elif opcion == "3":
            bajas = obtener_calificaciones_bajas(encuestas)
            if not bajas:
                print("No hay calificaciones bajas.")
            else:
                print(" Contenidos con calificación baja (1 o 2):")
                for encuesta in bajas:
                    print(f"[{encuesta['id']}] {encuesta['contenido']} - Calificación: {encuesta['calificacion']} - Fecha: {encuesta['fecha']}")

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print(" Opción inválida. Intentá de nuevo.")
if __name__ == "__main__":
    main()
