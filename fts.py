import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

pd.set_option("display.float_format", "{:.2f}".format)
plt.style.use("seaborn-v0_8-whitegrid")
sns.set_theme(style="whitegrid", palette="viridis", context="talk")

np.random.seed(42)
num_days = 7
days = [datetime.now() - timedelta(days=i) for i in range(num_days-1, -1, -1)]
date_labels = [d.strftime("%d-%b") for d in days]

data = {
    "Date": date_labels,
    "Steps": np.random.randint(3500, 12000, size=num_days),
    "Calories_Burned": np.random.randint(1800, 2800, size=num_days),
    "Calories_Consumed": np.random.randint(2000, 3200, size=num_days),
    "Water_Intake(ml)": np.random.randint(1500, 3500, size=num_days),
    "Sleep_Hours": np.random.uniform(5.5, 9, size=num_days).round(1),
    "BMI": np.random.uniform(20, 25, size=num_days).round(2),
    "BMR": np.random.uniform(1400, 1800, size=num_days).round(2),
    "Progress(%)": np.random.uniform(60, 100, size=num_days).round(1)
}

df = pd.DataFrame(data)
print("=== FITNESS DATA SAMPLE ===")
print(df)
print("\nBasic statistics:\n", df.describe())

plt.figure(figsize=(10, 6))
ax = sns.barplot(x="Date", y="Steps", data=df, hue=None, palette="viridis")
for i, val in enumerate(df["Steps"]):
    ax.text(i, val + 200, f"{val}", ha='center', va='bottom', fontsize=10, color='black')
plt.title("Steps Walked Per Day", fontsize=18, weight='bold')
plt.xlabel("Date")
plt.ylabel("Steps")
plt.tight_layout()
plt.savefig("steps_per_day.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Calories_Burned"], marker='o', label='Calories Burned', linewidth=2)
plt.plot(df["Date"], df["Calories_Consumed"], marker='o', label='Calories Consumed', linewidth=2)
plt.title("Calories Burned vs Consumed", fontsize=18, weight='bold')
plt.ylabel("Calories (kcal)")
plt.xlabel("Date")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("calories_comparison.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x="Date", y="Water_Intake(ml)", data=df, marker='o', color='dodgerblue', linewidth=2)
plt.title("Daily Water Intake", fontsize=18, weight='bold')
plt.ylabel("Water Intake (ml)")
plt.xlabel("Date")
plt.axhline(2000, color='red', linestyle='--', label='Recommended Minimum (2000ml)')
plt.legend()
plt.tight_layout()
plt.savefig("water_intake.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x="Date", y="Sleep_Hours", data=df, color='orange')
plt.axhline(8, color='red', linestyle='--', label='Recommended 8 hrs')
plt.title("Sleep Duration Pattern", fontsize=18, weight='bold')
plt.ylabel("Hours of Sleep")
plt.xlabel("Date")
for i, val in enumerate(df["Sleep_Hours"]):
    plt.text(i, val + 0.1, f"{val}h", ha='center', fontsize=10)
plt.legend()
plt.tight_layout()
plt.savefig("sleep_pattern.png", dpi=300)
plt.show()

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(df["Date"], df["BMI"], marker='o', color='green', linewidth=2, label="BMI")
ax1.set_ylabel("BMI", color='green', fontsize=12)
ax1.tick_params(axis='y', labelcolor='green')
ax2 = ax1.twinx()
ax2.plot(df["Date"], df["BMR"], marker='s', color='purple', linewidth=2, label="BMR")
ax2.set_ylabel("BMR (kcal/day)", color='purple', fontsize=12)
ax2.tick_params(axis='y', labelcolor='purple')
plt.title("BMI vs BMR Comparison", fontsize=18, weight='bold')
fig.tight_layout()
plt.savefig("bmi_bmr_trend.png", dpi=300)
plt.show()

plt.figure(figsize=(6, 6))
progress_val = df["Progress(%)"].iloc[-1]
plt.pie(
    [progress_val, 100 - progress_val],
    labels=[f"Achieved {progress_val}%", "Remaining"],
    colors=["#4CAF50", "#D3D3D3"],
    autopct='%1.1f%%',
    startangle=90,
    explode=[0.05, 0]
)
plt.title("Overall Fitness Progress", fontsize=18, weight='bold')
plt.tight_layout()
plt.savefig("overall_progress.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 7))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Between Fitness Parameters", fontsize=18, weight='bold')
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=300)
plt.show()

df["Calorie_Balance"] = df["Calories_Consumed"] - df["Calories_Burned"]
plt.figure(figsize=(10, 6))
sns.barplot(x="Date", y="Calorie_Balance", data=df, palette="coolwarm")
plt.axhline(0, color='black', linestyle='--')
plt.title("Daily Caloric Balance (Consumed - Burned)", fontsize=18, weight='bold')
plt.ylabel("Calorie Balance (kcal)")
plt.xlabel("Date")
plt.tight_layout()
plt.savefig("calorie_balance.png", dpi=300)
plt.show()

print("\n=== WEEKLY SUMMARY ===")
print(f"Average Steps: {df['Steps'].mean():.0f}")
print(f"Average Sleep Hours: {df['Sleep_Hours'].mean():.1f} hrs")
print(f"Average Water Intake: {df['Water_Intake(ml)'].mean():.0f} ml")
print(f"Average Calorie Deficit: {df['Calorie_Balance'].mean():.0f} kcal")
print(f"Average Progress: {df['Progress(%)'].mean():.1f}%")
print("\nAll plots saved as high-resolution PNG files.")


