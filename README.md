
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
