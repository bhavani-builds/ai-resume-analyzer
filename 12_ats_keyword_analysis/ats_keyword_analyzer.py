import re
from collections import Counter
from pathlib import Path


# ------------------------------------------
# Find project folder
# ------------------------------------------

project_folder = (
    Path(__file__).resolve().parent.parent
)


# ------------------------------------------
# Read resume
# ------------------------------------------

resume_file = (
    project_folder
    / "02_text_cleaning"
    / "cleaned_resume.txt"
)

with open(
    resume_file,
    "r",
    encoding="utf-8"
) as file:

    resume_text = file.read().lower()


# ------------------------------------------
# Read job description
# ------------------------------------------

job_file = (
    project_folder
    / "04_job_description"
    / "required_skills.txt"
)

with open(
    job_file,
    "r",
    encoding="utf-8"
) as file:

    job_skills = [
        line.strip().lower()
        for line in file
        if line.strip()
    ]


# ------------------------------------------
# Count keyword occurrences
# ------------------------------------------

keyword_counts = {}

for skill in job_skills:

    pattern = (
        r"\b"
        + re.escape(skill)
        + r"\b"
    )

    matches = re.findall(
        pattern,
        resume_text,
        re.IGNORECASE
    )

    keyword_counts[skill] = len(matches)


# ------------------------------------------
# Sort keywords
# ------------------------------------------

sorted_keywords = sorted(
    keyword_counts.items(),
    key=lambda item: item[1],
    reverse=True
)


# ------------------------------------------
# Display results
# ------------------------------------------

print("=" * 65)
print("              ATS KEYWORD ANALYZER")
print("=" * 65)

print(
    "\nJob-related keyword frequency:\n"
)


for keyword, count in sorted_keywords:

    if count > 0:

        status = "✓ Present"

    else:

        status = "✗ Missing"

    print(
        f"{keyword.title():25} "
        f"{count:3} times   {status}"
    )


# ------------------------------------------
# Calculate ATS keyword score
# ------------------------------------------

present_keywords = sum(
    1
    for count in keyword_counts.values()
    if count > 0
)


total_keywords = len(
    keyword_counts
)


if total_keywords > 0:

    ats_score = (
        present_keywords
        / total_keywords
    ) * 100

else:

    ats_score = 0


print("\n" + "=" * 65)

print(
    f"ATS Keyword Score: "
    f"{ats_score:.2f}%"
)

print("=" * 65)


# ------------------------------------------
# Recommendations
# ------------------------------------------

missing_keywords = [
    keyword
    for keyword, count in keyword_counts.items()
    if count == 0
]


print("\n🎯 KEYWORD RECOMMENDATIONS")

if missing_keywords:

    for keyword in missing_keywords:

        print(
            f"→ Consider adding: "
            f"{keyword.title()}"
        )

else:

    print(
        "Excellent! All detected job keywords "
        "are present in the resume."
    )


# ------------------------------------------
# Save report
# ------------------------------------------

output_file = (
    Path(__file__).resolve().parent
    / "ats_report.txt"
)


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "ATS KEYWORD ANALYSIS REPORT\n"
    )

    file.write(
        "=" * 50 + "\n\n"
    )

    file.write(
        f"ATS Keyword Score: "
        f"{ats_score:.2f}%\n\n"
    )

    file.write(
        "Keyword Frequency\n"
    )

    for keyword, count in sorted_keywords:

        file.write(
            f"{keyword}: {count}\n"
        )

    file.write(
        "\nMissing Keywords\n"
    )

    for keyword in missing_keywords:

        file.write(
            f"- {keyword}\n"
        )


print(
    "\nReport saved to:"
)

print(
    output_file
)
