import matplotlib.pyplot as plt
from pathlib import Path


# Find project folder
project_folder = (
    Path(__file__).resolve().parent.parent
)


# Read the matching report
report_file = (
    project_folder
    / "05_resume_job_matching"
    / "match_report.txt"
)


with open(
    report_file,
    "r",
    encoding="utf-8"
) as file:

    report = file.read()


# ------------------------------------------
# Extract match score
# ------------------------------------------

score_line = [
    line
    for line in report.splitlines()
    if "MATCH SCORE" in line
]


if score_line:

    score = float(
        score_line[0]
        .split(":")[1]
        .replace("%", "")
        .strip()
    )

else:

    score = 0


missing_count = 0
matching_count = 0

for line in report.splitlines():

    if line.startswith("✓"):
        matching_count += 1

    elif line.startswith("✗"):
        missing_count += 1


total_skills = (
    matching_count + missing_count
)


# ------------------------------------------
# Display information
# ------------------------------------------

print("=" * 55)
print("           RESUME MATCH ANALYSIS")
print("=" * 55)

print(
    f"\nMatch Score       : {score:.2f}%"
)

print(
    f"Matching Skills   : {matching_count}"
)

print(
    f"Missing Skills    : {missing_count}"
)

print(
    f"Total Job Skills  : {total_skills}"
)


# ------------------------------------------
# Create dashboard
# ------------------------------------------

fig, axes = plt.subplots(
    1,
    2,
    figsize=(14, 6)
)


# ------------------------------------------
# Donut chart
# ------------------------------------------

axes[0].pie(
    [score, 100 - score],
    labels=[
        "Matched",
        "Remaining"
    ],
    autopct="%1.1f%%",
    startangle=90,
    colors=[
        "mediumseagreen",
        "lightgray"
    ],
    wedgeprops={
        "width": 0.38,
        "edgecolor": "white"
    }
)

axes[0].text(
    0,
    0,
    f"{score:.1f}%\nMatch",
    ha="center",
    va="center",
    fontsize=20,
    fontweight="bold"
)

axes[0].set_title(
    "Resume–Job Match Score",
    fontsize=18,
    fontweight="bold"
)


# ------------------------------------------
# Skill comparison
# ------------------------------------------

labels = [
    "Matching Skills",
    "Missing Skills"
]

values = [
    matching_count,
    missing_count
]

bars = axes[1].bar(
    labels,
    values,
    color=[
        "royalblue",
        "crimson"
    ],
    width=0.55
)

axes[1].set_title(
    "Skill Comparison",
    fontsize=18,
    fontweight="bold"
)

axes[1].set_ylabel(
    "Number of Skills"
)

axes[1].grid(
    axis="y",
    linestyle="--",
    alpha=0.4
)


# Add numbers above bars
for bar in bars:

    axes[1].text(
        bar.get_x()
        + bar.get_width() / 2,
        bar.get_height(),
        str(int(bar.get_height())),
        ha="center",
        va="bottom",
        fontsize=14,
        fontweight="bold"
    )


# ------------------------------------------
# Overall title
# ------------------------------------------

fig.suptitle(
    "AI Resume Analyzer — Match Dashboard",
    fontsize=22,
    fontweight="bold"
)

plt.tight_layout(
    rect=[0, 0, 1, 0.93]
)


# Save figure
output_file = (
    Path(__file__).resolve().parent
    / "Figure_6.png"
)

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print(
    "\nDashboard saved as:"
)

print(
    output_file
)
