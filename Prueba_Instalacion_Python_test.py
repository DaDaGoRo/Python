#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fundamentos básicos de programación en Python, NextU
# Actividad Final Unidad 1
#
# Observe las acciones realizadas en este programa y la 
# salida que produce al ejecutar: python3 test.py

import platform

print('Curso              : Fundamentos básicos de programación en Python')
print('Unidad             : 1')
print()

# Información del ambiente de desarrollo
print('Versión de Python  :', platform.python_version())
print('Plataforma         :', platform.platform())
print('Sistema            :', platform.system())
print('Nombre Nodo        :', platform.node())
print('Versión kernel     :', platform.version())
print('Máquina/procesador :', platform.machine()+"/"+platform.processor())