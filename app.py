import gradio as gr
from utils import repondre_clara, enregistrer_interaction

def discuter(message, pays):
    reponse = repondre_clara(message, pays)
    enregistrer_interaction(message, reponse, pays)
    return reponse

iface = gr.Interface(
    fn=discuter,
    inputs=[
        gr.Textbox(label="🎄 Écris ton message à Clara"),
        gr.Textbox(label="🌍 Ton pays (ex: France, Côte d’Ivoire, Maroc)")
    ],
    outputs="text",
    title="SmartNoël – Clara l’IA festive",
    description="Clara t’aide à trouver des idées cadeaux, cartes, recettes et surprises pour les fêtes !"
)

iface.launch()
import json
from datetime import datetime

def repondre_clara(message, pays):
    # Réponse simple simulée (remplace par ton IA ou ton API Hugging Face)
    if "cadeau" in message.lower():
        return f"🎁 Une idée cadeau pour {pays} : un mug personnalisé ou un livre magique !"
    elif "carte" in message.lower():
        return f"💌 Voici une carte de vœux festive pour {pays} : 'Joyeux Noël et Bonne Année !'"
    else:
        return f"🎄 Clara te souhaite de belles fêtes depuis {pays} !"

def enregistrer_interaction(message, reponse, pays):
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append({
        "date": datetime.utcnow().isoformat(),
        "message": message,
        "reponse": reponse,
        "pays": pays,
        "paiement": "Oui" if "paypal.me" in reponse else "Non"
    })

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        import json
from datetime import datetime

def repondre_clara(message, pays):
    # Réponse simple simulée (remplace par ton IA ou ton API Hugging Face)
    if "cadeau" in message.lower():
        return f"🎁 Une idée cadeau pour {pays} : un mug personnalisé ou un livre magique !"
    elif "carte" in message.lower():
        return f"💌 Voici une carte de vœux festive pour {pays} : 'Joyeux Noël et Bonne Année !'"
    else:
        return f"🎄 Clara te souhaite de belles fêtes depuis {pays} !"

def enregistrer_interaction(message, reponse, pays):
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append({
        "date": datetime.utcnow().isoformat(),
        "message": message,
        "reponse": reponse,
        "pays": pays,
        "paiement": "Oui" if "paypal.me" in reponse else "Non"
    })

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
