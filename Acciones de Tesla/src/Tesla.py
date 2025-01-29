# -*- coding: utf-8 -*-

import csv
from collections import namedtuple
from _datetime import datetime
import matplotlib
from matplotlib import pyplot as plt

Acciones = namedtuple('Acciones', 'code, date, open, high, low, close, volume, activo, product')

#############################################################################################

'''BLOQUE 1'''

def leer_tesla(fichero):
    
    '''recibe la ruta del fichero csv codificado en UTF-8, y devuelve una lista de tuplas de tipo 
    Tesla(int,datetime,float, float, float, int, bool, str) conteniendo los datos del fichero.'''
    
    Tesla=[]
    with open(fichero, encoding= 'utf-8') as f:
        next(f)
        for linea in f:
            e= linea.split(',')
            Tesla.append(Acciones(int(e[0]),datetime.strptime(e[1],'%Y-%m-%d').date(),float(e[2]),float(e[3]),float(e[4]),float(e[5]),int(e[6]),bool(e[7]),str(e[8])))

    return Tesla

##############################################################################################

'''BLOQUE 2'''

def filtra_por_año(Tesla, d):
    
    '''recibe una lista de tuplas de tipo Tesla y el año dado como parámetro, devolviendo una lista de tuplas de tipo Tesla
    agrupando las acciones por el año introducido.'''
    
    filtro=[]
    for t in Tesla:
        if t.date.year == d:
                tupla=(t[1],t[0],t[2],t[5],t[6],t[7],t[8])
                filtro.append(tupla)
    
    return filtro

###############################################################################################

def calcula_productos(Tesla):
    
    '''recibe una lista de tuplas de tipo Tesla, y devuelve un conjunto con los tipos de productos
    a los que están asociadas las acciones.'''
    
    productos=set()
    for _,_,_,_,_,_,_,_,p in Tesla:
        tupla=(p)
        productos.add(tupla)
        
    return productos

#################################################################################################

def filtrar_por_cantidad_vendida(Tesla,numero):
    
    '''recibe una lista de tuplas de tipo Tesla, y un número introducido como parámetro, devolviendo una lista de tuplas
    de tipo Tesla con las acciones que vendieron un número superior o igual al introducido.'''
    
    ventas=[]
    for code,date,open,_,_,close,vol,_,product in Tesla:
        if vol >= numero:
            tupla=(vol,code,date,open,close,product)
            ventas.append(tupla)
                
    return ventas
    
 ###############################################################################################

'''BLOQUE 3'''
   
def calcular_numero_de_contratos(Tesla, prod=None):
    
    ''': introduces un producto(valor predefinido: none) y te dice cuantas acciones activas tienen asociado ese producto,
    si el valor es none, te dice todas las acciones activas que hay en general.'''
     
    i=0
    if prod is not None:
        for _,_,_,_,_,_,_,activo,product in Tesla:
            if product == prod:
                if activo == True:
                    i=i+1
                    
    else:
        for _,_,_,_,_,_,_,activo,product in Tesla:
            if activo == True:
                    i=i+1
                    
    return i 

################################################################################################
    
def calcular_diferencia_precio(Tesla, d, limit=10):
    
    '''recibe una lista de tuplas de tipo Tesla, un año, y un número límite dado como parámetro, devolviendo una lista 
    de tuplas(código, diferencia) con la diferencia del precio de salida y retirada del mercado de las acciones en el año dado.'''
    
    dif=[]
    for date,code,open,close,volume,_,product in filtra_por_año(Tesla, d):
        diferencia= close-open       
        tupla=(code,open,close,diferencia,volume,product)
        dif.append(tupla)
    dif1=dif[:limit]
        
    return dif1

###################################################################################################

def calcular_beneficio_aproximado(Tesla, cod):   
    
    '''introduces el código de una acción, calcula el valor medio entre el precio más alto y bajo en el mercado, 
    y lo multiplica por el número de unidades vendidas.'''
    
    benef=[]
    for code,_,_,high,low,_,vol,_,_ in Tesla:
        beneficio= ((high+low)/2)*vol
        if cod == code:
            tupla=(beneficio)
            benef.append(tupla)
            
    return benef

###################################################################################################

'''BLOQUE 4'''

def calcular_precio_máximo(Tesla, d, limit=10):
    
    '''Recibe una lista de tuplas de tipo Tesla, un año dado como parámetro y un número límite, 
    devolviendo el precio de salida más alto en las acciones que salieron en el año dado. '''
    
    precio=[]
    for t in Tesla:
        if t.date.year==d:
            tupla=(t[2])
            precio.append(tupla)
            máximo=max(precio)
            
    return máximo

######################################################################################################

def calcular_precio_mínimo(Tesla, d, limit=10):
    
    '''Recibe una lista de tuplas de tipo Tesla, un año dado como parámetro y un número límite, 
    devolviendo el precio de salida más bajo en las acciones que salieron en el año dado. '''
    
    precio=[]
    for t in Tesla:
        if t.date.year==d:
            tupla=(t[2])
            precio.append(tupla)
            mínimo= min(precio)
            
    return mínimo

##########################################################################################################

'''BLOQUE 5'''

def calcular_precios_más_altos(Tesla, d, limit=10):
    
    '''recibe una lista de tuplas de tipo Tesla, un año, y un número límite dado como parámetro, 
    devolviendo una lista de tuplas (código, precio más alto) con las acciones del año dado que alcanzaron los precios más altos.'''
    
    top=[]
    for t in Tesla:
        if t.date.year == d:
            tupla=(t[0],t[3])
            top.append(tupla)
    top1=sorted(top, key=lambda e : e[1], reverse=True)[:limit]
                
    return top1

################################################################################################

def calcuar_precios_más_bajos(Tesla, d, limit=10):
    
    '''recibe una lista de tuplas de tipo Tesla, un año, y un número límite dado como parámetro, devolviendo una
     lista de tuplas (código, precio más bajo) con las acciones del año dado que alcanzaron los precios más bajos.'''
    
    top=[]
    for t in Tesla:
        if t.date.year == d:
            tupla=(t[0],t[4])
            top.append(tupla)
    top1=sorted(top, key=lambda e : e[1], reverse=False)[:limit]
                
    return top1            
    
####################################################################################################   

'''BLOQUE 6'''

def productos_activos(Tesla, d):
    
    '''recibe una lista de tuplas de tipo Tesla, y un año dado como parámetro, devolviendo un 
    diccionario que tiene como clave el tipo de producto, y a la que tienen asociadas los códigos de las acciones del año dado, solo si se encuentran activas.'''
    
    dicc={}
    lista=[filtra_por_año(Tesla, d)]
    for t in lista:
        if t[5] == True:
            if t[6] in dicc:
                dicc[t[6]].append(t[8])
        else:
            dicc[t[6]]= [t[8]]
            
    return dicc
            
######################################################################################################

def acc_rentables(Tesla, d):
    
    '''recibe una lista de tuplas de tipo Tesla, y un año dado como parámetro, devolviendo un 
    diccionario que tiene como claves, de nuevo, los productos, a la que está asociada una lista con el código de la acción, y la diferencia entre el precio de apertura y el de última disposición en el mercado, mostrando solo los que den un valor positivo.'''
    
    lista=[]
    dicc={}
    for r in calcular_diferencia_precio(Tesla, d, limit=10):
        if r[3]>0:
            lista=[r[0],r[3]]
            for t in lista: 
                if r[5] in dicc:   
                    dicc[r[5]].append(lista)
                else:
                    dicc[r[5]]= [lista]
    
    return dicc

######################################################################################################

'''BLOQUE 7'''

def mostrar_precio_salida_por_año(Tesla, d):
    
    '''recibe una lista de tuplas y genera una gráfica de barras que muestra los precios de las acciones 
    en el año dado como parámetro.'''
    
    filtro= filtra_por_año(Tesla, d)
    precios=[t[2] for t in filtro]
    codes=[t[1] for t in filtro]
    titulo= "Precios de salida de las Acciones en el año " + str(d)
    plt.title(titulo)
    indice = range(len(codes))
    plt.bar(indice, precios)
    plt.xticks(indice, codes, fontsize=8)
    plt.show()

######################################################################################################

def mostrar_demanda_mercado(Tesla, d):
    
    '''recibe una lista de tuplas y genera una gráfica que muestra la evolución de la 
    compra de acciones en el año dado como parámetro.'''
    
    filtro=filtra_por_año(Tesla, d)
    demanda=[t[4] for t in filtro]
    codes=[t[1] for t in filtro]
    titulo = "Evolución de la demanda de Acciones en el año " + str(d)
    plt.title(titulo)
    plt.plot(codes,demanda)
    plt.show()

#########################################################################################################   