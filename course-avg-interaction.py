import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("/Users/chanrattnakmong/Desktop/TILT/TILT_Projects/course-avg-interaction-per-student.csv")

# Handle possible nulls
df['AVG_INTERACTION_PER_STUDENT'] = df['AVG_INTERACTION_PER_STUDENT'].fillna(0)

# Define bins up to 140
max_x = 140
bins = list(range(0, max_x + 10, 10))  # 0,10,20,...,140
labels = [f"{i}-{i+10}" for i in range(0, max_x, 10)]

# Assign each student-course instance to a range
df['interaction_range'] = pd.cut(
    df['AVG_INTERACTION_PER_STUDENT'],
    bins=bins,
    labels=labels,
    right=False,
    include_lowest=True
)

# Count number of student-course instances per range
hist_data = df['interaction_range'].value_counts().sort_index()

# Plot histogram
plt.figure(figsize=(14, 7))
bars = plt.bar(hist_data.index, hist_data.values, width=0.8, color='skyblue')

# Add grid background
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set Y-axis range and ticks (10, 20, 30, ...)
max_y = int(hist_data.max() / 10 + 1) * 10
plt.ylim(0, max_y)
plt.yticks(range(0, max_y + 1, 10))

# Labels and title
plt.xlabel("Average Interaction Range", fontsize=10)
plt.ylabel("Number of Virtual Courses", fontsize=10)
plt.title("Distribution of Virtual Courses by Average Interactions Per Student", fontsize=12)

# Rotate X-axis labels and make font smaller
plt.xticks(rotation=45, fontsize=8)

# Highlight highest bar dynamically
max_index = hist_data.idxmax()
for bar, label in zip(bars, hist_data.index):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height, f'{int(height)}', 
             ha='center', va='bottom', fontsize=7)
    if label == max_index:
        bar.set_color('orange')  # highlight the highest bin

plt.tight_layout()
plt.show()
