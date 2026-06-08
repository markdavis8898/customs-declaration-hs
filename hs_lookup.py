#!/usr/bin/env python3
"""
HS Code Lookup Tool — search Harmonized System codes for customs declarations.
"""
import json

HS_DATABASE = {
    "8471": "Automatic data processing machines",
    "847130": "Portable digital computers (laptops)",
    "847141": "Data processing machines with display",
    "847149": "Data processing machines, nesoi",
    "847150": "Processing units for data processing",
    "6204": "Suits, ensembles, jackets for women/girls",
    "620462": "Women's cotton trousers",
    "6109": "T-shirts, singlets, knitted or crocheted",
    "610910": "Cotton t-shirts",
    "8473": "Parts for data processing machines",
    "3926": "Articles of plastics, nesoi",
    "4820": "Paper notebooks, business forms",
    "4901": "Printed books, brochures",
    "4911": "Trade advertising materials",
}

class HSCodeLookup:
    def search(self, query):
        results = []
        q = query.lower()
        for code, desc in HS_DATABASE.items():
            if q in code or q in desc.lower():
                results.append({"hs_code": code, "description": desc})
        return results

if __name__ == "__main__":
    import sys
    lookup = HSCodeLookup()
    query = sys.argv[1] if len(sys.argv) > 1 else "computer"
    results = lookup.search(query)
    print(f"HS Code results for: {query}\n")
    for r in results:
        print(f"  {r['hs_code']:12s} {r['description']}")
    if not results:
        print("  No results found.")
