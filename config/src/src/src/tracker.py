import requests

from config import enabled_flights
from history import update_price

RAPIDAPI_HOST = "sky-scrapper.p.rapidapi.com"


class FlightTracker:

    def __init__(self, api_key):
        self.api_key = api_key

    def headers(self):
        return {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": RAPIDAPI_HOST
        }

    def search(self, flight):

        origin = flight["origin"]
        destination = flight["destination"]
        depart = flight["depart"]
        ret = flight["return"]

        print(f"Recherche {origin} -> {destination}")

        # La requête API sera branchée ici.
        #
        # Pour le moment on simule un prix.
        #
        # Dans le prochain commit nous reconnecterons
        # exactement le code de ton ancien flight_tracker.py

        simulated_price = 780

        route = f"{origin}-{destination}"

        stats = update_price(route, simulated_price)

        return {
            "flight": flight,
            "price": simulated_price,
            "stats": stats
        }

    def run(self):

        results = []

        for flight in enabled_flights():
            results.append(self.search(flight))

        return results
