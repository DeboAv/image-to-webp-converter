# 🖼 Image to WebP Converter

Aplicación de escritorio para convertir imágenes JPG y PNG a formato WebP con compresión optimizada.

## ✨ Características

- Conversión múltiple de imágenes
- Opción de guardar en la misma carpeta o elegir destino
- Dos modos de compresión:
  - Recomendada (alta calidad)
  - Máxima compresión
- Barra de progreso
- Resumen total de ahorro
- Detalle por imagen
- Compatible con macOS y Windows

---

## 📦 Requisitos (modo desarrollo)

- Python 3.10+
- pip

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la app:

```bash
python app.py
```

---

## 🖥 Ejecutables

El proyecto genera automáticamente:

- `.exe` para Windows
- `.app` para macOS

Desde la sección **Releases** del repositorio.

---

## 🛠 Tecnologías utilizadas

- Python
- Tkinter
- Pillow
- PyInstaller
- GitHub Actions

---

## 📊 Qué hace la compresión

- Convierte imágenes a formato WebP
- Reduce peso manteniendo calidad visual
- Muestra ahorro total y por archivo

---

## 📁 Estructura del proyecto

```
image-to-webp-app/
│
├── app.py
├── icon.png
├── icon.ico
├── requirements.txt
└── README.md
```