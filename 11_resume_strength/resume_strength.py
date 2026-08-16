import re


# ------------------------------------------
# Get resume text
# ------------------------------------------

with open(
    "../02_text_cleaning/cleaned_resume.txt",
    "r",
    encoding="utf-8"
) as file:

    resume = file.read().lower()


# ------------------------------------------
# Resume sections
# ------------------------------------------

sections = {
    "Education": [
        "education",
        "degree",
        "b.tech",
        "bachelor"
    ],

    "Skills": [
        "skills",
        "technical skills",
        "programming"
    ],

    "Projects": [
        "projects",
        "project"
    ],

    "Experience": [
        "experience",
        "internship",
        "intern"
    ],

    "Certifications": [
        "certification",
        "certificate"
    ],

    "Achievements": [
        "achievement",
        "award",
        "prize"
    ]
}


# ------------------------------------------
# Check sections
# ------------------------------------------

section_scores = {}

for section, keywords in sections.items():

    found = False

    for keyword in keywords:

        if keyword in resume:

            found = True
            break

    if found:

        section_scores[section] = 1

    else:

        section_scores[section] = 0


# ------------------------------------------
# Detect technical skills
# ------------------------------------------

skills = [
    "python",
    "c",
    "java",
    "sql",
    "numpy",
    "pandas",
    "matlab",
    "machine learning",
    "deep learning",
    "tensorflow",
    "opencv",
    "vlsi",
    "embedded systems",
    "pcb design",
    "cadence",
    "proteus",
    "git",
    "github",
    "react",
    "javascript",
    "mongodb"
]


found_skills = []

for skill in skills:

    if skill in resume:

        found_skills.append(
            skill
        )


# ------------------------------------------
# Skill score
# ------------------------------------------

skill_score = min(
    len(found_skills) * 3,
    20
)


# ------------------------------------------
# Section score
# ------------------------------------------

section_score = (
    sum(section_scores.values())
    / len(section_scores)
) * 40


# ------------------------------------------
# Extra profile elements
# ------------------------------------------

extra_score = 0


if "linkedin" in resume:

    extra_score += 10


if "github" in resume:

    extra_score += 10


if "email" in resume or "@" in resume:

    extra_score += 5


if "phone" in resume:

    extra_score += 5


# ------------------------------------------
# Final score
# ------------------------------------------

final_score = min(
    skill_score
    + section_score
    + extra_score,
    100
)


# ------------------------------------------
# Display
# ------------------------------------------

print("=" * 60)
print("             RESUME STRENGTH ANALYZER")
print("=" * 60)

print(
    f"\nOverall Resume Score: "
    f"{final_score:.1f}/100"
)


print("\nSection Analysis")
print("-" * 40)

for section, value in section_scores.items():

    status = (
        "✓ Present"
        if value
        else "✗ Missing"
    )

    print(
        f"{section:15} : {status}"
    )


print("\nTechnical Skills")
print("-" * 40)

print(
    f"Skills detected: "
    f"{len(found_skills)}"
)


for skill in found_skills:

    print(
        f"✓ {skill.title()}"
    )


# ------------------------------------------
# Overall feedback
# ------------------------------------------

print("\n" + "=" * 60)
print("RECOMMENDATION")
print("=" * 60)


if final_score >= 80:

    print(
        "🔥 Strong resume! Keep improving "
        "with measurable achievements."
    )

elif final_score >= 60:

    print(
        "👍 Good resume. Add more projects, "
        "skills and measurable achievements."
    )

else:

    print(
        "📈 Your resume needs improvement. "
        "Focus on projects, skills and achievements."
    )
