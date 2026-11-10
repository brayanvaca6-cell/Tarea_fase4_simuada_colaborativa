

#aca estamos basicamente creando el menu principal del sistema de gestion de reservas, aca se va a mostrar todo lo que se registro, clientes, servicios y reservas
if __name__ == "__main__":
#aca muestra unas lineas de separacion y un mensaje de bienvenida al sistema de gestion de reservas
        print("="*50)
        print("Bienvenido al sistema de gestión de reservas")
        print("="*50)
#aca inicia un bloque try para manejar posibles errores que puedan ocurrir durante la ejecución del código
        try:
#aca creamos una instancia de la clase sistemadegestion, que es la que va a manejar todo el sistema de reservas
                sistema = sistemadegestion()
#aca creamos el sistema de registro para clientes, muestra el titulo 
                print("\n---Registrando clientes---\n")
                c1 = cliente("12345", "Maria Gomez", "maria@example.com", "3102874391")
                c2 = cliente("67890", "Juan Perez", "juan@example.com", "3102874392")
#aca agregamos a maria y a juan en una lista de clientes dentro del sistema de gestion de reservas
                sistema.registrar_cliente(c1)
                sistema.registrar_cliente(c2)
#aca creamos el sistema de registro para servicios y tambien muestra el titulo de la seccion de servicios
                print("\n---Registrando servicios---\n")
                s1 = reservasala("sala de reuniones 1", "capacidad 10 personas", 30000,10)
                s2 = alquilerequipo("proyector", "equipo para expocisiones", 25000,5)
                s3 = asesoriaespecializada("asesoria en marketing", "asesoria para mejorar estrategias de marketing", 50000,4)
#aca agregamos los servicios que se registraron en una lista de servicios dentro del sistema de gestion de reservas
                sistema.registrar_servicio(s1)
                sistema.registrar_servicio(s2)
                sistema.registrar_servicio(s3)
#aca muestra el titulo de la seccion de reservas y crea 2 reservas, una para maria y otra para juan, con fechas especificas
                print("\n---Realizando reservas---\n")
                fecha1 = datetime(2026, 11, 10, 14, 0)
                fecha2 = datetime(2026, 11, 12, 9, 0)
#aca muestra un mensaje de que se esta realizando la reserva y luego llama a la funcion realizar_reserva para agregar las reservas a la lista de reservas dentro del sistema de gestion de reservas
                r1 = reserva(c1, s1, fecha1)
                r2 = reserva(c2, s3, fecha2)
#aca guardamos las dos reservas que se hicieron en la lista de reservas dentro del sistema de gestion de reservas
                sistema.realizar_reserva(r1)
                sistema.realizar_reserva(r2)
#aca mostramos la informacion de todo lo que se registro
                sistema.lista_clientes()
                sistema.lista_servicios()
                sistema.lista_reservas()
#aca manejamos los posibles errores que puedan ocurrir durante la ejecución del código, como errores de datos, errores de reserva, errores del sistema o errores inesperados
        except DatoInvalidoError as e:
         print(f"Error de datos: {e}")
        except ReservaInvalidaError as e:
         print(f"Error de reserva: {e}")
        except ErrorSistema as e:
         print(f"Error en el sistema: {e}")
        except Exception as e:
         print(f"Error inesperado: {e}")
#aca mostramos un mensaje de despedida al usuario y unas lineas de separacion
        print("\n" + "="*50)
        print("\nGracias por usar el sistema de gestión de reservas. ¡Hasta luego!")
        print("="*50)


        


                