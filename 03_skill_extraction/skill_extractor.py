import re
from pathlib import Path


# Find project folder
project_folder = Path(
    __file__
).resolve().parent.parent


# Resume text file
resume_file = (
    project_folder
    / "02_text_cleaning"
    / "cleaned_resume.txt"
)


# Read cleaned resume
with open(
    resume_file,
    "r",
    encoding="utf-8"
) as file:

    resume_text = file.read()


# Skills to search for
skills = [
    "python",
    "c",
    "java",
    "sql",
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "machine learning",
    "deep learning",
    "tensorflow",
    "keras",
    "opencv",
    "scikit-learn",
    "matlab",
    "vlsi",
    "embedded systems",
    "pcb design",
    "cadence",
    "proteus",
    "git",
    "github",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "mongodb"
]


# Find matching skills
found_skills = []

for skill in skills:

    pattern = r"\b" + re.escape(skill) + r"\b"

    if re.search(
        pattern,
        resume_text,
        re.IGNORECASE
    ):
        found_skills.append(skill)


# Display results
print("=" * 55)
print("          AI RESUME ANALYZER")
print("          SKILL EXTRACTION")
print("=" * 55)

print(
    f"\nTotal skills detected: "
    f"{len(found_skills)}\n"
)


if found_skills:

    for number, skill in enumerate(
        found_skills,
        start=1
    ):

        print(
            f"{number:02d}. {skill.title()}"
        )

else:

    print("No matching skills found.")


# Save detected skills
output_file = (
    Path(__file__).resolve().parent
    / "detected_skills.txt"
)


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    for skill in found_skills:
        file.write(
            skill + "\n"
        )


print("\n" + "-" * 55)

print(
    "Skill extraction completed!"
)

print(
    "Saved to:",
    output_file
)
