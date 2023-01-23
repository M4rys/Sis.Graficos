from OpenGL.GL import *

import math
import numpy as np

from math import cos, sin

def Scale(x: float, y: float, z: float):
    x = x if x != 0 else 1
    y = y if y != 0 else 1
    z = z if z != 0 else 1

    matriz = np.array([
        [x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]
    ], dtype=float)

    glMultMatrixf(matriz.T)

def Translate(x: float, y: float, z: float):
    matriz = np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]
    ], dtype=float)

    glMultMatrixf(matriz.T)

def Rotate(angulo: int, x: int, y: int, z: int):
    angulo = math.radians(angulo)

    rotateX(angulo) if x else None
    rotateY(angulo) if y else None
    rotateZ(angulo) if z else None

def rotateX(ang_rad):
    matriz = np.array([
        [+cos(ang_rad), 0, +sin(ang_rad), 0],
        [      0,       1,      0,        0],
        [-sin(ang_rad), 0, +cos(ang_rad), 0],
        [      0,       0,      0,        1]
    ], dtype=float)

    glMultMatrixf(matriz.T)

def rotateY(ang_rad):
    matriz = np.array([
        [1,       0,            0,        0],
        [0, +cos(ang_rad), +sin(ang_rad), 0],
        [0, -sin(ang_rad), +cos(ang_rad), 0],
        [0,       0,            0,        1]
    ], dtype=float)

    glMultMatrixf(matriz.T)

def rotateZ(ang_rad):
    matriz = np.array([
        [+cos(ang_rad), -sin(ang_rad), 0, 0],
        [+sin(ang_rad), +cos(ang_rad), 0, 0],
        [      0,             0,       1, 0],
        [      0,             0,       0, 1]
    ], dtype=float)

    glMultMatrixf(matriz.T)