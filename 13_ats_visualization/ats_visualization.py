import matplotlib.pyplot as plt
from pathlib import Path


# Find project folder
project_folder = (
    Path(__file__).resolve().parent.parent
)


# ------------------------------------------
# Read ATS report
# ------------------------------------------

report_file = (
    project_folder
    / "12_ats_keyword_analysis"
    / "ats_report.txt"
)


with open(
    report_file,
    "r",
    encoding="utf-8"
) as file:

    report = file.read()


# ------------------------------------------
# Get ATS score
# ------------------------------------------

score = 0

for line in report.splitlines():

    if "ATS Keyword Score:" in line:

        score = float(
            line.split(":")[1]
            .replace("%", "")
            .strip()
        )


# ------------------------------------------
# Count present and missing keywords
# ------------------------------------------

present = 0
missing = 0

reading_keywords = False
reading_missing = False

for line in report.splitlines():

    if line == "Keyword Frequency":
        reading_keywords = True
        reading_missing = False
        continue

    if line == "Missing Keywords":
        reading_keywords = False
        reading_missing = True
        continue

    if reading_keywords and ":" in line:

        count = int(
            line.split(":")[-1]
            .strip()
        )

        if count > 0:
            present += 1

    elif reading_missing and line.startswith("-"):

        missing += 1


# ------------------------------------------
# Print results
# ------------------------------------------

print("=" * 60)
print("             ATS SCORE VISUALIZATION")
print("=" * 60)

print(
    f"\nATS Score        : {score:.2f}%"
)

print(
    f"Keywords Found  : {present}"
)

print(
    f"Keywords Missing: {missing}"
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
# ATS score donut
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
    f"{score:.0f}%\nATS",
    ha="center",
    va="center",
    fontsize=21,
    fontweight="bold"
)

axes[0].set_title(
    "ATS Keyword Score",
    fontsize=18,
    fontweight="bold"
)


# ------------------------------------------
# Keyword comparison
# ------------------------------------------

labels = [
    "Keywords Found",
    "Keywords Missing"
]

values = [
    present,
    missing
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
    "Keyword Coverage",
    fontsize=18,
    fontweight="bold"
)

axes[1].set_ylabel(
    "Number of Keywords"
)

axes[1].grid(
    axis="y",
    linestyle="--",
    alpha=0.4
)


# Values above bars
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
# Main title
# ------------------------------------------

fig.suptitle(
    "AI Resume Analyzer — ATS Dashboard",
    fontsize=22,
    fontweight="bold"
)

plt.tight_layout(
    rect=[0, 0, 1, 0.93]
)


# ------------------------------------------
# Save figure
# ------------------------------------------

output_file = (
    Path(__file__).resolve().parent
    / "Figure_13.png"
)

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print(
    "\nVisualization saved to:"
)

print(
    output_file
)
