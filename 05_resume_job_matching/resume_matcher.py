from pathlib import Path


# ------------------------------------------
# Find project folder
# ------------------------------------------

project_folder = (
    Path(__file__).resolve().parent.parent
)


# ------------------------------------------
# File locations
# ------------------------------------------

resume_skills_file = (
    project_folder
    / "03_skill_extraction"
    / "detected_skills.txt"
)

job_skills_file = (
    project_folder
    / "04_job_description"
    / "required_skills.txt"
)


# ------------------------------------------
# Read resume skills
# ------------------------------------------

with open(
    resume_skills_file,
    "r",
    encoding="utf-8"
) as file:

    resume_skills = [
        line.strip().lower()
        for line in file
        if line.strip()
    ]


# ------------------------------------------
# Read job skills
# ------------------------------------------

with open(
    job_skills_file,
    "r",
    encoding="utf-8"
) as file:

    job_skills = [
        line.strip().lower()
        for line in file
        if line.strip()
    ]


# ------------------------------------------
# Find matching skills
# ------------------------------------------

matching_skills = []

missing_skills = []


for skill in job_skills:

    if skill in resume_skills:

        matching_skills.append(
            skill
        )

    else:

        missing_skills.append(
            skill
        )


# ------------------------------------------
# Calculate match percentage
# ------------------------------------------

if len(job_skills) > 0:

    match_percentage = (
        len(matching_skills)
        / len(job_skills)
    ) * 100

else:

    match_percentage = 0


# ------------------------------------------
# Display results
# ------------------------------------------

print("=" * 60)
print("           RESUME vs JOB MATCH")
print("=" * 60)


print("\n✅ MATCHING SKILLS")

if matching_skills:

    for skill in matching_skills:

        print(
            "   ✓",
            skill.title()
        )

else:

    print(
        "   No matching skills found."
    )


print("\n❌ MISSING SKILLS")

if missing_skills:

    for skill in missing_skills:

        print(
            "   ✗",
            skill.title()
        )

else:

    print(
        "   No missing skills!"
    )


print("\n" + "-" * 60)

print(
    f"Resume Match Score: "
    f"{match_percentage:.2f}%"
)

print("-" * 60)


# ------------------------------------------
# Save report
# ------------------------------------------

report_file = (
    Path(__file__).resolve().parent
    / "match_report.txt"
)


with open(
    report_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "RESUME vs JOB MATCH REPORT\n"
    )

    file.write(
        "=" * 40 + "\n\n"
    )

    file.write(
        "MATCHING SKILLS\n"
    )

    for skill in matching_skills:

        file.write(
            f"✓ {skill.title()}\n"
        )


    file.write(
        "\nMISSING SKILLS\n"
    )

    for skill in missing_skills:

        file.write(
            f"✗ {skill.title()}\n"
        )


    file.write(
        f"\nMATCH SCORE: "
        f"{match_percentage:.2f}%\n"
    )


print(
    "\nMatch report saved as:"
)

print(
    report_file
)
