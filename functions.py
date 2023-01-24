from OpenGL.GL import *

import math
import numpy as np

from math import cos, sin

# Projeções

def Perspectiva(left, right, top, bottom, near, far):
    l, r, t, b, n, f = left, right, top, bottom, near, far

    matriz = np.array([
        [(2*n) / (r - l),       0,            (r + l) / (r - l),                        0],
        [      0,          2*n / (t - b),     (t + b) / (t - b),                        0],
        [      0,               0,          -1* (f + n) / (f - n),       -2*f*n / (f - n)],
        [      0,               0,                  -1,                                 0]
    ], dtype=float)

    glMultMatrixf(matriz.T)

def Ortogonal(left, right, top, bottom, near, far):
    l, r, t, b, n, f = left, right, top, bottom, near, far

    matriz = np.array([
        [2 / (r - l),           0,                   0,            -1 * (r + l) / (r - l)],
        [     0,           2 / (t - b),              0,            -1 * (t + b) / (t - b)],
        [     0,                0,             -2 / (f - n),       -1 * (f + n) / (f - n)],
        [     0,                0,                   0,                                 1]
    ], dtype=float)

    glMultMatrixf(matriz.T)


# Transformações

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

# Normal

#
def Normal(p1, p2):
    x = p1[1] * p2[2] - p1[2] * p2[1]
    y = p1[2] * p2[0] - p1[0] * p2[2]
    z = p1[0] * p2[1] - p1[1] * p2[0]

    glNormal(x, y, z)

def solidCube(cubeQuads, cubeVertices, top=False):
    
    glBegin(GL_QUADS)


    for cubeQuad in cubeQuads:
        if top:
            glNormal(0, 0, 1)

        if not top and cubeQuad[1] < cubeQuad[0]:
            Normal(cubeVertices[cubeQuad[1]], cubeVertices[cubeQuad[3]])
        elif not top:
            Normal(cubeVertices[cubeQuad[1]], cubeVertices[cubeQuad[0]])
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()