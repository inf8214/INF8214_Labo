import json
from flask import Flask, render_template, request, jsonify, send_from_directory
from pathlib import Path
# from werkzeug.utils import secure_filename

# Setup Flask app.
app = Flask(__name__)


########################################################################
# Routes
########################################################################

# 1. Route racine pour le formulaire
####################################
@app.route('/', methods=['GET'])
def index():
    # Retourner le template formulaire.html
    return '...'

# 2. Route pour chemin d'accès complet vers ressource/fichier
####################################
@app.route('/img/<path:path>')
def fichier(path):
    # Retourne le fichier static
    return '...'

# 3. Route pour l'affichage de la liste des images
####################################
@app.route('/listeImages', methods=['GET'])
def listeImages():
    # Lire d'abord le fichier json et stocker le contenu sous forme de dictionnaire dans la variable 'images'
    # Stocker la valeur de l'argument 'droits' de la requête dans la variable 'droits', après conversion en booléen
    # retouner le template 'listeImages.html' avec passation des variables 'images' et 'droits'
    return '...'

# 4. Route pour ajouter une image
####################################
@app.route('/ajoutImage', methods=['POST'])
def ajoutImage():
    # Enregistrer l'image dans './static/img/'
    # Ajouter nouvelle image au fichier Json
    # Retourner ensuite la page par défaut
    return '...'


########################################################################
# Routes supplémentaires
########################################################################

# Route spécifique sans paramètres
####################################
@app.route('/allo')
def allo():
    # Retourne html directement
    return "<h1>Allo!</h1>"

# Route spécifique avec paramètres dans le chemin d'accès
####################################
@app.route('/allo/<nom>')
def allo_nom(nom):
    # Retourne html à partir d'un template en passant un paramètre
    return render_template('allo.html', nom=nom)

# Route spécifique avec paramètres comme arguments nommés
####################################
@app.route('/bonjour')
def bonjour():
    prenom = request.args.get('prenom')
    nom    = request.args.get('nom')
    # Retourne html directement, avec interpolation
    return f"<h1>Bonjour {prenom if prenom else ''} {nom if nom else ''}!</h1>"

# Route pour liste des photos en json, à partir d'un json local, filtré par argument nommé.
# Route presque identique à celle utilisée au labo du 18 mars.
####################################
@app.route('/listeJson')
def listeJson():
    # Fichier json local
    filepath = './static/json/listeImages.json'
    with open(filepath, 'r') as f:
        data = f.read()
    # Liste de dictionnaire
    images = json.loads(data)
    # Filtrer les images
    if request.args.get('droits'):
        droits = True if request.args.get('droits').capitalize() == "True" else False
        images = list(filter(lambda image: image['droits']==droits, images))
    # Retourne json
    return jsonify(images)




########################################################################
# Désactiver le caching. À enlever en mode production
########################################################################
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

########################################################################
# Run Flask!
########################################################################
if __name__ == '__main__':
    app.run(debug=True)  # <-- 'debug=True' à enlever en mode production