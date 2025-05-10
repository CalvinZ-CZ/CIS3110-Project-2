import pandas as pd
import numpy as np
from faker import Faker
import random
fake = Faker()

# 1. Mouse Usage
mouse_models = ['Finalmouse Starlight Pro', 'Logitech G Pro X Superlight', 'Razer Viper V2 Pro', 'Zowie EC2', 'Glorious Model O']
mouse_data = pd.DataFrame({
    'pro_name': [fake.user_name() for _ in range(100)],
    'mouse_model': [random.choice(mouse_models) for _ in range(100)]
})
mouse_data.to_csv('data/mouse_usage.csv', index=False)

# 2. Keyboard Preference
switch_types = ['Linear', 'Tactile', 'Clicky']
keyboard_data = pd.DataFrame({
    'pro_name': [fake.user_name() for _ in range(100)],
    'keyboard_brand': [random.choice(['Wooting', 'Ducky', 'SteelSeries', 'Corsair']) for _ in range(100)],
    'switch_type': [random.choice(switch_types) for _ in range(100)]
})
keyboard_data.to_csv('data/keyboard_preference.csv', index=False)

# 3. Headset Stats
headset_models = ['HyperX Cloud II', 'SteelSeries Arctis Pro', 'Logitech G Pro X', 'Razer BlackShark V2']
headset_data = pd.DataFrame({
    'pro_name': [fake.user_name() for _ in range(100)],
    'headset_model': [random.choice(headset_models) for _ in range(100)],
    'noise_cancellation': [round(random.uniform(5.0, 10.0), 1) for _ in range(100)]  # scale of 1-10
})
headset_data.to_csv('data/headset_stats.csv', index=False)

# 4. Monitor Configuration
monitor_data = pd.DataFrame({
    'pro_name': [fake.user_name() for _ in range(100)],
    'screen_size_in': [random.choice([24, 24.5, 27]) for _ in range(100)],
    'refresh_rate_hz': [random.choice([144, 240, 360]) for _ in range(100)]
})
monitor_data.to_csv('data/monitor_config.csv', index=False)

# 5. Mousepad Texture Map (for heatmap placeholder)
texture_map = pd.DataFrame({
    'x_coord': np.random.randint(0, 10, 100),
    'y_coord': np.random.randint(0, 10, 100),
    'texture_score': np.random.uniform(1, 10, 100)
})
texture_map.to_csv('data/mousepad_surface.csv', index=False)

# 6. Mousepad Longevity Based on Brand (Updated for Random Longevity)
# Mousepad Brands
mousepad_brands = ['SteelSeries', 'Corsair', 'Razer', 'Logitech', 'Glorious']

# Define ranges for longevity for each brand
longevity_ranges = {
    'SteelSeries': (18, 30),   # Random between 18 and 30 months
    'Corsair': (12, 24),       # Random between 12 and 24 months
    'Razer': (10, 22),         # Random between 10 and 22 months
    'Logitech': (15, 25),      # Random between 15 and 25 months
    'Glorious': (8, 20)        # Random between 8 and 20 months
}

# Generating mousepad longevity data
mousepad_data = pd.DataFrame({
    'pro_name': [fake.user_name() for _ in range(100)],
    'mousepad_brand': [random.choice(mousepad_brands) for _ in range(100)]
})

# Assigning random longevity values based on brand
def generate_random_longevity(brand):
    min_longevity, max_longevity = longevity_ranges[brand]
    return random.randint(min_longevity, max_longevity)

mousepad_data['mousepad_longevity_months'] = mousepad_data['mousepad_brand'].apply(generate_random_longevity)

# Saving mousepad longevity data to CSV
mousepad_data.to_csv('data/mousepad_longevity.csv', index=False)