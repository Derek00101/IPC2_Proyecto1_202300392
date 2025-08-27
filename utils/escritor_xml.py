import xml.etree.ElementTree as ET

def escritor_xml(ruta, lista_campos):
    try:
        root = ET.Element("camposAgricolas")

        actual_campo = lista_campos.primero
        while actual_campo:
            campo = actual_campo.dato
            campo_elem = ET.SubElement(root, "campo", {
                "id": campo.id,
                "nombre": campo.nombre
            })

            # Estaciones reducidas
            estaciones_elem = ET.SubElement(campo_elem, "estacionesBaseReducidas")
            actual_est = campo.estaciones.primero
            while actual_est:
                est = actual_est.dato
                ET.SubElement(estaciones_elem, "estacion", {
                    "id": est.id,
                    "nombre": est.nombre
                })
                actual_est = actual_est.siguiente

            # Sensores de Suelo
            sensores_suelo_elem = ET.SubElement(campo_elem, "sensoresSuelo")
            actual_sensor = campo.sensores_suelo.primero
            while actual_sensor:
                sens = actual_sensor.dato
                sensor_elem = ET.SubElement(sensores_suelo_elem, "sensorS", {
                    "id": sens.id,
                    "nombre": sens.nombre
                })

                freq = sens.frecuencias.primero
                while freq:
                    f = freq.dato
                    ET.SubElement(sensor_elem, "frecuencia", {
                        "idEstacion": f.id_estacion
                    }).text = str(f.valor)
                    freq = freq.siguiente

                actual_sensor = actual_sensor.siguiente

            # Sensores de Cultivo
            sensores_cultivo_elem = ET.SubElement(campo_elem, "sensoresCultivo")
            actual_sensor = campo.sensores_cultivo.primero
            while actual_sensor:
                sens = actual_sensor.dato
                sensor_elem = ET.SubElement(sensores_cultivo_elem, "sensorT", {
                    "id": sens.id,
                    "nombre": sens.nombre
                })

                freq = sens.frecuencias.primero
                while freq:
                    f = freq.dato
                    ET.SubElement(sensor_elem, "frecuencia", {
                        "idEstacion": f.id_estacion
                    }).text = str(f.valor)
                    freq = freq.siguiente

                actual_sensor = actual_sensor.siguiente

            actual_campo = actual_campo.siguiente

        # Guardar archivo
        tree = ET.ElementTree(root)
        tree.write(ruta, encoding="utf-8", xml_declaration=True)
        print(f"Archivo XML de salida escrito en: {ruta}")

    except Exception as e:
        print(f"Error al escribir XML: {e}")
