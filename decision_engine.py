# Space Disaster Guidance Engine (SDGE)

disaster = input("Enter disaster type: ")

if disaster.lower() == "flood":
    print("\nRecommended Satellite Data:")
    print("- Sentinel-1 SAR")
    print("- Sentinel-2")
    print("- Landsat")

    print("\nRecommended Actions:")
    print("- Monitor flood extent")
    print("- Support evacuation planning")
    print("- Assess affected populations")

elif disaster.lower() == "earthquake":
    print("\nRecommended Satellite Data:")
    print("- Sentinel-1 InSAR")
    print("- GNSS observations")
    print("- Optical imagery")

    print("\nRecommended Actions:")
    print("- Damage assessment")
    print("- Infrastructure monitoring")
    print("- Emergency coordination")

else:
    print("Disaster type not yet available.")
