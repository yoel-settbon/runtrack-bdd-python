import mysql.connector

# Connexion à la base de données
try:
    connexion = mysql.connector.connect(
        host="localhost",     # Remplace par l'adresse de ton serveur si nécessaire
        user="root",          # Remplace par ton utilisateur MySQL
        password="YoelIT2024!",          # Mets ton mot de passe ici
        database="LaPlateforme"  # Nom de la base de données
    )

    if connexion.is_connected():
        print("✅ Connexion réussie à la base de données 'LaPlateforme'")

        # Création du curseur pour exécuter les requêtes
        cursor = connexion.cursor()

        # Exécution de la requête pour calculer la superficie totale des étages
        cursor.execute("SELECT SUM(superficie) AS superficie_totale FROM etage")

        # Récupération du résultat
        resultat = cursor.fetchone()

        # Affichage du résultat
        superficie_totale = resultat[0]
        print(f"\nLa superficie de La Plateforme est de {superficie_totale} m²")

        # Fermeture du curseur et de la connexion
        cursor.close()
        connexion.close()
        print("\n🔌 Connexion fermée.")

except mysql.connector.Error as erreur:
    print(f"❌ Erreur lors de la connexion : {erreur}")
