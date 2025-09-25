import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("/Users/chanrattnakmong/Desktop/TILT/TILT_Projects/virtual-course-interaction-per-student-per-course.csv")

# Handle possible nulls in total interactions
df['STUDENT_INTERACTIONS'] = df['STUDENT_INTERACTIONS'].fillna(0)

# Determine max value for bins
max_val = int(df['STUDENT_INTERACTIONS'].max()) + 10

# Define bins and labels
bins = list(range(0, max_val + 10, 10))  # 0,10,20,...,max_val
labels = [f"{i}-{i+10}" for i in range(0, max_val, 10)]

# Assign each student-course instance to a range
df['interaction_range'] = pd.cut(
    df['STUDENT_INTERACTIONS'],
    bins=bins,
    labels=labels,
    right=False,       # left-inclusive, right-exclusive
    include_lowest=True
)

# Count number of student-course instances per range
hist_data = df['interaction_range'].value_counts().sort_index()

# Plot histogram
plt.figure(figsize=(14, 7))
bars = plt.bar(hist_data.index, hist_data.values, width=0.8, color='skyblue')  # wider bars

# Add grid background
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set Y-axis range and ticks
plt.ylim(0, 2200)
plt.yticks(range(0, 2201, 200))

# Labels and title
plt.xlabel("Total Interaction Range", fontsize=10)
plt.ylabel("Number of Student-Course Instances", fontsize=10)
plt.title("Distribution of Student-Course Instances by Total Interactions", fontsize=12)

# Rotate X-axis labels and make font smaller
plt.xticks(rotation=45, fontsize=8)

# Add value labels on top of bars (smaller font)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height, f'{int(height)}', ha='center', va='bottom', fontsize=7)

plt.tight_layout()
plt.show()
