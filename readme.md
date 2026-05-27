# README - Despliegue del Proyecto

## Importante

Este proyecto debe ejecutarse específicamente con **Python 3.11.9**.  
La razón es que algunas dependencias utilizadas, especialmente versiones antiguas de **LangChain** y otras librerías relacionadas con IA/RAG, presentan problemas de compatibilidad con versiones más recientes de Python.

Usar otra versión puede generar errores durante la instalación o ejecución del proyecto.

---

# Requisitos Previos

Instalar:

- Python 3.11.9
- pip
- virtualenv (opcional)

Verificar la versión instalada:

```bash
python --version
```

Debe mostrar algo similar a:

```bash
Python 3.11.9
```

---

# Configuración del Proyecto

## 1. Crear el entorno virtual usando Python 3.11.9

### Windows

```bash
py -3.11 -m venv venv
```

### Linux / Mac

```bash
python3.11 -m venv venv
```

---

## 2. Activar el entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Instalar dependencias

Desde la carpeta raíz del proyecto ejecutar:

```bash
pip install -r requirements.txt
```

---

# Ingesta de Documentos

Antes de ejecutar el backend y el frontend, es obligatorio ejecutar el proceso de ingesta para cargar los documentos y generar los embeddings utilizados por el sistema RAG, este archivo esta dentro de backend/app

Ejecutar:

```bash
python ingest.py
```

---

# Ejecutar el Backend

El backend se ejecuta utilizando **Uvicorn**.

Desde la carpeta /backend/app del proyecto ejecutar:

```bash
uvicorn main:app --reload
```

> Asegúrate de que el archivo principal del backend sea `main.py`.

---

# Ejecutar el Frontend

El frontend se ejecuta usando **Streamlit**.

Ejecutar:

```bash
streamlit run app.py
```

> Si el archivo principal del frontend tiene otro nombre, reemplazar `app.py` por el correspondiente.

---

# Orden Correcto de Ejecución

1. Crear el entorno virtual.
2. Activar el entorno virtual.
3. Instalar dependencias.
4. Ejecutar `ingest.py`.
5. Ejecutar el backend.
6. Ejecutar el frontend.

---

# Notas Adicionales

- Mantener el entorno virtual activado mientras se trabaja en el proyecto.
- Backend y frontend deben ejecutarse en terminales separadas.
- Si ocurre algún error de dependencias, verificar nuevamente la versión de Python utilizada.
- Se recomienda no actualizar manualmente las versiones de LangChain sin validar compatibilidad con el proyecto.