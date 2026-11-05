
import os
import random
import pandas as pd

# Make the generated data reproducible
random.seed(42)

# Base price per square foot for each location
locations = {
    "Bengaluru": 6500,
    "Hyderabad": 5200,
    "Chennai": 4800,
    "Pune": 5500,
    "Mumbai": 12000,
    "Delhi": 8500
}

records = []

# Generate 1000 house records
for _ in range(1000):

    location = random.choice(list(locations.keys()))

    area_sqft = random.randint(500, 3500)
    bedrooms = random.randint(1, 5)
    bathrooms = random.randint(1, 4)
    year_built = random.randint(1990, 2025)

    base_rate = locations[location]

    # Calculate a sample house price
    price = (
        area_sqft * base_rate
        + bedrooms * 250000
        + bathrooms * 150000
        + (year_built - 1990) * 10000
        + random.randint(-500000, 500000)
    )

    records.append({
        "area_sqft": area_sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "year_built": year_built,
        "location": location,
        "price": max(price, 1000000)
    })

# Convert records into a DataFrame
df = pd.DataFrame(records)

# Create dataset folder
os.makedirs("dataset", exist_ok=True)

# Save dataset to CSV
df.to_csv(
    "dataset/house_data.csv",
    index=False
)

print("Dataset created successfully!")
print("\nFirst 5 records:")
print(df.head())

print("\nDataset shape:", df.shape)
