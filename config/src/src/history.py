import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

HISTORY_FILE = DATA_DIR / "price_history.json"


def load_history():
    """Charge l'historique des prix."""
    if not HISTORY_FILE.exists():
        return {}

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_history(history):
    """Sauvegarde l'historique."""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def update_price(route, price):
    """
    Met à jour les statistiques d'un trajet.
    """

    history = load_history()

    if route not in history:
        history[route] = {
            "current": price,
            "best": price,
            "worst": price,
            "checks": 1,
            "prices": [
                {
                    "date": datetime.utcnow().isoformat(),
                    "price": price
                }
            ]
        }

    else:

        item = history[route]

        item["current"] = price
        item["checks"] += 1

        if price < item["best"]:
            item["best"] = price

        if price > item["worst"]:
            item["worst"] = price

        item["prices"].append(
            {
                "date": datetime.utcnow().isoformat(),
                "price": price
            }
        )

    save_history(history)

    return history[route]
