import sqlite3
import json


def initDatabase():

    # Create database / connexion
    ##################################################
    con = sqlite3.connect('./images.db')
    cur = con.cursor()

    # Drop table if exist
    ##################################################
    cur.execute('DROP TABLE IF EXISTS images')
    
    # Create table
    ##################################################
    fields = '(id integer primary key, titre text, droits numeric, fichier text)'
    sqlString = f'CREATE TABLE images {fields}'
    cur.execute(sqlString)

    # Insert default data into table
    ##################################################
    # Get data from Json
    filepath = './static/json/listeImages.json'
    with open(filepath, 'r') as f:
        data = json.loads(f.read())
    # List of records to be inserted
    records = [(i['titre'], 1 if i['droits'] else 0, i['fichier']) for i in data]
    # insert multiple records in a single query
    cur.executemany('INSERT INTO images VALUES(NULL,?,?,?);', records)
    # Save (commit) the changes
    con.commit()


def getImages(droits):

    # Create connexion
    con = sqlite3.connect('./images.db')
    con.row_factory = sqlite3.Row # <-- permet de retourner un objet contenant une liste de dictionnaire plutot qu'un objet contenant une liste de tuple!

    # Get images list
    t = (droits,) # <-- pour créer un tuple avec 1 seul élément
    images = con.cursor().execute('SELECT * FROM images WHERE droits=?', t) # <-- plus sécuritaire que l'interpolation p/r à SQL injection
    return images
    

def addImage(nouvelleImage):

    # Create connexion
    con = sqlite3.connect('./images.db')
    con.row_factory = sqlite3.Row

    # Add image; save (commit) the changes
    con.cursor().execute('INSERT INTO images VALUES(NULL,:titre,:droits,:fichier);', nouvelleImage)
    con.commit()

def deleteImage(id):
    pass