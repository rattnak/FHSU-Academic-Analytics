import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Step 1: Load CSV ===
df = pd.read_csv("student-instructor-interaction.csv")

# === Step 2: Normalize column names ===
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("Normalized columns:", df.columns.tolist())

# === Step 3: Select needed columns ===
required_cols = ["course_id", "instructor_interaction_count", "avg_interaction_per_student"]

missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise ValueError(f"Missing expected columns in CSV: {missing}")

df = df[required_cols].dropna()

# === Step 4: Correlation analysis ===
corr = df["instructor_interaction_count"].corr(df["avg_interaction_per_student"])
r_squared = corr**2
print(f"Correlation between instructor and student interaction: {corr:.2f}")
print(f"R² (variance explained): {r_squared:.2f}")

# === Step 5: Visualization ===
plt.figure(figsize=(8,6))
ax = sns.regplot(
    data=df,
    x="instructor_interaction_count",
    y="avg_interaction_per_student",
    scatter_kws={"alpha":0.6}
)

# Annotate correlation + R² on the plot
plt.text(
    0.05, 0.95,
    f"r = {corr:.2f}\nR² = {r_squared:.2f}",
    transform=ax.transAxes,
    fontsize=12,
    verticalalignment="top",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.6)
)

# Titles and labels
plt.title("Instructor vs Student Interaction per Course\nHypothesis: More active instructors => More active students")
plt.xlabel("Instructor Interaction Count (per course)")
plt.ylabel("Average Student Interaction (per student)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
