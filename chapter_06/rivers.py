rivers = {"nile": "egypt", "amazon": "brazil", "thames": "uk"}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("Rivers:", ", ".join(r.title() for r in rivers.keys()))
print("Countries:", ", ".join(c.title() for c in rivers.values()))
