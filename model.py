import json

## -- usar https://flask-sqlalchmey.palletsprojects.com/

def load_db():
    with open("flashcards_db.json", encoding="utf8") as f:
        return json.load(f)

def save_db():
    with open("flashcards_db.json", 'w', encoding="utf8") as f:
        return json.dump(db, f)

db = load_db()