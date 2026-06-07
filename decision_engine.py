# Space Disaster Guidance Engine (SDGE)

disaster = input("Enter disaster type: ")
phase = input("Enter phase (Preparedness, Response, Recovery): ")

if disaster.lower() == "flood":

    if phase.lower() == "preparedness":
        print("Develop flood risk maps")
        print("Establish early warning systems")

    elif phase.lower() == "response":
        print("Monitor flood extent")
        print("Support evacuation planning")

    elif phase.lower() == "recovery":
        print("Conduct damage assessment")
        print("Restore critical infrastructure")

elif disaster.lower() == "earthquake":

    if phase.lower() == "preparedness":
        print("Seismic risk assessment")
        print("Emergency drills")

    elif phase.lower() == "response":
        print("Damage assessment")
        print("Emergency coordination")

    elif phase.lower() == "recovery":
        print("Infrastructure reconstruction")
        print("Community recovery planning")

else:
    print("Disaster type not yet available.")
