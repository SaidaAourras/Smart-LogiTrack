# 🚖 Taxi Duration Predictor (ETA Pipeline)

Ce projet implémente une solution de bout en bout (End-to-End) pour prédire le temps d'arrivée estimé (**ETA**) des taxis urbains. Il intègre un pipeline ETL distribué, un modèle de Machine Learning, une orchestration complète et une API sécurisée.

---

## 🏗️ Architecture du Système

Le projet suit une **architecture Medallion** pour garantir la qualité des données :



1.  **Zone Bronze** : Ingestion des données brutes (données Taxi NYC).
2.  **Zone Silver** : Nettoyage et Feature Engineering avec **PySpark** (stockage PostgreSQL).
3.  **ML Layer** : Entraînement d'un modèle de régression pour prédire `trip_duration`.
4.  **Serving Layer** : API **FastAPI** sécurisée par JWT pour les prédictions et analytics.

---

## 🛠️ Stack Technique

* **Orchestration** : Apache Airflow
* **Traitement de données** : PySpark (Traitement distribué)
* **Base de données** : PostgreSQL
* **Machine Learning** : Scikit-Learn (Modèle de régression)
* **API & Backend** : FastAPI, SQLAlchemy, JWT
* **Conteneurisation** : Docker & Docker Compose

---

## 📋 Étapes du Workflow (DAG Airflow)

L'ensemble du processus est automatisé via un DAG Airflow comprenant :
* **Tâche 1** : Téléchargement automatique du dataset.
* **Tâche 2** : Ingestion en zone Bronze.
* **Tâche 3** : Nettoyage (Silver) : filtrage des trajets aberrants (distances > 200 miles, durée ≤ 0, passagers ≤ 0).
* **Tâche 4** : Entraînement et sérialisation du modèle (`model.pkl`).

---

## 🚀 API & Analytics

L'API FastAPI expose des endpoints sécurisés pour les utilisateurs et les analystes :

### Prédictions
* `POST /predict` : Envoi des features (JSON) -> Retourne la durée estimée.

### Analytics (SQL Avancé)
Les analytics utilisent des requêtes SQL natives (CTE) via SQLAlchemy pour garantir des performances optimales sans recalcul côté Python :
* `GET /analytics/avg-duration-by-hour` : Analyse des heures de pointe.
* `GET /analytics/payment-analysis` : Comparaison des durées selon le mode de paiement.

---

## ⚙️ Installation

### 1. Prérequis
* Docker & Docker Compose

### 2. Lancement
```bash
# Cloner le projet
git clone <url-du-repo>
cd <nom-du-repo>

# Lancer l'infrastructure
docker-compose up -d
```
### 3. Accès
- Airflow UI : ```http://localhost:8080```

- FastAPI Docs (Swagger) : ```http://localhost:8000/docs```

## 🧪 Tests
Pour lancer les tests unitaires :
``` pytest tests/ ```
