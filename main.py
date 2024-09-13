from data import AppHotel

# main
def main():
    app = AppHotel()  # Crear instancia de la clase AppHotel
    try:
        while True:
            print("\n" + "=" * 50)
            print("\t\tGESTIÓN DEL HOTEL")
            print("=" * 50)
            print("Menú Principal:")
            print("1. Clientes")
            print("2. Habitaciones")
            print("3. Reservas")
            print("4. Pagos")
            print("5. Salir")
            print("-" * 50)

            try:
                opcion = int(input("Escoja una opción (1-5): "))
            except ValueError:
                print("❌ Error: Por favor, ingrese un número válido.")
                continue

            if opcion == 1:
                print("\nOpciones de Clientes:")
                print("1. Registrar Cliente")
                print("2. Mostrar Clientes")
                try:
                    sub_opcion = int(input("Escoja una opción (1-2): "))
                except ValueError:
                    print("❌ Error: Por favor, ingrese un número válido.")
                    continue
                if sub_opcion == 1:
                    app.registrarCliente()
                elif sub_opcion == 2:
                    app.mostrarClientes()
                else:
                    print("❌ Opción no válida.")

            elif opcion == 2:
                print("\nOpciones de Habitaciones:")
                print("1. Registrar Habitación")
                print("2. Mostrar Habitaciones")
                try:
                    sub_opcion = int(input("Escoja una opción (1-2): "))
                except ValueError:
                    print("❌ Error: Por favor, ingrese un número válido.")
                    continue
                if sub_opcion == 1:
                    app.registrarHabitacion()
                elif sub_opcion == 2:
                    app.mostrarHabitaciones()
                else:
                    print("❌ Opción no válida.")

            elif opcion == 3:
                print("\nOpciones de Reservas:")
                print("1. Realizar Reserva")
                print("2. Mostrar Reservas")
                try:
                    sub_opcion = int(input("Escoja una opción (1-2): "))
                except ValueError:
                    print("❌ Error: Por favor, ingrese un número válido.")
                    continue
                if sub_opcion == 1:
                    app.realizarReserva()
                elif sub_opcion == 2:
                    app.mostrarReservas()
                else:
                    print("❌ Opción no válida.")

            elif opcion == 4:
                print("\nOpciones de Pagos:")
                print("1. Registrar Pago")
                print("2. Mostrar Pagos")
                try:
                    sub_opcion = int(input("Escoja una opción (1-2): "))
                except ValueError:
                    print("❌ Error: Por favor, ingrese un número válido.")
                    continue
                if sub_opcion == 1:
                    app.registrarPago()
                elif sub_opcion == 2:
                    app.mostrarPagos()
                else:
                    print("❌ Opción no válida.")

            elif opcion == 5:
                print("Saliendo...")
                break

            else:
                print("❌ Opción no válida.")
    except Exception as e:
        print(f"Se ha producido un error: {e}")
    finally:
        if app:
            app.cerrarConexion()

# Agregar bloque para que main sea el punto de entrada
if _name_ == "_main_":
    main()
