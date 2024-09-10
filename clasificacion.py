# -*- coding: utf-8 -*-
"""Clasificacion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NOw3xQxBnS6uY5d7guE_qtFAq7-YnuLG

# Codificación de las etiquetas en clasificación
"""

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#LEEMOS LOS DATOS DEL IRIS DATASET
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# El conjunto de datos Iris no tiene encabezado, agregaremos nombres a las columnas en español
nombres_columnas = ['longitud_sepalo', 'ancho_sepalo', 'longitud_petalo', 'ancho_petalo', 'clase']

# Leer desde la URL con pandas
data = pd.read_csv(url, names=nombres_columnas)

#Visualizamos las etiquetas
y = data.clase.to_numpy()
print(y)

# Codificación con Label Encoding (y={0,1,...})
label_encoder = LabelEncoder()
y_labels = label_encoder.fit_transform(y)

#visualizamos
y_labels

y.reshape(-1,1).shape

# Codificación con One-Hot Encoding usando `sparse_output`
onehot_encoder = OneHotEncoder(sparse_output=False)
y_onehot = onehot_encoder.fit_transform(y.reshape(-1, 1))
y_onehot[40:80]

# Vemos las dimensiones del array:
y_onehot.shape

# Convertimos los resultados a DataFrame para una mejor visualización
df_onehot = pd.DataFrame(y_onehot,columns=['Clase_0','Clase_1','Clase_2'])
df_onehot

# Convertimos los resultados de la otra codificación a DataFrame para una mejor visualización
df_labels = pd.DataFrame(y_labels,columns = ['Label'])
df_labels

"""# CLASIFICACIÓN BINARIA EN UNA DIMENSIÓN"""

# En este caso vamos a leer los datos con la biblioteca sklearn
from sklearn.datasets import load_iris

# Carganos el conjunto de datos Iris con la biblioteca sklearn y seleccionamos solo las dos primeras clases para la clasificación binaria
iris = load_iris()

iris.data

X = iris.data[iris.target != 2, 0:1]  # Usamos solo la primera característica y las dos primeras clases (0 y 1)
y = iris.target[iris.target != 2] # eliminamos la clase 2 en la variable objetivo

X.shape

y.shape

#visualizamos la codificación de y
y

# Representamos los datos
plt.scatter(X,y,color='blue',edgecolor = 'k')
plt.xlabel(iris.feature_names[0])
plt.ylabel('Clase')
plt.title('Datos Binarios en el Dataset Iris')
plt.show()

#CARGAMOS LA LIBRERÍA PARA REGRESIÓN LOGÍSTICA
from sklearn.linear_model import LogisticRegression

"""Más información sobre el algoritmo de Regresión Logística: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html"""

# Entrenamos un modelo de regresión logística
model = LogisticRegression()
model.fit(X, y)

# Coeficientes de la solución
coef = model.coef_[0]
intercept = model.intercept_

# Imprimimos los coeficientes del modelo
print('Término independiente: b:', intercept)
print('Coeficiente: w:', coef)

# Probamos la función np.linspace
np.linspace(0,5,10)

#REPRESENTAMOS LA FUNCIÓN LOGÍSTICA Y LA EC. DE FRONTERA

# Función logística
def logistic_function(x):
    return 1 / (1 + np.exp(-(coef*x + intercept)))

# Representar la función logística usando el mínimo y el máximo
x_values_logistic = np.linspace(np.min(X), np.max(X), 1000)
y_values_logistic = logistic_function(x_values_logistic)

plt.plot(x_values_logistic, y_values_logistic, color='red', label='Función logística')
plt.xlabel('x')
plt.ylabel('y')

#límites para y
plt.ylim(-0.5, 1.5)

# Representar los ejes y = 0 y y = 1
plt.axhline(y=0, color='black', linestyle='--')
plt.axhline(y=1, color='black', linestyle='--')

# Calcular y marcar el punto donde la función logística vale 0.5 (Ecuación de frontera)
x_05 = -intercept/coef

#Representamos una línea verical
plt.axvline(x=x_05, color='green', linestyle='--', label='frontera')

#Volvemos a representar los datos:
plt.scatter(X, y, color='blue', edgecolor='k', label='Datos')
plt.xlabel(iris.feature_names[0])
plt.ylabel('Clase')
plt.title('Clasificación Binaria en el Dataset Iris')
plt.legend()

plt.show()

"""# CLASIFICACIÓN BINARIA CON DOS DIMENSIONES"""

# Cargamos el conjunto de datos Iris
iris = load_iris()
X = iris.data[:,:2] #:2 Tomamos solo las primeras dos características
y = iris.target

# Creamos un filtro para quedarnos solo con dos clases (clasificación binaria)
filter = (y==0) | (y==1)
X=X[filter]
y=y[filter]

#Imprimimos la dimensión de X
X.shape

#Imprimimos la dimensión de y
y.shape

# Representamos los datos
plt.scatter(X[:,0],X[:,1], c=y, cmap='coolwarm', edgecolor='k', s=20)
plt.title('Iris Dataset 2D ')

plt.show()

# Entrenamos un modelo de regresión logística
model = LogisticRegression()
model.fit(X, y)

# Coeficientes para la frontera de decisión
coef = model.coef_[0]
intercept = model.intercept_[0]

# Imprimimos los coeficientes del modelo
print('Término independiente: beta_0:', coef)
print('Coeficientes: beta_1, beta_2:', intercept)

# REPRESENTAMOS LA ECUACIÓN DE FRONTERA JUNTO A LOS DATOS

# Sacamos los valores máximos y mínimos de la primera coordenada
# para determinar los extremos de la representación gráfica
x_values = np.array([np.min(X[:, 0]), np.max(X[:, 0])])

#Representamos la frontera de decisión
x_values = np.array([np.min(X[:, 0]), np.max(X[:, 0])])
y_values = -(coef[0][0]/coef[0][1])*x_values - intercept/coef[0][1]

plt.plot(x_values, y_values, color='black', label='Frontera')

# Representamos los datos de nuevo
plt.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm', edgecolor='k', s=20)

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('Clasificación Binaria en Iris Dataset')
plt.legend()

plt.plot()

"""# CLASIFICACIÓN CON TRES CLASES EN DOS DIMENSIONES"""

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data[:, :2] # Tomamos solo las primeras dos características
y = iris.target

# Representamos  los datos
from matplotlib.colors import ListedColormap

#Colores para los datos
cmap_bold = ListedColormap(['red', 'green', 'blue'])

# Gráfico de dispersión
plt.scatter(X[:,0],X[:,1], c=y, cmap=cmap_bold, edgecolor='k', s=20)

plt.show()

# Creamos el modelo de clasificación KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)

# Entrenamos el modelo
KNeighborsClassifier
knn.fit(X,y)

# Creamos una malla de puntos para trazar la frontera de decisión
# Establecemos los límites
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

# Creamos una malla de puntos bidimensional entre los límites con espaciado 0.1
# entre los puntos
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

# Predecimos la clase para cada punto en la malla con el modelo entrenado
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Colores para la gráfica
cmap_bold = ListedColormap(['red', 'green', 'blue'])
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])

# Representar la frontera de decisión
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# Representar también los datos
plt.scatter(X[:,0],X[:,1], c=y, cmap=cmap_bold, edgecolor='k', s=20)

#Límites de la gráfica
# plt.___
# plt.___
plt.title("Clasificación con K-NN (k=5)")

plt.show()

