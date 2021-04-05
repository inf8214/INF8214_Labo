import json
from flask import Flask, render_template, request, send_from_directory, jsonify
from pathlib import Path
from imagesDb import initDatabase, getImages, addImage
# from werkzeug.utils import secure_filename


# Setup Flask app.
app = Flask(__name__)

# Database initialisation
initDatabase()


########################################################################
# Routes
########################################################################

# 1. Route racine pour le formulaire
####################################
@app.route('/', methods=['GET'])
def index():
    return render_template('formulaire.html')

# 2. Route pour chemin d'accès complet vers ressource/fichier
####################################
@app.route('/img/<path:path>')
def fichier(path):
    # Retourne fichier static
    return send_from_directory('static/img', path)

# 3. Route pour l'affichage de la liste des images
####################################
@app.route('/listeImages', methods=['GET'])
def listeImages():
    # Stocker la valeur de l'argument 'droits' de la requête dans une variable (après conversion en integer)
    droits = 1 if request.args.get('droits') == "True" else 0
    # Requête pour la liste des images
    images = getImages(droits)
    # retouner un template, avec passation de la variable 'images'
    return render_template('listeImages.html', images=images)

# 4. Route pour ajouter une image
####################################
@app.route('/ajoutImage', methods=['POST'])
def ajoutImage():
    # Enregistrer l'image
    f = request.files['fichier']
    f.save(f'./static/img/{f.filename}') # <-- Pour plus de sécurité, on peut utiliser '{secure_filename(f.filename)}'
    # Ajouter nouvelle image au fichier Json
    nouvelleImage = {
        'titre'   : request.form['titre'],
        'droits'  : 1 if request.form['droits'] == "True" else 0,
        'fichier' : f.filename
    }
    addImage(nouvelleImage)
    # Retourner ensuite la page par défaut
    return 'Image ajoutée à la banque d\'images'



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
