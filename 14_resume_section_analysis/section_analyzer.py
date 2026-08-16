from pathlib import Path


# ------------------------------------------
# Find project folder
# ------------------------------------------

project_folder = (
    Path(__file__).resolve().parent.parent
)


# ------------------------------------------
# Read cleaned resume
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

    resume = file.read().lower()


# ------------------------------------------
# Resume sections
# ------------------------------------------

sections = {

    "Professional Summary": [
        "summary",
        "objective",
        "profile"
    ],

    "Education": [
        "education",
        "b.tech",
        "degree",
        "bachelor",
        "diploma"
    ],

    "Technical Skills": [
        "technical skills",
        "skills",
        "programming languages"
    ],

    "Projects": [
        "projects",
        "project experience"
    ],

    "Internships / Experience": [
        "internship",
        "internships",
        "experience",
        "work experience"
    ],

    "Certifications": [
        "certifications",
        "certification",
        "certificates"
    ],

    "Achievements": [
        "achievements",
        "awards",
        "prizes"
    ],

    "Links": [
        "github",
        "linkedin",
        "portfolio"
    ]
}


# ------------------------------------------
# Check sections
# ------------------------------------------

results = {}

for section, keywords in sections.items():

    found = False

    for keyword in keywords:

        if keyword in resume:

            found = True
            break

    results[section] = found


# ------------------------------------------
# Calculate score
# ------------------------------------------

total_sections = len(results)

completed_sections = sum(
    results.values()
)

section_score = (
    completed_sections
    / total_sections
) * 100


# ------------------------------------------
# Display analysis
# ------------------------------------------

print("=" * 65)
print("             RESUME SECTION ANALYZER")
print("=" * 65)

print(
    f"\nSection Score: "
    f"{section_score:.2f}%"
)

print(
    f"Sections Found: "
    f"{completed_sections}/{total_sections}\n"
)


for section, found in results.items():

    if found:

        print(
            f"✅ {section}"
        )

    else:

        print(
            f"❌ {section}"
        )


# ------------------------------------------
# Recommendations
# ------------------------------------------

print("\n" + "=" * 65)
print("RECOMMENDATIONS")
print("=" * 65)


missing_sections = [
    section
    for section, found in results.items()
    if not found
]


if missing_sections:

    for section in missing_sections:

        print(
            f"→ Consider adding a "
            f"{section} section."
        )

else:

    print(
        "🎉 All important resume sections "
        "were detected!"
    )


# ------------------------------------------
# Save report
# ------------------------------------------

output_file = (
    Path(__file__).resolve().parent
    / "section_analysis.txt"
)


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "RESUME SECTION ANALYSIS\n"
    )

    file.write(
        "=" * 50 + "\n\n"
    )

    file.write(
        f"Section Score: "
        f"{section_score:.2f}%\n\n"
    )

    for section, found in results.items():

        status = (
            "Present"
            if found
            else "Missing"
        )

        file.write(
            f"{section}: {status}\n"
        )


    file.write(
        "\nRecommendations\n"
    )

    for section in missing_sections:

        file.write(
            f"- Add {section}\n"
        )


print(
    "\nReport saved to:"
)

print(
    output_file
)
