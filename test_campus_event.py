from campus_event import calculer_prix_panier


def test_panier_normal():
    """Deux articles : le total doit être correct."""
    panier = [{"prix": 10.0, "quantite": 2}, {"prix": 5.0, "quantite": 1}]
    assert calculer_prix_panier(panier) == 25.0


def test_panier_vide():
    """Un panier vide doit retourner 0."""
    assert calculer_prix_panier([]) == 0.0
    