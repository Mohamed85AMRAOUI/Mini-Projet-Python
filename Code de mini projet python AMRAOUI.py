import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

print("Répertoire actuel :", os.getcwd())  # Vérifiez où Python cherche le fichier
print("Fichier présent ?", os.path.exists("student_depression_dataset.csv"))
df = pd.read_csv(r"C:\Users\PC\Desktop\Licence d'excellence\Python_\MiniProjetPython\student_depression_dataset.csv")
# === 1. Importation des données ===
print("1. Importation des données :")
try:
    df = pd.read_csv(r"C:\Users\PC\Desktop\Licence d'excellence\Python_\MiniProjetPython\student_depression_dataset.csv")
    print("✅ Fichier chargé avec succès !")
except FileNotFoundError:
    print("❌ Erreur : Fichier introuvable. Vérifiez le chemin ou le nom.")


# === 2. Exploration des données ===
print("2. Exploration des données :")
print("\n=== Premières lignes ===")
print(df.head())

print("\n=== Informations générales ===")
print(df.info())

print("\n=== Valeurs manquantes ===")
print(df.isnull().sum())

# === 3. Manipulation des données ===
print("3. Manipulation des données :")
# Création d'une colonne "mention"
print("Création d'une colonne mention :")
df['mention'] = df['note'].apply(
    lambda x: 'Excellent' if x >= 16 else 
              'Très bien' if x >= 14 else 
              'Bien' if x >= 12 else 
              'Passable' if x >= 10 else 
              'Insuffisant'
)

# Filtrage des étudiants de Terminale
print("Filtrage des étudiants de Terminale :")
terminale = df[df['classe'] == 'Terminale']

# === 4. Analyse statistique ===
print("4. Analyse statistique === :")
print("\n=== Statistiques par matière ===")
print(df.groupby('matiere')['note'].describe())

print("\n=== Moyenne par classe ===")
print(df.groupby('classe')['note'].mean().round(2))

# === 5. Visualisation ===
print("5. Visualisation :")
# Histogramme des notes
print("Histogramme des notes :")
df['note'].plot(
    kind='hist',
    bins=10,
    title='Distribution des notes',
    edgecolor='black'
)
plt.xlabel('Note')
plt.show()

# Boxplot par matière
print("Boxplot par matière :")
df.boxplot(column='note', by='matiere', grid=False)
plt.title('Comparaison des notes par matière')
print("Supprime le titre automatique :")
plt.suptitle('')  # Supprime le titre automatique
plt.show()

# === Export des résultats ===
print("6. Export des résultats :")
df.to_csv('resultats_analyse.csv', index=False)
print("\n Résultats exportés dans 'resultats_analyse.csv'")