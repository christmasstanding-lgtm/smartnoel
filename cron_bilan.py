import json
from datetime import datetime
from collections import Counter

def generer_bilan():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("Erreur lors de la lecture du fichier :", e)
        return

    if not data:
        print("Aucune interaction enregistrée.")
        return

    total = len(data)
    interactions_par_jour = {}
    for entry in data:
        date = entry["date"].split("T")[0]
        interactions_par_jour[date] = interactions_par_jour.get(date, 0) + 1

    pays_counter = Counter([entry["pays"] for entry in data])
    cadeaux = sum(1 for entry in data if "cadeau" in entry["message"].lower())
    cartes = sum(1 for entry in data if "carte" in entry["message"].lower())
    paiements = sum(1 for entry in data if entry["paiement"] == "Oui")

    bilan = f"🎄 Bilan annuel SmartNoël – {datetime.utcnow().year}\n"
    bilan += f"Total d’interactions : {total}\n"
    bilan += f"Pays les plus actifs : {pays_counter.most_common(3)}\n"
    bilan += f"Demandes de cadeaux : {cadeaux}\n"
    bilan += f"Demandes de cartes : {cartes}\n"
    bilan += f"Paiements détectés : {paiements}\n"
    bilan += "\n📅 Interactions par jour :\n"
    for date, count in interactions_par_jour.items():
        bilan += f"{date} : {count}\n"

    try:
        with open("bilan.txt", "w", encoding="utf-8") as f:
            f.write(bilan)
        print("✅ Bilan généré et enregistré dans 'bilan.txt'")
    except Exception as e:
        print("Erreur lors de l'enregistrement du bilan :", e)

if __name__ == "__main__":
    generer_bilan()
