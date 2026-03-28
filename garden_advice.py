"""
Garden Advice App
This program provides gardening advice based on the season and plant type.
"""

def get_season_advice(season):
    """Return advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Return advice based on the plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Main function to run the program."""

    # Get user input instead of hardcoded values
    season = input("Enter the season (summer/winter): ").lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").lower()

    # Generate advice
    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)

    # Display advice
    print("\nGardening Advice:")
    print(advice)


# Run the program
if __name__ == "__main__":
    main()