# 🎄 SmartNoël – Clara, l’assistante magique de Noël

[![Tester sur Hugging Face](https://img.shields.io/badge/🎄%20Tester%20Clara%20en%20ligne-blue)](https://huggingface.co/spaces/Daou/smartnoel)

Bienvenue dans SmartNoël, une application festive propulsée par Gradio...
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

Festive bot developer.  
> ✨ Christmas, AI, and creativity in service of a magical world.  
> 🎁 Hugging Face + GitHub = enchanted solution.

