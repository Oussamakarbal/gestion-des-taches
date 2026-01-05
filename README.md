OUSSAMA KARBAL 5IIRG2


Gestion des Tâches - Odoo 17 (Custom Module)
📝 Présentation du Projet
Ce projet consiste en la création d'un module personnalisé pour Odoo 17 nommé tp_gestion_taches. L'objectif est de fournir une interface simplifiée et efficace pour la gestion opérationnelle des activités au sein d'une organisation.

Le projet utilise Docker pour garantir un environnement de développement reproductible et facile à déployer, incluant une base de données PostgreSQL 16.

✨ Fonctionnalités
Création de tâches : Enregistrement détaillé des missions à accomplir.
Suivi des responsables : Assignation d'un membre de l'équipe à chaque tâche.
Gestion des états (Workflow) : Cycle de vie d'une tâche (Brouillon ➡️ En cours ➡️ Terminé).
Vues dynamiques : Affichage en mode Liste (Tree) pour une vue d'ensemble et mode Formulaire (Form) pour l'édition.
Sécurité : Gestion des droits d'accès via des fichiers CSV de configuration.

🛠️ Architecture Technique
Le projet est structuré comme suit :

addons/ : Contient le code source du module tp_gestion_taches.
models/ : Logique métier en Python (ORM Odoo).
views/ : Définition des interfaces utilisateur en XML.
security/ : Règles d'accès aux données.
config/ : Fichiers de configuration du serveur Odoo (odoo.conf).
docker-compose.yml : Orchestration des conteneurs Odoo et PostgreSQL.

🚀 Installation et Lancement
Prérequis
Docker Desktop installé.
Git Bash ou un terminal compatible.

Étapes
Cloner le dépôt :

Bash
git clone https://github.com/votre-utilisateur/tp_gestion_taches.git
cd tp_gestion_taches
Lancer l'infrastructure :

Bash
docker-compose up -d
Accéder à l'application : Rendez-vous sur http://localhost:8069.

Installer le module :

Activez le mode développeur dans les paramètres.
Allez dans le menu Applications.
Cliquez sur Mettre à jour la liste des modules.
Recherchez tp_gestion_taches et cliquez sur Installer.
📊 Commandes Utiles
Redémarrer Odoo : docker restart odoo_app

Voir les logs : docker logs -f odoo_app

Mise à jour automatique du module : Le fichier docker-compose.yml est configuré avec l'option -u tp_gestion_taches pour appliquer vos changements XML/Python automatiquement au redémarrage.
