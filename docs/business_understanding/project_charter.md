# Project Charter

## Business background

* El cliente es La empresa X, de la ciudad de Bogota
Buscan predecir que clientes se van a suscribir para generar camapañas especializadas para sus nichos mas relevantes

## Scope
* Se planea usar un modelo de clasifcacion binaria
* Crear una herramienta de marketing 
* La idea es que el cliente pueda visualizar informacion de las predicciones y tambien utilizar diferentes bases de datos

## Personnel
* Who are on this project:
	* David Dizes:
		* Project lead
		* PM
		* Data scientist(s)
		* Account manager
	* Client:
		* Data administrator
		* Business contact
	
## Metrics
* What are the qualitative objectives?
	 -Mejorar el alcance de las campañas publicitarias
* What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)
	-Aumentar el numero de suscriptores
* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%) 
	-Aumentar la tasa de clientes suscritos en un %25 
* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
* 	-La empresa se encuentra migrando su informacion a bases de datos por lo que actualmente no sacan provecho de la informacion 
* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)
- la metrica a utlizar es el accuracy con la particion de la base de datos para train, el zip trae ya representaciones del base de datos utiles para entrenar aparte del total de los datos 

## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.

1.Entendimiento del problema/negocio :
	se revisa la informacion en la base de datos para 		entender su estructura y el posible uso de los datos
2.Carga de Datos:
	se carga los datos en formatos utiles para poder 		preprocesar y limpiar la informacion con facilidad
3.Preprocesado:
	se trabajan los datos para hacer normalizacion, data 	augmentation y extraccion de caracteristicas de manera 	personalizada
4.Modelo
	se crea el importa el modelo y se modifican las capas ocultas para tener un modelo mas personalizado y se entrena
5.Test 


## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.
	-Se esperan bases de datos en formato csv con las mismas columnas que la base de  datos con la que fue entrenado el modelo
* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
	- se descarga directamente el zip con todas las bases de datos a partir del link y la biblioteca system para correr comandos de consola y usar wget
  * all the data, 
  * after some pre-aggregation on-prem,
  * Sampled data enough for modeling 

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * Python for feature construction, aggregation and sampling
	*tensorFlow para importar y modifcar el modelo
	*matplotlib para crear graficas con las bases de datos y entender su estructura
	*sklearn para sacar metricas y manejo de datos de entrenamiento y de test
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Communication
* How will we keep in touch? Weekly meetings?
* Who are the contact persons on both sides?
