# Project Game Recomendation System (Machine Learning Operations)


The objective of this project is to develop a video game recommendation system for the STEAM platform that improves the user experience. This system will be based on a machine learning model capable of analyzing sentiment from user reviews, and in addition, a recommendation system will be created, based on cosine similarity to recommend similar games to the user.

The project has been divided into the following stages:

1. Data loading and preprocessing (ETL)

The data necessary for the development of the model was collected from JSON files. The data includes information about video games, such as the title, description, ratings, and user reviews. The data was cleaned and transformed to be ready for analysis.

2. Exploratory data analysis (EDA)

The data was explored to understand its structure and content. Patterns and trends were identified in the data, as well as possible problems with the data. Additionally, some data was graphed to understand the nature of this.

3. API function development

The API functions that will provide access to the data and solve the problems raised were developed. The API functions were designed to be secure and efficient, and to meet the needs of end users.

4. Machine learning model development

The modeling for the recommendation system, based on cosine similarity, was developed.

5. API implementation

The API functions were implemented in a production environment. The API implementation included its publication, documentation, and monitoring.

6. Deployment

The API was deployed on the Render platform. The deployment included the creation of a virtual environment, the installation of the necessary packages, and the configuration of the API.


## Fases del Proyecto

El proyecto se desarrolló siguiendo estos aspectos clave:
- Carga y Preprocesamiento de Datos: [ETL link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/ETL.ipynb)

- Análisis Exploratorio de Datos: [EDA link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/EDA.ipynb)

- Desarrollo de Funciones API: [Desarrollo de Funciones link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/funcionesAPI.ipynb)

- Desarrollo de modelos de aprendizaje automático: [Machine Learning Desarrollo link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/modeloML.ipynb)

<<<<<<< HEAD
- Implementación de API: [Deployed API link](https://machine-learning-operations-22hy.onrender.com)

=======
- Implementación de API: [Main Link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/main.py)

- Deployement: [Deployed API link](https://machine-learning-operations-22hy.onrender.com)
>>>>>>> 48a4ac49cec6461bfaef1460a9f46b26ccc56f45
</br>


## ETL: Extract, Transform, and Load

To ensure data quality and consistency, a series of essential steps were taken during the ETL (extract, transform, and load) transformation and cleaning phase. These steps prepared the dataset for further analysis and consumption by the API that is being developed.

**Duplicate removal and numeric index assignment**

Duplicates were removed to ensure the uniqueness of rows and a sequential numeric index was assigned to each row to facilitate its manipulation and analysis.

**Invalid date filtering**

The "release_date" column was filtered to identify and quantify outliers that did not comply with the YYYY-MM-DD format. This provided a clear understanding of the data quality and potential problems with the release dates.

**Inconsistent record removal**

Records with null values in all relevant columns for the API were removed to maintain data quality.


The ETL process resulted in a clean, consistent, and optimized dataset for analysis and implementation in the API. Meticulous attention to each step ensures that the results are reliable and useful for future operations and calculations.


**Feature Engineering**

The user_reviews dataset contains reviews of games written by different users. As part of the project challenge, I was assigned the task of creating a sentiment column. To complete this task, I used the TextBlob Natural Language Processing (NLP) library to generate this sentiment column. A scale was established where the value '0' corresponds to a negative rating, '1' indicates neutrality, and '2' represents a positive rating. This approach allowed the reviews to be categorized based on their sentiment, thus providing an additional layer of understanding and analysis for the dataset.

**Tools and environment**

All of these steps were carried out locally in Visual Studio Code (VSCODE), using Jupyter Notebook as the main environment. Python was used as the programming language for the implementation of each step, supported by the versatile numpy and pandas libraries. These tools were essential for the efficient manipulation and transformation of the data.

[ETL link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/ETL.ipynb)

</br>


## EDA: Exploratory Data Analysis

Exploratory data analysis (EDA) was performed on the data resulting from the ETL process. This analysis revealed interesting insights and underlying patterns.

EDA enabled critical decision-making that influenced the direction of the project. The identification of relevant patterns and attributes became an essential pillar for building the API features and the recommendation system that would be developed later on.

The quality of the analysis performed during EDA set the ground for the creation of solid and efficient solutions that would make the most of the information extracted from the data processed in the ETL stage.

The integral process of data transformation, EDA, and building advanced technological solutions encapsulates the very essence of the project. Each step contributed synergistically to bring to life a solid and versatile platform, ready to offer accurate recommendations and an exceptional user experience.

At the end of the EDA, several CSV files were exported only with the columns relevant to the features, with the goal of optimizing the functioning of the API by not having to use the initial data that were quite extensive.

**Tools and environment**

The entire process was developed locally in Visual Studio Code (VSCODE) using Jupyter Notebook as the main working environment. The technological tools that were used include Python as the programming language, along with essential libraries such as numpy and pandas for efficient data manipulation. Additionally, matplotlib and seaborn were used for the creation of impactful graphical visualizations, which allowed to reveal patterns and trends hidden in the data effectively.

[EDA link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/EDA.ipynb)


## Building the API

For the development of the API, I used the FASTAPI framework. Here are the functions created for the endpoints that will be consumed in our API:

- PlayTimeGenre(genre): This function returns the year with the most hours played for the specified genre.

- UserForGenre(genre): The UserForGenre function returns the user with the most hours played for the specified genre, along with a list that shows the accumulation of hours played by year.

- UsersRecommend(year): Returns the top 3 MOST recommended games by users for the given year. These games have positive or neutral recommendations and have the highest rating from users.

- UsersNotRecommend(year): Returns the top 3 LEAST recommended games by users for the given year. These games have negative recommendations and critical comments from users.

- Sentiment_analysis(developer): According to the developer company, a dictionary is returned with the developer name as the key and a list with the total number of user review records that are categorized with a sentiment analysis as the value.

These functions are essential for the functioning of our API, as they are responsible for processing incoming requests and generating appropriate responses.

[Functions link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/funcionesAPI.ipynb)


## Machine Learning Modeling

In this phase of the project, the modeling was carried out for the development of the Recommendation System, based on cosine similarity, where the following functions were created:

- First Item-Item Function: Enter the game id and get recommended games.
- Second User-Item Function: Enter the user id and get recommended games.

For the first approach of the model, an item-item relationship is established. In this scenario, an item is evaluated in terms of its similarity to other items to offer similar recommendations. In this case, the input corresponds to a game and the output is a list of recommended games, using the concept of cosine similarity.

On the other hand, a second proposal for the recommendation system is considered, based on the user-item filter. In this strategy, a user is analyzed to identify users with similar tastes and items that have been appreciated by these similar users are recommended.

[Machine Learning Desarrollo link](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/modeloML.ipynb)


## Deployment

After completing the implementation of main.py and other files that compose the model and the functions, the API deployment was successfully carried out through Render, following a meticulous and organized process:

1. Virtual Environment Creation: The deployment process began with the creation of an isolated virtual environment, which allowed to manage and separate the API-specific dependencies, avoiding conflicts and ensuring consistency in the production environment.

2. Necessary File Configuration: The necessary configurations for the deployment were carried out, ensuring that all essential files were present and correctly configured. This ensured a solid foundation for the operation of the API in the Render environment.

3. Git Initialization and Installations: A Git repository was initialized for the project and the relevant installations of the libraries and packages necessary for the operation of the API were carried out. This ensured that the infrastructure was ready for the deployment process.

4. Generation of Dependency List (Pip Freeze): A list of the specific dependencies and versions used in the virtual environment was generated. This list provided a clear and concise record of the libraries that supported the API, simplifying management and maintenance.

[requierements.txt](https://github.com/alexxcode/Proyecto-1-Machine-Learning-Operations/blob/main/requirements.txt)

5. Render Experience: The necessary steps to deploy the API were carried out through Render. Render provided an efficient and reliable platform for deploying applications, ensuring an optimized and accessible user experience. Render deploys the application and generates a link to access the API. [API](https://machine-learning-operations-22hy.onrender.com). **(You can add "/docs" to the end of the link to access the automatic documentation created by FastAPI. This will give you a detailed, interactive interface that describes all the endpoints, methods and parameters available in the API in a clear and concise manner.)**



## Insights 

This project has been a very rewarding experience that has allowed me to learn and grow as a professional. I have acquired new knowledge about the functioning of recommendation systems, the importance of the initial phases of a Machine Learning project, and how to take a model to production.

In particular, it can be stated that:

- A thorough understanding of the data is essential for the success of any Machine Learning project.
- Data cleaning is an essential task that must be done carefully and rigorously.
- The implementation of an API is an effective way to expose a Machine Learning model to other users.
- Deploying a model in a production environment requires careful planning.


<<<<<<< HEAD
=======

<div align="center">
  
![YouTube]([here](https://youtu.be/Pq9qqReXFNg))
  
</div>
>>>>>>> 48a4ac49cec6461bfaef1460a9f46b26ccc56f45
