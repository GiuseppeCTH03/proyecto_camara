# EXPERIMENTO DE ACCESO A CÁMARA (ANDROID-->LINUX)

Descripción breve: acceso al hardware de un Honor 400 desde Fedora 23 usando scrcpy y v4l2loopback para el procesamiento en python.

## Requisitos previos
- Activar el modo desarrollador del dispositivo android.
- Activar la depuración USB
- Módulo 'v4l2loopback' (akmod).
- Python 3 con OpenCV.
- Creación de un entorno virtual .venv con python -m venv .venv
- Dentro del entorno virtual se instalan todas las dependencias (OpenCV)

## Guia de inicio rápido
### Paso 1: Tunel de video
El tunel de video se crea para (valga la redundancia), crear un tunel que conecte el ide con la camara del smartphone.
```bash
sudo modprobe v4l2loopback video_nr=10 card_label="Honor-Camera" exclusive_caps=1
```
## Paso 2: Iniciar el puente scrcpy
Esto es para visualizar y controlar el tunel de video, se inicializa en la terminal del proyecto, en este caso en visual studio code.
```bash
scrcpy --video-source=camera --v4l2-sink=dev/video10 --no-window
```
## Paso 3: Ejecutar el script
```bash
source .venv/bin/activate
python main.py
```

# SOLUCIÓN A PROBLEMAS COMUNES
## Error en la cámara: CAMERA_IN_USE
Significa que la cámara está siendo utilizada por alguna otra aplicación del smartphone, se deben cerrar y limpiar estas aplicaciones del segundo plano.
**Adicional**: Se debe revisar el reconocimiento facial desde seguridad y biométrica (o alguna opción similar), donde podrás desactivar el reconocimiento facial y liberar la cámara frontal.

## Index out of range:
Verificar que /dev/video10 existe con ls /dev/video* esto mostrará las "entradas" ocupadas o asignadas de la computadora a cada índice.

## Confusion:
Si no sabes siquiera si la computadora está detectando el puerto que usas con el dispositivo, utiliza
```bash
adb devices
```
Si sale algo como
```bash
List of devices attached
AMBEJV5830G00051    device
```
Significa que el sistema detecta al dispositivo y se puede proceder a ejecutar el script con confianza.

# CURIOSIDADES
Si quieres ver el modelo exacto del dispositivo puedes anclar este comando a la terminal
```bash
adb shell getprop ro.product.model
```
Para ver la version de Android:
```bash
adb shell getprop ro.build.version.release
```
Para reiniciar el servidor ADB si se queda apagado o se cuelga:
```bash
adb kill-server
adb start-server
```
