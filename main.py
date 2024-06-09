from typing import Counter
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    with open("listado.txt", "r") as datos:
        for linea in datos:
            datos = linea
            if datos[0] == "D":
                print(datos)
            break
    return "Hello from Flask!"


##if __name__ == '__main__':
#app.run(host='0.0.0.0', port=5000)
print("")
cont = 0
with open("listado.txt", "r") as datos:
    for linea in datos:
        datos = linea
        if datos[0] == "D":
            dni = datos[62:70]
            nombre = datos[175:224]
            appaterno = datos[75:124]
            apmaterno = datos[125:174]
            domicilio = datos[375:524].strip()
            monPago = datos[535:539]
            vencimientoanio = datos[565:572]
            vencimientomes = datos[554:560]
            vencimientodia = datos[565:572]
            
            print("DNI:",dni)
            print("Nombre:", nombre)
            print("Apellido Paterno:", appaterno)
            print("Apellido Materno:",apmaterno)
            print("Domicilio:", domicilio)
            print("Monto:", monPago)
            print("Vencimiento:", vencimientoanio)
            print("-----------------------------")

            break
            #cont += 1
            #if cont == 10:
            #    break

@app.route('/api/listado', methods=['GET'])
def obtener_listado():
    datos = []
    with open("listado.txt", "r") as archivo:
        for linea in archivo:
            uuu = linea
            if uuu[0] == "D":
                nombreCompleto = uuu[224:374].strip()
                dni = uuu[62:73]
                montoPago = uuu[535:539]
                fechaPago1 = uuu[542:546]
                fechaPago2 = uuu[546:548]
                datos.append({
                    'nombre': nombreCompleto,
                    'dni': dni,
                    'montoPago': montoPago,
                    'fechaPago': f"{fechaPago2}/{fechaPago1}"
                })
    datos = datos[:10]
    return jsonify(datos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)