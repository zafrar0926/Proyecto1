## 🚀 Proyecto MLOps – Canalización de Datos y ML Metadata
## 🚀 Edwin A. Caro (EDCAJI)
## 🚀Andres F. Matallana (ANDRESMLZ)
## 🚀Santiago Zafra Rodríguez (ZAFRAR0926)

¡Bienvenido al proyecto! Este repositorio demuestra cómo construir un ambiente de desarrollo MLOps usando TFX, Docker y Jupyter Lab. Aquí se muestran todas las etapas:

Ingesta y selección de características del dataset Forest Cover Type
Generación de estadísticas, inferencia y curado del esquema (con entornos TRAINING y SERVING)
Transformación e ingeniería de características mediante preprocesamiento personalizado
Registro y consulta de ML Metadata para rastrear la procedencia de los artefactos

**📥 1. Descarga del Repositorio**

Para descargar el proyecto desde GitHub, ejecuta el siguiente comando en la terminal:

```bashgi
git clone https://github.com/zafrar0926/Proyecto1.git
```

***📥 1.1. Navega al directorio clonado***

```bash
cd Proyecto_1
```

**🐳 2.Entorno de Ejecución con Docker**

Este proyecto se ejecuta dentro de un contenedor Docker. Asegúrate de tener Docker instalado en tu máquina o en la máquina virtual.

***2.1. Creación de la Imagen Docker***

El Dockerfile se encuentra en la raíz del proyecto y tiene el siguiente contenido:

***⚙️ dockerfile***

FROM python:3.9
RUN mkdir /work
WORKDIR /work
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install apache-beam[interactive]==2.45.0
RUN pip install jupyter==1.0.0 -U && pip install jupyterlab==3.6.1
EXPOSE 8888
ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]

***⚙️Dependencias***

El archivo requirements.txt contiene:

tfx==1.12.0
apache-beam==2.45.0
jsonschema==3.2.0
scikit-learn==1.6.1
Asegúrate de que todas las dependencias se instalen correctamente durante la construcción de la imagen.

***2.2. Creación de la Imagen Docker***

Para construir la imagen ejecuta:

```bash
docker build -t imagen_proyecto1 .
```

###  2.3. Levantar el Contenedor

Ejecuta el siguiente comando para levantar el contenedor:

**En Linux/Mac:**
```bash
docker run -d -p 8888:8888 -v $(pwd)/Desarrollo:/work --name contenedor_proyecto1 imagen_proyecto1
```

**En Windows (PowerShell):**

```
powershell
docker run -d -p 8888:8888 -v ${PWD}\Desarrollo:/work --name contenedor_proyecto1 imagen_proyecto1
```

**En Windows (CMD):**

```
cmd
docker run -d -p 8888:8888 -v %cd%\Desarrollo:/work --name contenedor_proyecto1 imagen_proyecto1
```

***Detalles***

-d: Modo "detached" (segundo plano)
-p 8888:8888: Mapea el puerto 8888 del contenedor al mismo puerto en tu máquina
-v "ruta_local":/work: Monta el directorio del proyecto en /work dentro del contenedor
--name contenedor_proyecto1: Asigna un nombre al contenedor

**Para acceder a Jupyter Lab, revisa los logs del contenedor para obtener el URL y token.** Por ejemplo:

```bash
docker logs contenedor_proyecto1
```

Abre el URL que aparezca (por ejemplo, http://<IP_MV>:8888/?token=...) en tu navegador.

### 📓 3. Ejecución del Pipeline (Desarrollo.ipynb)

El notebook Desarrollo.ipynb contiene el pipeline completo, que incluye:

***3.1. Descarga y Preparación del Dataset***

Descarga de datos:
Se descarga el dataset Forest Cover Type y se guarda en ./data/covertype/original.
Selección de características:
Se eliminan columnas no deseadas y se realiza una selección univariante usando SelectKBest.
El subconjunto resultante se guarda en
/work/notebooks/data/covertype/transformed/covertype_train_numeric_selected.csv.

***3.2. Prueba de Modelo Simple (Opcional)***

Se divide el dataset, se estandariza y se entrena un modelo Random Forest para obtener una métrica de precisión.

***3.3 Data Pipeline con TFX***

**Conexión a Metadata:**
Se configura una base de datos SQLite en /work/notebooks/ml_metadata.sqlite para almacenar artefactos.

**Ingesta con ExampleGen:**
Se convierte el CSV en TFRecords.

**Estadísticas y Esquema:**
Se calculan estadísticas con StatisticsGen y se infiere un esquema con SchemaGen.
Luego se "cura" el esquema (ajustando rangos y definiendo entornos TRAINING y SERVING).

**Validación de Inferencia:**
Se simula un dataset de servicio (sin la columna Cover_Type) y se valida con ExampleValidator.

**Transformación (Ingeniería de Características):**
Se aplica una función de preprocesamiento (definida en modules/preprocessing.py) mediante el componente Transform.

***3.4. Exploración y Consulta de ML Metadata***

Se registran y consultan artefactos (Examples, ExampleStatistics, Schema, etc.) para rastrear la procedencia y validación de los datos.

**📋Requisitos del Taller**

Este proyecto cumple con todos los puntos especificados en el taller:

***Ingesta y transformación de datos***

Con ExampleGen, StatisticsGen, SchemaGen, y Transform.

***Curado y validación del esquema***

Se ajustan rangos (ej. Hillshade 9am: 0–255, Slope: 0–90) y se definen entornos TRAINING y SERVING.

***Ingeniería de características***

Se aplica preprocesamiento consistente en entrenamiento e inferencia.

***Registro y seguimiento de metadatos***

Se exploran los artefactos y se rastrea la procedencia usando ML Metadata.

***Entorno reproducible***

Se utiliza Docker para crear un ambiente aislado y versionado.

***Versionamiento***

El código está versionado en GitHub: [Proyecto1](https://github.com/zafrar0926/Proyecto1)

***📝 Notas Adicionales***

Configuración de Rutas:
Revisa que las rutas dentro de los notebooks y scripts coincidan con la estructura del directorio en la MV.

Acceso a Jupyter Lab:
Consulta los logs del contenedor para obtener el URL y token de acceso.

Actualización del Esquema y ML Metadata:
Se muestran funciones para consultar y rastrear artefactos en la metadata, facilitando la auditoría del pipeline.