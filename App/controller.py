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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadVideosCategory(catalog)
    """sortBooks(catalog)"""


def loadVideos(catalog):
    """
    Carga los videos del archivo.  Por cada video se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videosfile = cf.data_dir + 'Videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


def loadVideosCategory(catalog):
    """
    Carga la información que asocia tags con libros.
    """
    videocategoryfile = cf.data_dir + 'Videos/category-id.csv'
    input_file = csv.DictReader(open(videocategoryfile, encoding='utf-8'), delimiter='\t')
    for videotag in input_file:
        model.addVideoCategory_id(catalog, videotag)


# Funciones de ordenamiento


def sortVideos(catalog, size):
    return model.sortVideos_byViews(catalog, size)



# Funciones de consulta sobre el catálogo

def GetVideosbyCountry (catalog, pais):
    return model.getvideobycountry(catalog, pais)

def Get_trending_pais(catalog):
    return model.Get_trending_pais(catalog)
def GetVideosbycategoria(catalog, categoria):
    return model.GetVideosbycategoria(catalog,categoria)
def Get_rending_categoria(catalog):
    return model.Get_rending_categoria(catalog)
def sortVideos_byDias(catalog):
    return model.sortVideos_byDias(catalog)
def video_por_etiqueta(catalog,label):
    return model.video_por_etiqueta(catalog,label)
def videos_por_likes(catalog,size):
    return model.videos_por_likes(catalog,size)