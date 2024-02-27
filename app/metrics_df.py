
### Modèle Random Forest et Calcul des Métriques :

# Import des bibliothèques nécessaires
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import pandas as pd

# Chargement du dataset Iris
iris = load_iris()

df2 = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df2['target'] = iris.target
df2['nature'] = iris.target

dict = {0: "setosa", 1: "versicolor", 2: "virginica"}
df2 = df2.replace({"nature": dict})

dd = df2.groupby('nature')
sl = dd.describe().iloc[:,1:8]
sw = dd.describe().iloc[:,9:16]
pl = dd.describe().iloc[:,17:24]
pw = dd.describe().iloc[:,25:32]

df_sl = pd.DataFrame(pd.DataFrame(sl))
df_sl.columns = df_sl.columns.droplevel(level=0)
df_sl.drop(columns='std', inplace=True)

df_sw = pd.DataFrame(pd.DataFrame(sw))
df_sw.columns = df_sw.columns.droplevel(level=0)
df_sw.drop(columns='std', inplace=True)

df_pl = pd.DataFrame(pd.DataFrame(pl))
df_pl.columns = df_pl.columns.droplevel(level=0)
df_pl.drop(columns='std', inplace=True)

df_pw = pd.DataFrame(pd.DataFrame(pw))
df_pw.columns = df_pw.columns.droplevel(level=0)
df_pw.drop(columns='std', inplace=True)


X = df2.iloc[:,:-2]
y = df2.iloc[:,-2]

# Séparation des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création et entraînement du modèle Random Forest
rf_model = RandomForestClassifier(n_estimators=1, max_depth=2,random_state=42)

rf_model.fit(X_train, y_train)

# Prédiction sur l'ensemble de test
y_pred = rf_model.predict(X_test)
y_prob = rf_model.predict_proba(X_test)

# Calcul des métriques d'évaluation
accuracy = round(accuracy_score(y_test, y_pred)*100,2)
precision = round(precision_score(y_test, y_pred, average='weighted')*100,2)
recall = round(recall_score(y_test, y_pred, average='weighted')*100,2)
f1 = round(f1_score(y_test, y_pred, average='weighted')*100,2)
auc_score = round(roc_auc_score(y_test, y_prob, multi_class='ovr'),4)

# Création d'un DataFrame avec les métriques
df = pd.DataFrame({'Names': ['Accuracy', 'Precision', 'Recall', 'F1-Score','AUC'],
                           'Metrics': [accuracy, precision, recall, f1, auc_score]})
