# 🛡️ Le Bouclier de Production — Campus-Event CI/CD

Pipeline d'Intégration Continue pour protéger la branche `main` contre tout code défectueux.

---

## 📁 Structure du projet

```
campus-event/
├── .github/
│   └── workflows/
│       └── ci.yml             ← Pipeline GitHub Actions
├── campus_event.py            ← Code source principal
├── test_campus_event.py       ← Tests unitaires (pytest)
├── README.md
└── .flake8                    ← (optionnel) config du linter
```

---

## ⚙️ Installation locale

```bash
# 1. Cloner le dépôt
git clone https://github.com/<votre-org>/campus-event.git
cd campus-event

# 2. Installer les dépendances
pip install flake8 pytest

# 3. Lancer le linter manuellement
flake8 . --max-line-length=127

# 4. Lancer les tests manuellement
pytest test_campus_event.py -v
```

---

## 🚀 Mise en place du pipeline (étapes GitHub)

### Étape 1 — Pousser les fichiers sur GitHub
```bash
git add .
git commit -m "feat: ajout du pipeline CI Le Bouclier de Production"
git push origin main
```

### Étape 2 — Activer la protection de branche

1. Aller dans **Settings → Branches** de votre dépôt GitHub
2. Cliquer sur **Add branch protection rule**
3. Renseigner `main` dans *Branch name pattern*
4. Cocher ✅ **Require status checks to pass before merging**
5. Dans la barre de recherche, taper `Vérification & Tests` (le nom du job CI)
6. Cocher ✅ **Require branches to be up to date before merging**
7. Cliquer **Save changes**

> ⚠️ Le job doit avoir tourné **au moins une fois** avant d'apparaître dans la liste.

---

## 🎬 Scénarios de démonstration

### ❌ Démo d'échec — Code cassé

Créer une branche et introduire une erreur de syntaxe :

```bash
git checkout -b feature/test-echec
# Editer campus_event.py : supprimer un ":" à la fin d'un def
# Exemple : "def calculer_prix_panier(articles)" ← syntaxe invalide
git add campus_event.py
git commit -m "test: code cassé intentionnellement"
git push origin feature/test-echec
```

→ Ouvrir une Pull Request vers `main`  
→ Le robot détecte l'erreur → ❌ croix rouge → bouton **Merge bloqué**

---

### ✅ Démo de succès — Code corrigé

```bash
# Corriger l'erreur dans campus_event.py
git add campus_event.py
git commit -m "fix: correction de la syntaxe"
git push origin feature/test-echec
```

→ Le robot relance automatiquement → ✅ coche verte → bouton **Merge débloqué**

---

## 🔧 Ce que fait le robot (détail du pipeline)

| Étape | Outil | Rôle |
|---|---|---|
| Checkout | `actions/checkout` | Télécharge le code de la PR |
| Python setup | `actions/setup-python` | Configure Python 3.11 |
| Installation | `pip install` | Installe flake8 et pytest |
| Linter | `flake8` | Vérifie la syntaxe et le style |
| Tests | `pytest` | Exécute tous les tests unitaires |

---

## 📚 Ressources utiles

- [Documentation GitHub Actions](https://docs.github.com/en/actions)
- [pytest — Introduction](https://docs.pytest.org/en/stable/getting-started.html)
- [flake8 — Documentation](https://flake8.pycqa.org/en/latest/)
- [Branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
