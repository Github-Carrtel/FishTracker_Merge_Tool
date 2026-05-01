# FishTracker Merge Tool

> Script Python pour l'extraction, le traitement et la fusion des données exportées par le logiciel FishTracker (version 0.1).

## 1. Métadonnées / Metadata

| Champ | Valeur |
|-------|--------|
| **Nom** | FishTracker Merge Tool |
| **Version** | [À compléter : Version actuelle, ex: 1.0.0] |
| **Date** | [À compléter : Date de dernière modification] |
| **Auteurs / Développeurs** | [À compléter : Noms et affiliations des auteurs] |
| **Contact** | [À compléter : Email de contact] |
| **Laboratoire / Organisme responsable** | [À compléter : Nom de l'institut, ex: INRAE, CARRTEL] |
| **Licence** | GNU General Public License v3.0 (GPL-3.0) |
| **Site web** | [À compléter : URL du site du projet si applicable] |
| **Code source** | [À compléter : URL du dépôt, ex: Gitlab INRAE] |
| **Domaine scientifique** | [À compléter : Écologie, hydrobiologie, traitement de données, etc.] |
| **Fonctionnalités clés** | Extraction des dates et heures depuis les noms de fichiers, fusion de multiples exports FishTracker, formatage de données |
| **Technologies** | Python 3.x, pandas |
| **Mots-clés** | FishTracker, data processing, merge, python, pandas |

## 2. Contexte et historique / Context & History

### Historique
- Matériel préparatoire : [À compléter]
- Versions précédentes : Première version identifiée
- Composants intégrés et dépendances : 
  - `pandas` : Licence BSD (compatible avec GPL-3.0)
- Feuille de route / Roadmap : [À compléter]
- Logiciels équivalents : [À compléter]

### Projet(s) lié(s)
- [À compléter : Nom du projet lié, type de financement, etc.]
- Cadre de développement : Traitement des exports (version 0.1) du logiciel FishTracker.
- Contraintes de licence liées au financement : [À compléter]

## 3. Objectifs / Objectives

### Objectifs scientifiques
[À compléter : Décrire les objectifs de recherche, comme faciliter l'analyse comportementale des poissons en consolidant de multiples exports en une seule base de données analysable.]

### Objectifs d'utilisation et de diffusion
- Durée de vie prévue : [À compléter]
- Utilisation prévue : Production scientifique, analyse de données post-traitement.
- Public cible : Chercheurs, ingénieurs et techniciens de l'équipe / laboratoire.
- Objectifs de diffusion : [À compléter : Outil interne, dépôt public, etc.]
- Communauté de collaboration souhaitée : [À compléter : Oui / Non]
- Préservation : [À compléter : Stratégie d'archivage]

## 4. Caractéristiques techniques / Technical Features

- Technologies utilisées : Python 3.x
- Dépendances : `pandas`, bibliothèques standard (`os`)
- Réutilisation de briques existantes : [À compléter]
- Contraintes techniques : Compatibilité stricte avec le format de nommage et de données du logiciel FishTracker v0.1 (fichiers terminant par `_tracks.txt`).
- Normes et standards : Fichiers en sortie au format CSV délimité par des points-virgules (`;`).

## 5. Installation et utilisation / Installation & Usage

### Prérequis
- Environnement Python 3.x
- Bibliothèque `pandas`

### Installation
Cloner ou télécharger le dépôt, puis installer les dépendances (idéalement dans un environnement virtuel) :
```bash
pip install pandas
```

### Utilisation rapide
1. Placer les fichiers textes à traiter (terminant par `_tracks.txt`) dans un dossier.
2. Éditer le fichier `FishTracker-Merge-Tool.py` et modifier la variable `source_folder` pour indiquer le chemin du dossier :
   ```python
   source_folder = r"/path/to/your/folder"
   ```
3. Exécuter le script :
   ```bash
   python FishTracker-Merge-Tool.py
   ```
4. Le fichier fusionné `CSOT_merged.txt` sera généré dans le même dossier.

## 6. Organisation de l'équipe et du développement / Team & Development Organisation

### Gouvernance
- Organisme responsable : [À compléter]
- Accord de consortium : [À compléter si applicable]

### Équipe
- Membres : [À compléter : Liste des membres avec rôles et statuts]

### Organisation du développement
- Méthodes et outils : [À compléter : Git, etc.]
- Procédures qualité : Le script intègre un traitement par lots robuste ignorant les fichiers non compatibles.
- Sécurité : [À compléter]
- Gestion des versions, bugs et validation : [À compléter]
- Documentation : Mise à jour manuelle du README.
- Règles de contribution externe : [À compléter]

## 7. Diffusion et citation / Distribution & Citation

### Dépôt de référence
- URL du dépôt principal : [À compléter]
- Identifiant pérenne (DOI) : [À compléter]

### Citation
[À compléter : Proposer une formule de citation type, ex: Auteurs (Année). FishTracker Merge Tool. Version X.X. URL]

### Publications et utilisations externes
- [À compléter]

### Support et communication
- Support utilisateur : [À compléter : email, etc.]
- Communications : [À compléter]
- Référencement : [À compléter]

## 8. Gestion du Plan de Gestion de Logiciel / SMP Management

- Responsable du SMP : [À compléter]
- Fréquence de mise à jour : [À compléter]
- Événements déclencheurs : [À compléter]
- Diffusion du SMP : [À compléter]
- Lien avec le DMP (Data Management Plan) : [À compléter]

## 9. Licences et propriété intellectuelle / Legal & IP

- Auteurs et détenteurs des droits : [À compléter]
- Licence du code : **GNU General Public License v3.0 (GPL-3.0)**
- Licence de la documentation et du site : [À compléter, ex: CC-BY-4.0]
- Date d'ouverture prévue (si code actuellement fermé) : [À compléter]
- Gestion des contributions externes : [À compléter]
- Confidentialité / données sensibles : Non applicable pour le code source (attention aux données d'entrée).

---

*Ce README est structuré selon le Modèle de Plan de Gestion de Logiciel de la Recherche – Projet PRESOFT V3.2 (CNRS/IN2P3, 2018).*