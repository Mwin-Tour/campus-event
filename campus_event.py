# Version 1.0
def calculer_prix_panier(articles):
    """Calcule le prix total d'un panier d'articles.

    articles : liste de dicts avec 'prix' (float) et 'quantite' (int)
    Retourne le total arrondi à 2 décimales.
    """
    total = 0.0
    for article in articles:
        total += article["prix"] * article["quantite"]
    return round(total, 2)
