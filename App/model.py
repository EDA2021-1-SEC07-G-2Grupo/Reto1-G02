﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as inser
from DISClib.Algorithms.Sorting import selectionsort as selec
from DISClib.Algorithms.Sorting import quicksort as quic
from DISClib.Algorithms.Sorting import mergesort as merg
assert cf
assert quic

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    lista=str("ARRAY_LIST")
    catalog = {
                "Video": None,
                'video_id': None
               }
    catalog['Video'] = lt.newList(lista,cmpfunction=cmpvideos)           
    catalog['video_id'] = lt.newList(lista,cmpfunction=comparecategorynames)

    return catalog

# Funciones para agregar informacion al catalogo
def addVideo(catalog, videos):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog["Video"], videos)

    # Se obtienen los autores del libro
       

def addVideoCategory_id(catalog, categoriavid):
    """
    Adiciona un tag a la lista de tags
    """
    t = newVidcategoria(categoriavid['id'], categoriavid['name'])
    lt.addLast(catalog["video_id"], t)

# Funciones para creacion de datos

def newVidcategoria(_id, category_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    categoriavid = {'id': _id, 'category_id': category_id}
    return categoriavid


# Funciones de consulta
def getvideobycountry(catalog, pais):
    Country_list = lt.newList()
    n=0
    while n < lt.size(catalog):
          video=lt.getElement(catalog,n)
          if video["country"]==pais:
              lt.addLast(Country_list, video) 
          n+=1
    
    return Country_list
    
def GetVideosbycategoria(catalog, categoria):
    vid_categ = lt.newList()
    n=0
    while n < lt.size(catalog):
          video=lt.getElement(catalog,n)
          if video["category_id"]==categoria:
              lt.addLast(vid_categ, video) 
          n+=1  
    return vid_categ

def GetVideosbyCountry(catalog, pais):
    vid_country = lt.newList()
    n=0
    while n < lt.size(catalog):
          video=lt.getElement(catalog,n)
          if video["country"]==pais:
              lt.addLast(vid_categ, video) 
          n+=1  
    return vid_country

def video_por_etiqueta(catalog, label):
    vid_label = lt.newList()
    n=0
    while n < lt.size(catalog):
          video=lt.getElement(catalog,n)
          if label in video["tags"]:
              lt.addLast(vid_label, video) 
          n+=1  
    return vid_label

    
def Get_rending_categoria(catalog):
    trending_dates= lt.newList()
    lista_prohibido=[]
    n=0
    while n < lt.size(catalog):
          video=lt.getElement(catalog,n)
          ID=video["video_id"]
          if ID not in lista_prohibido:
              dato={"ID": ID,"title":video["title"], "Channel title": video["channel_title"], "country":video["country"],"dias":1}
              lt.addLast(trending_dates,dato)
              lista_prohibido.append(ID)
          else:
               posicion=lista_prohibido.index(ID)
               elemento_cambiar=lt.getElement(trending_dates,posicion)
               elemento_cambiar["dias"]+=1

          n+=1  
    
    return trending_dates


def Get_trending_pais(catalog):
    trending_dates= lt.newList()
    lista_prohibido=[]
    n=0
    while n < lt.size(catalog):
          video=lt.getElement(catalog,n)
          ID=video["video_id"]
          if ID not in lista_prohibido:
              dato={"ID": ID,"title":video["title"], "Channel title": video["channel_title"], "country":video["country"],"dias":1}
              lt.addLast(trending_dates,dato)
              lista_prohibido.append(ID)
          else:
               posicion=lista_prohibido.index(ID)
               elemento_cambiar=lt.getElement(trending_dates,posicion)
               elemento_cambiar["dias"]+=1
          n+=1  
    
    return trending_dates
   

   
# Funciones utilizadas para comparar elementos dentro de una list
def cmpvideos(vid1,vid2):
    if (vid1.lower() in vid2['id'].lower()):
        return 0
    return -1



def cmpVideosByViews(video1, video2):

    return (float(video1['views']) > float(video2['views']))



def cmpVideosBydias(vid1, vid2):
    
    return (float(vid1) > float(vid2))





def cmpVideosByLikes(video1, video2):

    return (float(video1['likes']) > float(video2['likes']))




def comparecategorynames(name, tag):
    return (name == tag['name'])

# Funciones de ordenamiento

def sortVideos_byViews(catalog, size):
    sub_list = lt.subList(catalog,1, size)
    sub_list = sub_list.copy()
    sorted_list=merg.sort(sub_list, cmpVideosByViews)
    return  sorted_list

def sortVideos_byDias(catalog):
    sub_list = lt.subList(catalog,1, 1)
    sub_list = sub_list.copy()
    sorted_list=merg.sort(sub_list, cmpVideosBydias)
    return  sorted_list

    
def videos_por_likes(catalog,size):
    sub_list = lt.subList(catalog,1, size)
    sub_list = sub_list.copy()
    sorted_list=merg.sort(sub_list, cmpVideosByLikes)
    return  sorted_list

