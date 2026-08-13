import re
from pathlib import Path


# ------------------------------------------
# Project paths
# ------------------------------------------

project_folder = (
    Path(__file__).resolve().parent.parent
)


# ------------------------------------------
# Job description
# ------------------------------------------

job_description = """
We are looking for an Electronics and Software Engineer.

Required skills:

Python
C
Machine Learning
NumPy
Pandas
Matplotlib
MATLAB
Embedded Systems
VLSI
PCB Design
Git
GitHub
SQL
"""

# Convert job description to lowercase
job_text = job_description.lower()


# ------------------------------------------
# Skills database
# ------------------------------------------

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


# ------------------------------------------
# Find required skills
# ------------------------------------------

required_skills = []

for skill in skills:

    pattern = (
        r"\b"
        + re.escape(skill)
        + r"\b"
    )

    if re.search(
        pattern,
        job_text,
        re.IGNORECASE
    ):

        required_skills.append(
            skill
        )


# ------------------------------------------
# Display results
# ------------------------------------------

print("=" * 60)
print("           JOB DESCRIPTION ANALYSIS")
print("=" * 60)

print(
    f"\nRequired skills detected: "
    f"{len(required_skills)}\n"
)


for number, skill in enumerate(
    required_skills,
    start=1
):

    print(
        f"{number:02d}. {skill.title()}"
    )


# ------------------------------------------
# Save results
# ------------------------------------------

output_file = (
    Path(__file__).resolve().parent
    / "required_skills.txt"
)


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    for skill in required_skills:

        file.write(
            skill + "\n"
        )


print("\n" + "-" * 60)

print(
    "Job description analysis completed!"
)

print(
    "Saved to:",
    output_file
)
