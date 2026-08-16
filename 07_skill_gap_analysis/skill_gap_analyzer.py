from pathlib import Path


# Find project folder
project_folder = (
    Path(__file__).resolve().parent.parent
)


# ------------------------------------------
# Read resume skills
# ------------------------------------------

resume_file = (
    project_folder
    / "03_skill_extraction"
    / "detected_skills.txt"
)

with open(
    resume_file,
    "r",
    encoding="utf-8"
) as file:

    resume_skills = {
        line.strip().lower()
        for line in file
        if line.strip()
    }


# ------------------------------------------
# Read required job skills
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

    job_skills = {
        line.strip().lower()
        for line in file
        if line.strip()
    }


# ------------------------------------------
# Find missing skills
# ------------------------------------------

missing_skills = (
    job_skills - resume_skills
)


# ------------------------------------------
# Skill categories
# ------------------------------------------

skill_categories = {

    "Programming": [
        "python",
        "c",
        "java",
        "sql",
        "javascript"
    ],

    "AI / Machine Learning": [
        "machine learning",
        "deep learning",
        "tensorflow",
        "keras",
        "scikit-learn",
        "opencv"
    ],

    "Data Science": [
        "numpy",
        "pandas",
        "matplotlib",
        "scipy"
    ],

    "ECE / VLSI": [
        "vlsi",
        "embedded systems",
        "pcb design",
        "cadence",
        "proteus",
        "matlab"
    ],

    "Tools": [
        "git",
        "github"
    ],

    "Web Development": [
        "html",
        "css",
        "react",
        "node.js",
        "mongodb"
    ]
}


# ------------------------------------------
# Categorize missing skills
# ------------------------------------------

gap_analysis = {}

for category, skills in skill_categories.items():

    category_missing = []

    for skill in skills:

        if skill in missing_skills:

            category_missing.append(
                skill
            )

    if category_missing:

        gap_analysis[
            category
        ] = category_missing


# ------------------------------------------
# Display results
# ------------------------------------------

print("=" * 65)
print("              SKILL GAP ANALYZER")
print("=" * 65)


if not gap_analysis:

    print(
        "\n🎉 No major skill gaps found!"
    )

else:

    for category, skills in gap_analysis.items():

        print(
            f"\n📌 {category}"
        )

        print(
            "-" * 40
        )

        for skill in skills:

            print(
                f"   ❌ {skill.title()}"
            )


# ------------------------------------------
# Recommendations
# ------------------------------------------

print(
    "\n" + "=" * 65
)

print(
    "RECOMMENDATIONS"
)

print(
    "=" * 65
)


recommendations = {

    "Programming":
        "Practice coding, problem solving and SQL.",

    "AI / Machine Learning":
        "Learn ML algorithms, model evaluation and neural networks.",

    "Data Science":
        "Practice NumPy, Pandas, visualization and data analysis.",

    "ECE / VLSI":
        "Strengthen embedded systems, VLSI and PCB design concepts.",

    "Tools":
        "Practice Git, GitHub and collaborative development.",

    "Web Development":
        "Learn frontend, backend and database technologies."
}


for category in gap_analysis:

    print(
        f"\n{category}:"
    )

    print(
        recommendations[category]
    )


# ------------------------------------------
# Save report
# ------------------------------------------

output_file = (
    Path(__file__).resolve().parent
    / "skill_gap_report.txt"
)


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "AI RESUME ANALYZER\n"
    )

    file.write(
        "SKILL GAP ANALYSIS\n"
    )

    file.write(
        "=" * 50 + "\n\n"
    )


    for category, skills in gap_analysis.items():

        file.write(
            f"{category}\n"
        )

        for skill in skills:

            file.write(
                f"- {skill.title()}\n"
            )

        file.write("\n")


print(
    "\nSkill gap report saved to:"
)

print(
    output_file
)
