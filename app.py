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
[]
import json
from datetime import datetime
from collections import Counter

def generer_bilan():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Aucune donnée trouvée.")
        return

    if not data:
        print("Aucune interaction enregistrée.")
        return

    total = len(data)
    pays_counter = Counter([entry["pays"] for entry in data])
    cadeaux = sum(1 for entry in data if "cadeau" in entry["message"].lower())
    cartes = sum(1 for entry in data if "carte" in entry["message"].lower())
    paiements = sum(1 for entry in data if entry["paiement"] == "Oui")

    bilan = f"""
🎄 Bilan annuel SmartNoël – {datetime.utcnow().year}
Nombre total d’interactions : {total}
Nombre de pays différents : {len(pays_counter)}
Pays les plus actifs : {pays_counter.most_common(3)}
Demandes de cadeaux : {cadeaux}
Demandes de cartes : {cartes}
Interactions avec lien de paiement : {paiements}
"""

    print(bilan)

if __name__ == "__main__":
    generer_bilan()
import gradio as gr
from noel_message import encode_string, decode_string, is_christmas_season

def interagir(message):
    if not is_christmas_season():
        return "⛄ Ce n’est pas encore la saison de Noël ! Reviens en novembre ou décembre 🎄"
    encoded = encode_string(message)
    decoded = decode_string(encoded)
    return f"🔐 Encodé : {encoded}\n🔓 Décodé : {decoded}"

iface = gr.Interface(
    fn=interagir,
    inputs=gr.Textbox(label="🎁 Ton message de Noël"),
    outputs=gr.Textbox(label="🎄 Résultat"),
    title="Encodeur de Message Festif",
    description="Tape un message de Noël et découvre sa magie encodée ✨"
)

if __name__ == "__main__":
    iface.launch()
    import streamlit as st
from datetime import datetime
import base64

st.set_page_config(
    page_title="SmartNoël – Clara",
    page_icon="assets/icon-clara.png",
    layout="centered"
)

st.image("assets/banniere-smartnoel.png", use_column_width=True)

ua = st.experimental_get_query_params().get("ua", [""])[0]
if "Android" in ua or "iPhone" in ua:
    st.success("📱 Bonjour depuis un mobile ! Clara t'accompagne partout 🎁")
else:
    st.info("🖥️ Bonjour depuis un ordinateur ! Clara est prête à t'aider 🎄")

st.header("🎄 Clara, l’assistante magique de Noël")
message = st.text_input("🎁 Ton message de Noël")

def encode_string(s):
    return base64.b64encode(s.encode("utf-8")).decode("utf-8")

def decode_string(s):
    return base64.b64decode(s.encode("utf-8")).decode("utf-8")

def is_christmas_season():
    return datetime.now().month in [11, 12]

if st.button("Envoyer à Clara"):
    if not is_christmas_season():
        st.warning("⛄ Ce n’est pas encore la saison de Noël ! Reviens en novembre ou décembre 🎄")
    else:
        encoded = encode_string(message)
        decoded = decode_string(encoded)
        st.text_area("🔐 Encodé", encoded)
        st.text_area("🔓 Décodé", decoded)
