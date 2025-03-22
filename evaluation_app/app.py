from flask import Flask, render_template
from tg_model_evaluation import evaluate_tg_models
from phi3_eval import evaluate_phi3
import os

app = Flask(__name__)

# Sicherstellen, dass der Ordner existiert
SAVE_FOLDER = "gespeicherte_ergebnisse"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tg_ergebnisse')
def tg_results():
    """ Führt die erste Bewertungsmethode durch (Standard-Modelle wie GPT-2, Legal-BERT, usw.) """
    results = evaluate_tg_models()

    # Durchschnittswerte pro Modell berechnen
    average_results = {}
    for result in results:
        modell = result["modell"]
        if modell not in average_results:
            average_results[modell] = {
                "modellgroesse_mb": result["modellgroesse_mb"],
                "durchschnittliche_antwortzeit": result["durchschnittliche_antwortzeit"],
                "durchschnittlicher_bertscore": result["durchschnittlicher_bertscore"],
                "durchschnittlicher_fact_score": result["durchschnittlicher_fact_score"]
            }

    # Render HTML-Seite als String
    html_content = render_template("tg_vergleich.html", average_results=average_results, detailed_results=results)

    # HTML-Datei speichern
    save_path = os.path.join(SAVE_FOLDER, "tg_ergebnisse_modelle.html")
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Ergebnisse gespeichert unter: {save_path}")
    return html_content

@app.route('/phi3_ergebnisse')
def tg_results_onnx():
    """ Führt die zweite Bewertungsmethode für ONNX Phi-3 durch """
    results = evaluate_phi3()

    # Durchschnittswerte pro Modell berechnen
    average_results = {}
    for result in results:
        modell = result["modell"]
        if modell not in average_results:
            average_results[modell] = {
                "modellgroesse_mb": result["modellgroesse_mb"],
                "durchschnittliche_antwortzeit": result["durchschnittliche_antwortzeit"],
                "durchschnittlicher_bertscore": result["durchschnittlicher_bertscore"],
                "durchschnittlicher_fact_score": result["durchschnittlicher_fact_score"]
            }

    # Render HTML-Seite als String
    html_content = render_template("tg_vergleich.html", average_results=average_results, detailed_results=results)

    # HTML-Datei speichern
    save_path = os.path.join(SAVE_FOLDER, "evaluate_phi3_ergebnisse.html")
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Ergebnisse gespeichert unter: {save_path}")
    return html_content

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)  # Disable auto-reload