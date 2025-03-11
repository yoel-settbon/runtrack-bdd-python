import mysql.connector

try:
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YoelIT2024!",
        database='LaPlateforme'
    )

    if connexion.is_connected():
        print("Connexion réussie à la base de données 'LaPlateforme'")

        cursor = connexion.cursor()

        cursor.execute("SELECT * FROM etudiant")

        etudiants = cursor.fetchall()

        print("\n Liste des étudiants :")
        for etudiant in etudiants:
            print(etudiant)
        
        cursor.close()
        connexion.close()
        print("\n Connexion fermée")

except mysql.connector.Error as erreur:
    print(f"Erreur lors de la connexion : {erreur}")