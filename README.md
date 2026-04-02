# 🎫 Campus-Event

![Status](https://img.shields.io/badge/status-en%20développement-yellow)
![Node](https://img.shields.io/badge/node-%3E%3D18.0.0-green)
![MySQL](https://img.shields.io/badge/mysql-8.0-blue)

Plateforme de billetterie universitaire permettant aux associations étudiantes de créer des événements et aux étudiants de réserver leurs tickets en ligne avec génération automatique de QR Code.


## Description & Contexte

Campus-Event est une application web full-stack développée dans le cadre d'un projet universitaire. Elle permet à 3 types d'utilisateurs d'interagir :

- 🎓 **L'étudiant** consulte les événements, réserve des tickets et reçoit un QR Code scannable.
- 🏛 **Le responsable d'association** crée et gère ses événements depuis un dashboard dédié.
- ⚙️ **L'administrateur** supervise l'ensemble de la plateforme.

Le projet suit une méthodologie **Usine Logicielle** avec une toolchain intégrée : Notion (documentation), Trello (Kanban), GitHub (versioning) et Slack (alertes automatiques).

---

## Prérequis & Installation

### Prérequis

- Node.js >= 18.0.0
- MySQL 8.0
- npm >= 9.0.0
- Git

### Installation

**Étape 1 — Cloner le dépôt**
```bash
git clone https://github.com/Mwin-Tour/campus-event.git
cd campus-event
```

**Étape 2 — Installer les dépendances backend**
```bash
cd backend
npm install
```

**Étape 3 — Configurer les variables d'environnement**
```bash
cp .env.example .env
```
Édite le fichier `.env` avec tes valeurs :
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASS=ton_mot_de_passe
DB_NAME=campus_event
JWT_SECRET=un_secret_tres_long_et_securise
PORT=3000
```

**Étape 4 — Créer la base de données**
```bash
mysql -u root -p < docs/campus_event_database.sql
```

**Étape 5 — Démarrer le serveur**
```bash
npm start
```
Le serveur tourne sur → http://localhost:3000

**Étape 6 — Ouvrir l'interface**

Ouvre simplement `frontend/index.html` dans ton navigateur.

---

## Utilisation & Exemples

### Inscription d'un étudiant
```bash
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "nom": "Diallo",
    "prenom": "Ousmane",
    "email": "ousmane@campus.edu",
    "mot_de_passe": "monMotDePasse123"
  }'
```

### Connexion et récupération du token JWT
```bash
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "ousmane@campus.edu", "mot_de_passe": "monMotDePasse123"}'
```

### Liste des événements disponibles
```bash
curl http://localhost:3000/api/events
```

### Réserver un ticket (avec token JWT)
```bash
curl -X POST http://localhost:3000/api/reservations \
  -H "Authorization: Bearer TON_TOKEN_JWT" \
  -H "Content-Type: application/json" \
  -d '{"evenement_id": 1, "nombre_tickets": 2}'
```

### Vérifier que l'API fonctionne
```bash
curl http://localhost:3000/api/health
# Réponse attendue : {"status": "ok"}
```

---

## Guide de Contribution

### Convention de branches
```
feature/nom-fonctionnalite   → nouvelle fonctionnalité
hotfix/nom-correction        → correctif urgent
```

### Convention de commits
```
feat: description [Trello-Card-#N]      → nouvelle fonctionnalité
fix: description [Trello-Card-#N]       → correction de bug
docs: description [Trello-Card-#N]      → documentation
hotfix: description [Trello-Card-#N]    → correctif urgent
```

### Processus de Pull Request
1. Crée ta branche depuis `develop`
2. Développe et commit avec la convention ci-dessus
3. Pousse ta branche : `git push origin feature/ma-branche`
4. Ouvre une Pull Request vers `develop`
5. Au moins **1 membre** doit approuver avant le merge
6. Après merge → déplace le ticket Trello vers **✅ Terminé**

Voir [CONTRIBUTING.md](./CONTRIBUTING.md) pour plus de détails.

---

## 📄 Licence

**Licence Propriétaire — Campus-Event**

Copyright (c) 2026 Équipe Campus-Event. Tous droits réservés.

Ce logiciel et sa documentation associée sont la propriété exclusive de l’équipe Campus-Event.

### 🚫 Restrictions
- Il est strictement interdit de copier, modifier, distribuer, vendre ou exploiter tout ou partie de ce logiciel sans autorisation écrite préalable.
- Toute reproduction ou utilisation non autorisée constitue une violation des droits d’auteur.

### 🔐 Utilisation autorisée
- Ce projet est fourni uniquement dans un cadre académique et de démonstration.
- Aucun droit d’exploitation commerciale n’est accordé.

### ⚖️ Responsabilité
- Le logiciel est fourni “en l’état”, sans garantie d’aucune sorte.
- Les auteurs ne peuvent être tenus responsables des dommages résultant de son utilisation.

### 📩 Contact
Pour toute demande d’autorisation ou d’utilisation :
> contacter l’équipe Campus-Event

---

## Liens utiles

| Outil | Lien |
|-------|------|
| 📋 Notion (Wiki) | [https://www.notion.so/Campus-event-central-33545519435880e1bdf2c71215d908d7?source=copy_link] |
| 📌 Trello (Kanban) | [https://trello.com/invite/b/69cbadee10695d790b571fff/ATTI7676f517614835fef831017af9b4a8b2EE2B126F/campus-events] |
| 💬 Slack | [https://app.slack.com/client/T0AQLJBTH6V/C0APS927WK1] |
| 📂 GitHub | [https://github.com/Mwin-Tour/campus-event] |