# 🧠 Lokaler KI-Chatbot mit ONNX – Dummy-Anwendung

Diese Dummy-Anwendung wurde im Rahmen eines Projekts entwickelt, um die lokale Inferenz eines KI-Modells im Browser bzw. lokal über Python zu testen und evaluiren. 

---

## 📁 Projektstruktur

| Datei / Ordner              | Beschreibung                                              |
|-----------------------------|-----------------------------------------------------------|
| `app.py`                    | Startpunkt der Anwendung (z. B. für eine Flask-App)       |
| `phi3_eval.py`              | Skript zur Evaluierung des Phi3-Modells                  |
| `tg_model_evaluation.py`    | Alternatives Evaluation-Skript                           |
| `datenstaz_zur_eval.json`   | Beispieldatensatz zur Bewertung                          |
| `onnx/`                     | ONNX-Modelle zur Inferenz (nur kleine Modelle beilegen) |
| `templates/`                | HTML-Dateien (falls Flask mit Weboberfläche genutzt wird)|
| `requirements.txt`          | Python-Abhängigkeiten                                    |
| `.gitignore`                | Ignorierte Dateien/Folders bei Git (z. B. `__pycache__`) |

---

### 🔹 1. Virtuelle Umgebung erstellen (optional, aber empfohlen)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 🔹 2. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```
### 🔹 3. Anwendung starten


```bash
python app.py
```
Danach im Browser aufrufen.


