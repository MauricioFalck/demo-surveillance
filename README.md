# Sistema de Vigilancia con Detección de Personas

Este proyecto implementa un sistema de vigilancia en tiempo real que utiliza la cámara web para detectar personas usando el modelo de inteligencia artificial **YOLO**. Cada segundo se procesa un fotograma de la cámara, se anota con los objetos detectados y se muestra en pantalla junto con el conteo de personas detectadas.

## Requisitos previos

- Python 3.8 o superior
- Una cámara web conectada al equipo
- El archivo de modelo `yolo26n.pt` en el directorio del proyecto

## Instalación de dependencias

Descarga el proyecto y luego instala las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Dependiendo del sistema operativo, si falla el comando anterior:

```bash
pip3 install -r requirements.txt
```

Esto instalará:

| Librería        | Descripción                                      |
| --------------- | ------------------------------------------------ |
| `opencv-python` | Captura y visualización de video desde la cámara |
| `ultralytics`   | Framework de YOLO para detección de objetos      |

## Cómo ejecutar el proyecto

Desde el directorio del proyecto:

```bash
python main.py
```

Dependiendo del sistema operativo, si falla el comando anterior:

```bash
python3 main.py
```

Se abrirá una ventana mostrando el video de la cámara con stream de la webcam del computador y el numero de personas detectadas. En la consola se imprimirá el número de personas detectadas por cada fotograma procesado.

Para salir del programa, presiona la tecla **`q`** con la ventana de video en foco.
