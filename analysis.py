import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# 1. Load Data
# -------------------------------
csv_file = "survey_responses.csv"  # Ensure the CSV is in the same folder as this script

try:
    df = pd.read_csv(csv_file)
    print(f"✅ Data loaded successfully: {csv_file}")
except FileNotFoundError:
    print(f"❌ File not found: {csv_file}. Please add it to the repo.")
    exit()

# -------------------------------
# 2. Basic Cleaning
# -------------------------------
df = df.drop_duplicates()
df = df.dropna(axis=1, how='all')

# -------------------------------
# 3. Formatting Numeric Columns
# -------------------------------
numeric_cols = [
    'How would you rate the sound quality of your wireless speaker?',
    'What made you buy your current wireless speaker? Rate each factor from 1 to 5, where 1 is "Not Important" and 5 is "Very Important." [Recommendation from friends/family]',
    'What made you buy your current wireless speaker? Rate each factor from 1 to 5, where 1 is "Not Important" and 5 is "Very Important." [Online reviews from other customers ]',
    'What made you buy your current wireless speaker? Rate each factor from 1 to 5, where 1 is "Not Important" and 5 is "Very Important." [Expert reviews]',
    'What made you buy your current wireless speaker? Rate each factor from 1 to 5, where 1 is "Not Important" and 5 is "Very Important." [Brand reputation]',
    'What made you buy your current wireless speaker? Rate each factor from 1 to 5, where 1 is "Not Important" and 5 is "Very Important." [Price]',
    'What made you buy your current wireless speaker? Rate each factor from 1 to 5, where 1 is "Not Important" and 5 is "Very Important." [Specific features]',
    'What made you buy your current wireless speaker? Rate each factor from 1 to 5, where 1 is "Not Important" and 5 is "Very Important." [Advertising]',
    'How happy are you with your wireless speaker?',
    'How likely are you to buy a new wireless speaker in the next 12 months?',
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# -------------------------------
# 4. Descriptive Statistics
# -------------------------------
print("===== Descriptive Statistics =====")
print(df.describe(include='all'))

# -------------------------------
# 5. Create folder for figures
# -------------------------------
os.makedirs("figures", exist_ok=True)

# -------------------------------
# 6. Graphs
# -------------------------------

# 1. Frequency of use
plt.figure()
freq_avg = df['How often do you use your wireless speaker?'].value_counts(normalize=True) * 100
freq_avg.plot(kind='bar')
plt.title("Frequency of Wireless Speaker Use")
plt.ylabel("% of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/frequency_of_use.png")

# 2. Age bands
plt.figure()
age_bands = df['How old are you?'].value_counts(normalize=True) * 100
age_bands.plot(kind='bar')
plt.title("% of Respondents by Age Band")
plt.ylabel("% of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/age_bands.png")

# 3. Gender
plt.figure()
df['What is your gender?'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("figures/gender_pie.png")

# 4. Household income
plt.figure()
income_dist = df["What's your annual household income?"].value_counts(normalize=True) * 100
income_dist.plot(kind='bar')
plt.title("Household Income Distribution")
plt.ylabel("% of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/income_distribution.png")

# 5. Desired features
desired_cols = [col for col in df.columns if col.startswith("What's most important")]
clean_names = [col.split('[')[-1].strip(']') for col in desired_cols]
desired_means = df[desired_cols].mean()
desired_means.index = clean_names

plt.figure()
desired_means.plot(kind='bar')
plt.title("Desired Features in Wireless Speakers")
plt.ylabel("Average Ranking")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/desired_features.png")

# 6. Respondents vs age & spending
plt.figure()
df_grouped = df.groupby(['How old are you?', 'How much did you spend on your wireless speaker? (US dollars)']).size().unstack(fill_value=0)
df_grouped.plot(kind='bar', stacked=True)
plt.title("Respondents by Age Range & Spending Range")
plt.ylabel("Count of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/age_spending.png")

# 7. Brand competitors (top 20)
plt.figure()
brand_col = "Which brands of wireless speakers do you own or have used before? (Select all that apply) "
brands_series = df[brand_col].dropna().apply(lambda x: [b.strip() for b in str(x).split(',')])
all_brands = brands_series.explode()
brand_counts = all_brands.value_counts(normalize=True) * 100
top20_brands = brand_counts.head(20)
top20_brands.plot(kind='bar')
plt.title("Top 20 Competitor Brands Share")
plt.ylabel("% of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/brand_competitors_top20.png")

# 8. Purchase drivers
purchase_cols = [col for col in df.columns if col.startswith("What made you buy")]
purchase_clean = [col.split('[')[-1].strip(']') for col in purchase_cols]
purchase_means = df[purchase_cols].mean()
purchase_means.index = purchase_clean

plt.figure()
purchase_means.plot(kind='bar')
plt.title("Purchase Drivers (Average Likert Scale)")
plt.ylabel("Average Score (1-5)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/purchase_drivers.png")

# 9. Channel vs % of respondents (Top 10)
plt.figure()
channel_col = "Where do you like to buy wireless speakers?"
channel_dist = df[channel_col].value_counts(normalize=True) * 100
top10_channels = channel_dist.head(10)
top10_channels.plot(kind='bar')
plt.title("Top 10 Purchase Channels")
plt.ylabel("% of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("figures/purchase_channel_top10.png")

print("✅ Analysis complete. Figures saved in 'figures/' folder.")
