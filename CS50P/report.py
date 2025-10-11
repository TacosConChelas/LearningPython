def main():
    spacecraft = {"name": "Voyager 1",}

    spacecraft.update({"distance" : 0.1, "orbit" : "Sun"})

    print(create_report(spacecraft))



def create_report(spacecraft):
    return f"""
    ============ REPORT ============
    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ================================
    """




main()