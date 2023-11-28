# Proyecto 1 (Machine Learning Operations)
Machine Learning Operations (MLOps)

El objetivo de este proyecto es desarrollar un sistema de recomendación de videojuegos para la plataforma STEAM que mejore la experiencia de los usuarios. Este sistema se basará en un modelo de aprendizaje automático capaz de analizar los sentimientos a partir de los comentarios de los usuarios, y ademas se creará un Sistema de Recomendación, basado en la similitud del coseno para recomendar juegos similares al usuario. 

El proyecto se ha dividido en las siguientes etapas:

1. Carga y preprocesamiento de datos

Se recopilaron los datos necesarios para el desarrollo del modelo a partir de archivos json. Los datos incluyen información sobre los videojuegos, como el título, la descripción, las puntuaciones y los comentarios de los usuarios. Los datos se limpiaron y se transformaron para que estuvieran listos para el análisis.

2. Análisis exploratorio de datos

Se exploraron los datos para comprender su estructura y contenido. Se identificaron patrones y tendencias en los datos, así como posibles problemas con los datos. Además, se graficaron algunos datos para comprender la naturaleza de estos.  

3. Desarrollo de funciones API

Se desarrollaron las funciones API que proporcionarán acceso resolver las necesidades planteadas. Las funciones API fueron diseñadas para ser seguras y eficientes, y para satisfacer las necesidades de los usuarios finales.

4. Desarrollo de modelo de aprendizaje automático

Se desarrolló el modelado para el Sistema de Recomendación, basado en la similitud del coseno.

5. Implementación de API

Se implementaron las funciones API en un entorno de producción. La implementación de API incluyó su publicación documentación y el monitoreo de esta.

6. Despliegue

Se desplegó la API en la plataforma 'render'. El despliegue incluyó la creación de un entorno virtual, la instalación de los paquetes necesarios y la configuración de la API.


## Fases del Proyecto

El proyecto se desarrolló siguiendo estos aspectos clave:
- Carga y Preprocesamiento de Datos: [ETL link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/ETL.ipynb)

- Análisis Exploratorio de Datos: [EDA link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/EDA.ipynb)

- Desarrollo de Funciones API: [Desarrollo de Funciones link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/funcionesAPI.ipynb)

- Desarrollo de modelos de aprendizaje automático: [Machine Learning Desarrollo link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/modeloML.ipynb)

- Implementación de API: [Main Link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/main.py)

- Deployement: [Deployed API link](https://machine-learning-operations-22hy.onrender.com)
</br>

## ETL: extraer, transformar, y cargar

Para garantizar la calidad y coherencia de los datos, se realizaron una serie de pasos esenciales durante la fase de transformación y limpieza de datos (ETL). Estos pasos prepararon el conjunto de datos para su análisis posterior y su consumo por la API que se está desarrollando.

**Eliminación de duplicados y asignación de índice numérico**

Se eliminaron los duplicados para asegurar la unicidad de las filas y se asignó un índice numérico secuencial a cada fila para facilitar su manipulación y análisis.

**Filtrado de fechas inválidas**

Se filtró la columna "release_date" para identificar y cuantificar los valores atípicos que no cumplían con el formato aaaa-mm-dd. Esto proporcionó una comprensión clara de la calidad de los datos y posibles problemas en las fechas de lanzamiento.


**Eliminación de registros incoherentes**

Se eliminaron los registros con valores nulos en todas las columnas relevantes para la API para mantener la calidad de los datos.

El proceso de ETL resultó en un conjunto de datos limpio, coherente y optimizado para el análisis y la implementación en la API. La atención meticulosa a cada paso garantiza que los resultados sean confiables y útiles para futuras operaciones y cálculos.



**Feature Engineering**

Dentro del dataset de **user_reviews**, se recopilan reseñas de juegos realizadas por diversos usuarios. Como parte del desafío del proyecto, se me asignó la tarea de crear una columna de sentimiento. Para llevar a cabo esta tarea, se empleó una librería de Procesamiento del Lenguaje Natural (NLP) TextBlob, con el fin de generar esta columna de sentimiento. Se estableció una escala donde el valor '0' corresponde a una valoración negativa, '1' indica neutralidad y '2' representa una valoración positiva. Este enfoque permitió categorizar las reseñas en base a su sentimiento, proporcionando así una capa adicional de comprensión y análisis en el dataset.

**Herramientas y entorno**

Todas estas etapas se llevaron a cabo de manera local en Visual Studio Code (VSCODE), empleando Jupyter Notebook como entorno principal. Para la implementación de cada paso, se utilizó Python como lenguaje de programación, respaldado por las versátiles bibliotecas numpy y pandas. Estas herramientas fueron fundamentales para la manipulación y transformación eficiente de los datos.

[ETL link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/ETL.ipynb)

## EDA: Análisis Exploratorio de Datos

El análisis exploratorio de datos (EDA) se realizó sobre los datos resultantes del proceso ETL. Este análisis reveló interesantes perspectivas y patrones subyacentes.


El EDA permitió tomar decisiones críticas que influyeron en la dirección del proyecto. La identificación de patrones y atributos relevantes se convirtió en un pilar esencial para construir las funciones API y el sistema de recomendación que se desarrollaría posteriormente.

La calidad del análisis realizado durante el EDA estableció el terreno para la creación de soluciones sólidas y eficientes que aprovecharían al máximo la información extraída de los datos procesados en la etapa de ETL.

El proceso integral de transformación de datos, EDA y construcción de soluciones tecnológicas avanzadas encapsula la esencia misma del proyecto. Cada paso contribuyó de manera sinérgica para dar vida a una plataforma sólida y versátil, preparada para ofrecer recomendaciones precisas y una experiencia de usuario excepcional.

Al finalizar el EDA, se exportaron varios archivos CSV solo con las columnas relevantes para las funciones, con el objetivo de optimizar el funcionanmiento de la API al no tener que utilizar los datos iniciales que eran bastante extensos. 

**Herramientas y entorno**

Todo este proceso se desarrolló localmente en Visual Studio Code (VSCODE) utilizando Jupyter Notebook como entorno de trabajo principal. Las herramientas tecnológicas que se emplearon incluyen Python como lenguaje de programación, junto con bibliotecas esenciales como numpy y pandas para la manipulación eficiente de datos. Además, se utilizaron matplotlib y seaborn para la creación de visualizaciones gráficas impactantes, que permitieron revelar patrones y tendencias ocultas en los datos de manera efectiva.

[EDA link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/EDA.ipynb)


## Construcción de la API

Para el desarrollo de la API, he utilizado el framework FASTAPI. A continuación, se detallan las funciones creadas para los endpoints que serán consumidos en nuestra API:

1. PlayTimeGenre(genero): Esta función devuelve el año con la mayor cantidad de horas jugadas para el género especificado.

2. UserForGenre(genero): La función UserForGenre devuelve el usuario que acumula la mayor cantidad de horas jugadas para el género especificado, junto con una lista que muestra la acumulación de horas jugadas por año.

3. UsersRecommend(año): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. Estos juegos tienen recomendaciones positivas o neutrales y cuentan con la máxima calificación por parte de los usuarios.

4. UsersNotRecommend(año): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. Estos juegos tienen recomendaciones negativas y comentarios críticos por parte de los usuarios.

5. sentiment_analysis(desarrolladora): Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.

Estas funciones son fundamentales para el funcionamiento de nuestra API, ya que se encargan de procesar las solicitudes entrantes y generar respuestas adecuadas.

[Desarrollo de Funciones link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/funcionesAPI.ipynb)

## Modelamiento (Machine Learning)

En esta fase del proyecto, se llevó a cabo el modelado para el desarrollo del Sistema de Recomendación, basado en la similitud del coseno, donde se crearon las siguientes funciones:

- Primera Función item-item, introduzco el id del juego y me devuelve juegos recomendados.

- Segunda Función de usuario-item, Ingreso el id  del usuario y le devuelve juegos recomendados.

Para el primer enfoque del modelo, se establece una relación ítem-ítem. En este escenario, se evalúa un ítem con respecto a su similitud con otros ítems para ofrecer recomendaciones similares. En este caso, el input corresponde a un juego y el output es una lista de juegos recomendados, utilizando el concepto de similitud del coseno.

Por otra parte, se considera una segunda propuesta para el sistema de recomendación, basada en el filtro user-item. En esta estrategia, se analiza a un usuario para identificar usuarios con gustos similares y se recomiendan ítems que hayan sido apreciados por estos usuarios afines.

[Machine Learning Desarrollo link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/modeloML.ipynb)

## Deployment

Luego de completar la implementación de **main.py** y demás archivos que componen el modelo y las funciones, el despliegue de la API se realizó de manera exitosa a través de Render, siguiendo un proceso meticuloso y organizado:

**1. Creación de Entorno Virtual:** El proceso de despliegue comenzó con la creación de un entorno virtual aislado, lo cual permitió gestionar y separar las dependencias específicas de la API, evitando conflictos y asegurando la coherencia en el entorno de producción.

**2. Configuración de Archivos Necesarios:** Se llevaron a cabo las configuraciones necesarias para el despliegue, asegurando que todos los archivos esenciales estuvieran presentes y correctamente configurados. Esto garantizó una base sólida para el funcionamiento de la API en el entorno de Render.

**3. Inicialización de Git y Realización de Instalaciones:** Se inició un repositorio de Git para el proyecto y se realizaron las instalaciones pertinentes de las bibliotecas y paquetes necesarios para el funcionamiento de la API. Esto aseguró que la infraestructura estuviera lista para el proceso de despliegue.

**4. Generación de Lista de Dependencias (Pip Freeze):** Se generó una lista de las dependencias y versiones específicas utilizadas en el entorno virtual. Esta lista proporcionó un registro claro y conciso de las bibliotecas que respaldaban la API, simplificando la gestión y el mantenimiento. [requierements.txt](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/requirements.txt)

**5. Experiencia Render:** A través de Render, se llevaron a cabo los pasos necesarios para desplegar la API. Render proporcionó una plataforma eficiente y confiable para implementar aplicaciones, asegurando una experiencia de usuario optimizada y accesible. Render implementa la aplicación y genera un enlace para acceder a la [API en ejecución](https://machine-learning-operations-22hy.onrender.com). **(Puedes agregar "/docs" al final del enlace para acceder a la documentación automática creada por FastAPI. Esto te brindará una interfaz interactiva y detallada que describe todos los endpoints, métodos y parámetros disponibles en la API de manera clara y concisa.)**



## Conclusiones 

Este proyecto ha sido una experiencia muy gratificante que me ha permitido aprender y crecer como profesional. He adquirido nuevos conocimientos sobre el funcionamiento de los sistemas de recomendación, la importancia de las fases iniciales de un proyecto de Machine Learning, y cómo llevar a producción un modelo.

En particular, se puede afirmar que:

* La comprensión a fondo de los datos es fundamental para el éxito de cualquier proyecto de Machine Learning.
* La limpieza de datos es una tarea esencial que debe realizarse con cuidado y rigor.
* La implementación de una API es una forma eficaz de exponer un modelo de Machine Learning a otros usuarios.
* El despliegue de un modelo en un entorno de producción requiere una planificación cuidadosa.



<div align="center">
  
![YouTube]([here](https://youtu.be/Pq9qqReXFNg))
  
</div>
