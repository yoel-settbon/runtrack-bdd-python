import mysql.connector

try:
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YoelIT2024!",
        database="LaPlateforme"
    )

    if connexion.is_connected():
        print("Connexion réussie à la base de données 'LaPlateforme'")

        cursor = connexion.cursor()
        cursor.execute("SELECT nom, capacite FROM salle")
        resultats = cursor.fetchall()

        print("\n Liste des salles et leurs capacités :")
        for salle in resultats:
            print(f"Salle: {salle[0]}, Capacité: {salle[1]}")

        cursor.close()
        connexion.close()
        print("\n Connexion fermée.")

except mysql.connector.Error as erreur:
    print(f"Erreur lors de la connexion : {erreur}")