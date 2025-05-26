import numpy as np
from catboost import  Pool
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar datos de ejemplo (cáncer de mama)
data = load_breast_cancer()
X = data.data
y = data.target

# Dividir en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Especificar columnas categóricas (en este caso no hay, pero así se haría)
# cat_features = [0, 1, 2]  # Índices de columnas categóricas

# Crear el modelo
model = CatBoostClassifier(
    iterations=500,  # Número de árboles
    learning_rate=0.1,
    depth=6,
    loss_function='Logloss',
    verbose=100,  # Muestra información cada 100 iteraciones
    random_state=42
)

# Entrenar el modelo
model.fit(
    X_train, y_train,
    eval_set=(X_test, y_test),
    # cat_features=cat_features  # Usar si hay características categóricas
)

# Predecir
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# Importancia de características
feature_importances = model.get_feature_importance()
feature_names = data.feature_names
for score, name in sorted(zip(feature_importances, feature_names), reverse=True):
    print(f"{name}: {score:.2f}")