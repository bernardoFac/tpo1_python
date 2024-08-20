import random
# Generar cantidad random de clientes por rubro
clientes_residencial = random.randint(20, 200)
clientes_comercio = random.randint(20, 200)
clientes_pymes = random.randint(20, 200)
clientes_industria = random.randint(20, 200)
clientes_estatal = random.randint(20, 200)
#fijar costos
costos = [3, 5, 7, 10, 6]
#fijar precios
precios_fijos = [750, 1500, 3000, 7500, 3500]
precios_adicional_1 = [60.5, 70.5, 80, 100, 30.5]
precios_adicional_2 = [150, 160, 250, 300, 100]

# Generando el consumo random por cliente

def consumoCli(clientes):
    consumo = []
    for i in range(clientes):
        consu = random.randint(300, 3000)
        consumo.append(consu)
    return consumo

consumo_residencial = consumoCli(clientes_residencial)
consumo_comercio = consumoCli(clientes_comercio)
consumo_pymes = consumoCli(clientes_pymes)
consumo_industria = consumoCli(clientes_industria)
consumo_estatal = consumoCli(clientes_estatal)

# Generando el costo por cliente

def generar_costo(consumos, costos):
    costes = []
    for i in range(len(consumos)):
        costitos = consumos[i] * costos
        costes.append(costitos)
    return costes

def calcularCostos(costos):
    total = 0
    for i in range(len(costos)):
        total += costos[i]
    return total

costos_residencial = generar_costo(consumo_residencial, costos[0])
costos_comercio = generar_costo(consumo_comercio, costos[1])
costos_pymes = generar_costo(consumo_pymes, costos[2])
costos_industria = generar_costo(consumo_industria, costos[3])
costos_estatal = generar_costo(consumo_estatal, costos[4])

# Generando la facturacion por cada uno de los clientes

def generar_facturacion(consumos,precios_fijos,precios_adicional1,precios_adicional2):
    facturacion=[]
    for consumo in consumos:
        if consumo <=500:
           facturacion.append(precios_fijos)
        elif consumo>500 and consumo <=2000:
            facturacion.append(precios_fijos+precios_adicional1*consumo)
        else:
            facturacion.append(precios_fijos+precios_adicional2*consumo)
    return facturacion   

# Función para el total de la facturación

def calculo_facturacion(facturas):
    total = 0
    for i in range(len(facturas)):
        total += facturas[i]
    return total

fact_residencial = generar_facturacion(consumo_residencial, precios_fijos[0], precios_adicional_1[0], precios_adicional_2[0])
fact_comercio = generar_facturacion(consumo_comercio, precios_fijos[1], precios_adicional_1[1], precios_adicional_2[1])
fact_pymes = generar_facturacion(consumo_pymes, precios_fijos[2], precios_adicional_1[2], precios_adicional_2[2])
fact_industria = generar_facturacion(consumo_industria, precios_fijos[3], precios_adicional_1[3], precios_adicional_2[3])
fact_estatal = generar_facturacion(consumo_estatal, precios_fijos[4], precios_adicional_1[4], precios_adicional_2[4])

facturacion_tipos = [calculo_facturacion(fact_pymes), calculo_facturacion(fact_residencial), calculo_facturacion(fact_comercio), calculo_facturacion(fact_industria), calculo_facturacion(fact_estatal)]
costos_tipos = [calcularCostos(costos_pymes), calcularCostos(costos_residencial), calcularCostos(costos_comercio), calcularCostos(costos_industria), calcularCostos(costos_estatal)]
cantidad_clientes = [clientes_pymes, clientes_residencial, clientes_comercio, clientes_industria, clientes_estatal]
tipos_clientes = ['pymes', 'residencial', 'comercio', 'industria', 'estatal']

# OBJETIVO 2

facturacion_costos_clientes = []

for i in range(len(tipos_clientes)):
    facturacion_costos_clientes.append([facturacion_tipos[i], costos_tipos[i], cantidad_clientes[i], tipos_clientes[i]])

def ordenarListaSecuencial(lista):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[j][0] < lista[i][0]:  
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

facturacion_ordenada = ordenarListaSecuencial(facturacion_costos_clientes)

# OBJETIVO 3

lista_clientes = []

for i in range(clientes_pymes):
    lista_clientes.append(('Pyme', consumo_pymes[i], fact_pymes[i]))
for i in range(clientes_residencial):
    lista_clientes.append(('Residencial', consumo_residencial[i], fact_residencial[i]))
for i in range(clientes_comercio):
    lista_clientes.append(('Comercio', consumo_comercio[i], fact_comercio[i]))
for i in range(clientes_industria):
    lista_clientes.append(('Industria', consumo_industria[i], fact_industria[i]))
for i in range(clientes_estatal):
    lista_clientes.append(('Estatal', consumo_estatal[i], fact_estatal[i]))

def ordenarListaClientes(lista_clientes):
    for i in range(len(lista_clientes) - 1):
        for j in range(i + 1, len(lista_clientes)):
            if lista_clientes[j][2] < lista_clientes[i][2]:
                aux = lista_clientes[i]
                lista_clientes[i] = lista_clientes[j]
                lista_clientes[j] = aux
    return lista_clientes
lista_clientes = ordenarListaClientes(lista_clientes)

# OBJETIVO 4

def mostrar_clientes_por_tipo(tipo_cliente, lista_clientes):
    print(f"\nClientes de tipo {tipo_cliente}:")
    for cliente in lista_clientes:
        if cliente[0] == tipo_cliente:
            print(f"Tipo: {cliente[0]}, Consumo: {cliente[1]}, Facturación: ${cliente[2]}")

# Menú principal

bandera=True

while bandera:
    print("\nMenú Principal")
    print("1. Total de la facturación del mes, cantidad de clientes y el costo")
    print("2. Total de facturación por tipo de cliente")
    print("3. Listado completo detallado del total facturado de todos los clientes")
    print("4. Lista de facturación por tipo de cliente")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        fact_total = calculo_facturacion(fact_pymes) + calculo_facturacion(fact_residencial) + calculo_facturacion(fact_comercio) + calculo_facturacion(fact_estatal) + calculo_facturacion(fact_industria)
        print("\nLa facturación total del mes es de: $",fact_total)
        total_clientes = clientes_comercio + clientes_estatal + clientes_industria + clientes_pymes + clientes_residencial
        print("El total de clientes que tuvimos este mes es:", total_clientes)
        total_costos = calcularCostos(costos_pymes) + calcularCostos(costos_comercio) + calcularCostos(costos_estatal) + calcularCostos(costos_industria) + calcularCostos(costos_residencial)
        print("El costo total que tuvimos este mes fue de:", total_costos)
    
    elif opcion == "2":
        def imprimir(facturacion_ordenada):
            for i in range(len(facturacion_ordenada)):
                print(f"\nTipo de clientes: {facturacion_ordenada[i][3]}\n Facturación: ${facturacion_ordenada[i][0]}\n Costos: {facturacion_ordenada[i][1]}\n Cantidad clientes: {facturacion_ordenada[i][2]}\n")
        imprimir(facturacion_ordenada)

    elif opcion == "3":
        print("\nLista completa del total facturado por cliente, ordenado de menor a mayor:")
        for detalle in lista_clientes:
            tipo, consumo, facturacion = detalle
            print("Tipo:", tipo, "| Consumo:", consumo, "| Facturación: $", facturacion)
            
    elif opcion == "4":
        opcion_clientes = input("Escriba el tipo de cliente que se requiera tal como se muestra en pantalla: Pyme, Estatal, Comercio, Industria o Residencial\n")
        mostrar_clientes_por_tipo(opcion_clientes, lista_clientes)
        
    elif opcion == "5" or opcion == "Salir":
        print("Se finalizó el programa. Muchas gracias")
        bandera = False
        
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")