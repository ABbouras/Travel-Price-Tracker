import json
from pathlib import Path

CONFIG_FILE = Path("config/flights.json")


def load_flights():
    """Charge la liste des vols à surveiller."""
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"{CONFIG_FILE} introuvable")

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def enabled_flights():
    """Retourne uniquement les vols activés."""
    return [f for f in load_flights() if f.get("enabled", True)]


if __name__ == "__main__":
    flights = enabled_flights()

    print(f"{len(flights)} vol(s) chargé(s)\n")

    for flight in flights:
        print(
            f"{flight['origin']} ➜ {flight['destination']} "
            f"({flight['depart']} → {flight['return']})"
        )
