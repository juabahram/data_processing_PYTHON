# -*- coding: utf-8 -*-


from Tesla import * 
    
###########################################################################################

def TEST_leer_tesla():
    print ("leídos", len(TESLA), "datos.", "Los primeros 3 registros son:" , TESLA[:3], "Los últimos 3 son:" ,TESLA[-1],TESLA[-2], TESLA[-3])
    
###########################################################################################

def TEST_filtra_por_año():
    filtro= filtra_por_año(TESLA, 2016)
    print(filtro[:10])
    
    filtro2= filtra_por_año(TESLA, 2017)
    print(filtro2[:10])
    
###########################################################################################

def TEST_calcula_productos():
    lista= calcula_productos(TESLA)
    print(lista)
    
############################################################################################

def TEST_filtrar_por_cantidad_vendida():
    cantidad= filtrar_por_cantidad_vendida(TESLA, 20000000 )
    print(cantidad[:10])
    
    cantidad2= filtrar_por_cantidad_vendida(TESLA, 30000000 )
    print(cantidad2[:10])
############################################################################################

def TEST_calcular_numero_de_contratos():
    
    prod1='Electric Car\n'
    contratos1= calcular_numero_de_contratos(TESLA, prod1 )
    print("Leídos ", contratos1, " contratos activos para ", prod1 )
    
    prod2='House-Powering Battery\n'
    contratos2= calcular_numero_de_contratos(TESLA, prod2 )
    print("Leídos ", contratos2, " contratos activos para ", prod2 )
    
    
############################################################################################

def TEST_calcular_diferencia_precio():
    
    diferencia=calcular_diferencia_precio(TESLA, 2016)
    print(diferencia)
    
    diferencia2=calcular_diferencia_precio(TESLA, 2017)
    print(diferencia2)
    
############################################################################################

def TEST_calcular_beneficio_aproximado():
    cod=9000
    stonks=calcular_beneficio_aproximado(TESLA, cod)
    print("La acción con código ", cod,"recoge un beneficio aproximado de ", stonks, "unidades monetarias")
    
    cod2=8766
    stonks2=calcular_beneficio_aproximado(TESLA, cod2)
    print("La acción con código ", cod2,"recoge un beneficio aproximado de ", stonks2, "unidades monetarias")

############################################################################################

def TEST_calcular_precio_máximo():
    
    año1=2013
    high1=(calcular_precio_máximo(TESLA, año1))
    print("La acción que más cara salió al mercado en " , año1, "Tuvo un precio de: ", high1, "unidades monetarias")
    
    año2=2015
    high2=(calcular_precio_máximo(TESLA, año2))
    print("La acción que más cara salió al mercado en " , año2, "Tuvo un precio de: ", high2, "unidades monetarias")
    
############################################################################################

def TEST_calcular_precio_mínimo():
    
    año1=2013
    low1=(calcular_precio_mínimo(TESLA, año1))
    print("La acción que más barata salió al mercado en " , año1, "Tuvo un precio de: ", low1, "unidades monetarias")
    
    año2=2015
    low2=(calcular_precio_mínimo(TESLA, año2))
    print("La acción que más barata salió al mercado en " , año2, "Tuvo un precio de: ", low2, "unidades monetarias")

############################################################################################


def TEST_calcular_precios_más_altos():
    año1=2014
    top=calcular_precios_más_altos(TESLA, año1)
    print("El top 10 de precios más altos alcanzados en el año ", año1, "es: ",top)
    
    año2= 2016
    top1=calcular_precios_más_altos(TESLA, año2)
    print("El top 10 de precios más altos alcanzados en el año ", año2, "es: ",top1)
    
############################################################################################

def TEST_calcular_precios_más_bajos():
    año1=2014
    top=calcular_precios_más_altos(TESLA, año1)
    print("El top 10 de precios más bajos alcanzados en el año ", año1, "es: ",top)
    
    año2= 2016
    top1=calcular_precios_más_altos(TESLA, año2)
    print("El top 10 de precios más bajos alcanzados en el año ", año2, "es: ",top1)
    
############################################################################################


def TEST_productos_activos():
    
    d=2013
    otrodiccionariomás=[productos_activos(TESLA, d)]
    print("Aquí se muestra un diccionario agrupado por el tipo de producto en el año ", d, "cumpliendo la condición de estar activos ", otrodiccionariomás)
    
    d2=2016
    otrodiccionariomás=[productos_activos(TESLA, d2)]
    print("Aquí se muestra un diccionario agrupado por el tipo de producto en el año ", d2, "cumpliendo la condición de estar activos ", otrodiccionariomás)
    
###############################################################################################

def TEST_acc_rentables():
    
    d=2012
    diccionario=[acc_rentables(TESLA, d)]
    print("Esta función muestra un diccionario, agrupando las acciones cuya diferencia de valor más alto y bajo haya sido mayor que cero en el año ", d, diccionario)
    
    d2=2014
    diccionario=[acc_rentables(TESLA, d2)]
    print("Esta función muestra un diccionario, agrupando las acciones cuya diferencia de valor más alto y bajo haya sido mayor que cero en el año ", d2, diccionario)
        
#############################################################################################

def TEST_mostrar_precio_salida_por_año():
    mostrar_precio_salida_por_año(TESLA, 2015)
    
#############################################################################################

def TEST_mostrar_demanda_mercado():
    mostrar_demanda_mercado(TESLA, 2017)

##############################################################################################

if __name__ == '__main__':
    TESLA = leer_tesla('..\data\Tesla.csv')
    
    #TEST_leer_tesla()
    #TEST_filtra_por_año()
    #TEST_calcula_productos()
    #TEST_filtrar_por_cantidad_vendida()
    #TEST_calcular_numero_de_contratos()
    #TEST_calcular_diferencia_precio()
    #TEST_calcular_beneficio_aproximado()
    #TEST_calcular_precio_máximo()
    #TEST_calcular_precio_mínimo()
    #TEST_calcular_precios_más_altos()
    #TEST_calcular_precios_más_bajos()
    #TEST_productos_activos()
    #TEST_acc_rentables()
    #TEST_mostrar_precio_salida_por_año()
    #TEST_mostrar_demanda_mercado()
    
    
    
    
    
    
    
    
    
    
    
    
    
    