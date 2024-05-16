import tensorflow as tf
import tensorflow_hub as hub
import yaml
import openai
import sys
import os
from tkinter import filedialog
import tkinter as tk
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Charge les clés d'API depuis le fichier keys.yaml
def load_api_keys():
    try:
        with open(os.path.join(os.getcwd(), '../private/keys.yaml'), 'r') as file:
            keys = yaml.safe_load(file)
        return keys
    except Exception as e:
        print(f"Erreur lors du chargement des clés d'API : {e}")
        return None

# Télécharge le modèle de transfert de style pré-entraîné
def download_style_transfer_model():
    try:
        hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
        return hub_module
    except Exception as e:
        print(f"Erreur lors du téléchargement du modèle de transfert de style : {e}")
        return None

# Applique le transfert de style à une image
def apply_style_transfer(file_path, hub_module):
    try:
        # Charge l'image
        content_image = tf.io.read_file(file_path)
        content_image = tf.image.decode_image(content_image, channels=3)
        content_image = tf.image.convert_image_dtype(content_image, tf.float32)
        content_image = tf.image.resize(content_image, (256, 256))  # Redimensionne l'image à la taille attendue
        
        # Applique le transfert de style
        stylized_image = hub_module(tf.expand_dims(content_image, axis=0))

        # Sauvegarde l'image stylisée
        output_path = 'stylized_image.png'
        tf.io.write_file(output_path, tf.image.encode_png(tf.cast(stylized_image[0] * 255, tf.uint8)))

        return output_path
    except Exception as e:
        print(f"Erreur lors de l'application du transfert de style : {e}")
        return None

# Fonction pour générer du texte avec OpenAI GPT-3
def generate_text(tags, prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Modèle GPT-3 à utiliser
            prompt=prompt,  # Texte à utiliser comme prompt
            max_tokens=100,  # Nombre maximum de tokens pour le texte généré
            temperature=0.7,  # Contrôle la diversité du texte généré
            n=1  # Nombre de réponses à générer
        )
        generated_text = response.choices[0].text.strip()
        return generated_text
    except Exception as e:
        print(f"Erreur lors de la génération de texte avec GPT-3 : {e}")
        return None

# Fonction pour obtenir une description de l'image avec Azure Cognitive Services
def describe_image(file_path, api_credentials):
    try:
        # Initialisation du client Computer Vision
        credentials = CognitiveServicesCredentials(api_credentials['azure_key'])
        client = ComputerVisionClient(api_credentials['azure_endpoint'], credentials)

        # Analyse de l'image
        with open(file_path, "rb") as image_stream:
            description = client.describe_image_in_stream(image_stream)
        
        return description.captions[0].text if description.captions else "Aucune description trouvée."
    except Exception as e:
        print(f"Erreur lors de la description de l'image avec Azure Cognitive Services : {e}")
        return None

# Fonction pour afficher une image
def show_image(image_path):
    try:
        from PIL import Image
        image = Image.open(image_path)
        image.show()
    except Exception as e:
        print(f"Erreur lors de l'affichage de l'image : {e}")

def main():
    # Chargement des clés d'API
    keys = load_api_keys()
    if keys:
        azure_endpoint = keys['azure_endpoint']
        azure_key = keys['azure_key']
        openai_key = keys['openai_key']
    else:
        print("Impossible de charger les clés d'API. Veuillez vérifier le fichier keys.yaml.")
        return

    # Configuration des clés d'API pour Azure Cognitive Services et OpenAI
    os.environ['AZURE_ENDPOINT'] = azure_endpoint
    os.environ['AZURE_KEY'] = azure_key
    os.environ['OPENAI_KEY'] = openai_key

    # Téléchargement du modèle de transfert de style pré-entraîné
    hub_module = download_style_transfer_model()

    # Interface utilisateur pour sélectionner l'image
    root = tk.Tk()
    root.withdraw()  # Cache la fenêtre principale
    file_path = filedialog.askopenfilename(title="Sélectionner une image")

    # Vérification du chemin de l'image fourni
    if not file_path:
        print("Aucune image sélectionnée.")
        return

    # Obtenir une description de l'image
    image_description = describe_image(file_path, keys)
    print(f"Description de l'image : {image_description}")

    # Demande à l'utilisateur d'entrer un texte pour la modification de l'image
    prompt = input("Quelle modification voulez-vous apporter à l'image? : ")

    # Traitement de l'image
    styled_image_path = apply_style_transfer(file_path, hub_module)
    if styled_image_path:
        print(f"Chemin de l'image stylisée : {styled_image_path}")
        # Génère du texte recontextualisé à partir des tags de l'image et du texte demandant la modification
        print("Génération de texte...")
        image_tags = ["tag1", "tag2", "tag3"]  # Remplacez ceci par les vrais tags de l'image
        generated_text = generate_text(image_tags, prompt)
        print(f"Texte généré : {generated_text}")
        # Affichage de l'image modifiée
        show_image(styled_image_path)
        
if __name__ == "__main__":
    main()
