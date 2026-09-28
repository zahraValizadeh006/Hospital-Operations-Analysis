import pandas as pd

# Step 1: Read the CSV file
df =pd.read_csv("hospital_operations.csv")# Read the file here

# Step2: Verify that data was loaded correctly
print("Number of rows:",df.shape[0])
print("\nColumn names:",df.columns)
print("\nFirst 5 rows:")
print(df.head())

# Step 3: Group by department and calculate average cost and length of stay
dept_summary = df.groupby("Department").agg(
    Avg_Cost=("Cost",'mean'),
    Avg_Stay=("Length_of_Stay",'mean')
).round(2).reset_index()

print("Department Summary:")
print(dept_summary)

# Step 4: Sort by average cost (descending)
dept_summary_sorted = dept_summary.sort_values(by="Avg_Cost", ascending=False)

print("\nSorted Department Summary:")
print(dept_summary_sorted)

import matplotlib.pyplot as plt
import seaborn as sns

# Step 5: Plot horizontal bar chart for Average Cost
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=dept_summary_sorted, x='Department', y='Avg_Cost', palette='Blues_r', order=dept_summary_sorted['Department'])
for container in ax.containers:
    ax.bar_label(container, fmt='$%d', fontweight='bold', fontsize=10, padding=3)
plt.title('Average Cost per Patient by Department', fontsize=14, fontweight='bold')
plt.xlabel('Department', fontsize=12)
plt.ylabel('Average Cost (USD)', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Adjust layout to make room for text
plt.subplots_adjust(bottom=0.25)  # Create space at the bottom

# Add Insights Text
insights_text = (
    "KEY INSIGHTS:\n"
    "1. ICU and Surgery have highest costs ($2500+).\n"
    "2. Emergency shows lowest costs ($800).\n"
    "RECOMMENDATION: Optimize ICU patient flow."
)

plt.figtext(0.5, -0.05, insights_text, ha='center', fontsize=9, 
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.2))

# Save and Show
plt.savefig('cost_analysis.png', dpi=300, bbox_inches='tight') # bbox_inches is critical!
plt.show()
# CHART 2: Average Length of Stay
import matplotlib.pyplot as plt
import seaborn as sns

# COMBINED CHART: Cost & Length of Stay

# Create a figure with 2 subplots side by side (1 row, 2 columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- LEFT CHART: Average Cost (Blue) ---
sns.barplot(
    data=dept_summary_sorted,
    x='Department',
    y='Avg_Cost',
    palette='Blues_r',
    ax=ax1,  # Plot on the left axis
    order=dept_summary_sorted['Department']
)
ax1.set_title('Average Cost per Patient', fontsize=13, fontweight='bold')
ax1.set_xlabel('Department', fontsize=11)
ax1.set_ylabel('Cost (USD)', fontsize=11)
ax1.tick_params(axis='x', rotation=45)

# Add labels on top of ALL bars (Left chart)
for container in ax1.containers:
    ax1.bar_label(container, fmt='$%d', fontweight='bold', fontsize=9, padding=3)

# --- RIGHT CHART: Average Length of Stay (Green) ---
sns.barplot(
    data=dept_summary_sorted,
    x='Department',
    y='Avg_Stay',
    palette='Greens_r',
    ax=ax2,  # Plot on the right axis
    order=dept_summary_sorted['Department']
)
ax2.set_title('Average Length of Stay', fontsize=13, fontweight='bold')
ax2.set_xlabel('Department', fontsize=11)
ax2.set_ylabel('Days', fontsize=11)
ax2.tick_params(axis='x', rotation=45)

# Add labels on top of ALL bars (Right chart)
for container in ax2.containers:
    ax2.bar_label(container, fmt='%d days', fontweight='bold', fontsize=9, padding=3)

# --- MAIN TITLE (Above both charts) ---
fig.suptitle('Hospital Department Analysis: Cost vs. Length of Stay', 
             fontsize=16, fontweight='bold', y=1.02)

# Adjust layout to make room for text at the bottom
plt.subplots_adjust(bottom=0.30, top=0.88, wspace=0.3)

# --- INSIGHTS TEXT (Below both charts) ---
insights_text = (
    "KEY INSIGHT: There is a direct correlation between Length of Stay and Total Cost.\n"
    "Departments with longer stays (e.g., Surgery, ICU) naturally incur higher daily expenses.\n"
    "RECOMMENDATION: Focus on optimizing patient flow in high-cost departments."
)

plt.figtext(
    0.5, 0.02, insights_text,
    ha='center', fontsize=10, fontweight='bold', color='darkblue',
    bbox=dict(boxstyle='round,pad=0.8', facecolor='#f0f8ff', edgecolor='blue', alpha=0.3)
)

# Save and Show
plt.savefig('combined_analysis.png', dpi=300, bbox_inches='tight')
print("✅ Combined plot saved successfully: combined_analysis.png")

plt.show()
# Step Final: Save the summarized data to a new CSV file
dept_summary_sorted.to_csv('department_summary.csv', index=False)
print("✅ Summary data saved: department_summary.csv")
# Save the summarized data to a new CSV file
dept_summary_sorted.to_csv('department_summary.csv', index=False)
print("✅ Summary data saved: department_summary.csv")