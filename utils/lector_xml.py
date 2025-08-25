import xml.etree.ElementTree as ET
from modelos.campo import Campo
from modelos.estacion import Estacion
from modelos.sensor_suelo import SensorSuelo
from modelos.sensor_cultivo import SensorCultivo
from modelos.frecuencia import Frecuencia

def cargar_xml(ruta, lista_campos):
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        
        for campo_xml in root.findall("campo"):
            id_campo = campo_xml.get("id")
            nombre_campo = campo_xml.get("nombre")
            campo = Campo(id_campo, nombre_campo)
            print(f"➢ Cargando campo {id_campo} - {nombre_campo}")
            
            # Estaciones
            for est in campo_xml.find("estacionesBase").findall("estacion"):
                estacion = Estacion(est.get("id"), est.get("nombre"))
                campo.estaciones.insertar(estacion)
                print(f"   ➢ Creando estación base {estacion.id}")
            
            # Sensores de Suelo
            for sens in campo_xml.find("sensoresSuelo").findall("sensorS"):
                sensor = SensorSuelo(sens.get("id"), sens.get("nombre"))
                for freq in sens.findall("frecuencia"):
                    frecuencia = Frecuencia(freq.get("idEstacion"), freq.text.strip())
                    sensor.frecuencias.insertar(frecuencia)
                campo.sensores_suelo.insertar(sensor)
                print(f"   ➢ Creando sensor de suelo {sensor.id}")
            
            # Sensores de Cultivo
            for sens in campo_xml.find("sensoresCultivo").findall("sensorT"):
                sensor = SensorCultivo(sens.get("id"), sens.get("nombre"))
                for freq in sens.findall("frecuencia"):
                    frecuencia = Frecuencia(freq.get("idEstacion"), freq.text.strip())
                    sensor.frecuencias.insertar(frecuencia)
                campo.sensores_cultivo.insertar(sensor)
                print(f"   ➢ Creando sensor de cultivo {sensor.id}")
            
            lista_campos.insertar(campo)
        
        print("Archivo cargado con éxito.")
    
    except Exception as e:
        print(f"Error al cargar XML: {e}")
