from pathlib import Path


# ------------------------------------------
# Find project folder
# ------------------------------------------

project_folder = (
    Path(__file__).resolve().parent.parent
)


# ------------------------------------------
# Read missing skills
# ------------------------------------------

report_file = (
    project_folder
    / "07_skill_gap_analysis"
    / "skill_gap_report.txt"
)


# Skill recommendations
recommendations = {

    "python":
        "Practice Python programming, functions, OOP and problem solving.",

    "c":
        "Strengthen C programming, pointers, arrays and memory concepts.",

    "java":
        "Learn Java OOP, collections and exception handling.",

    "sql":
        "Practice SQL queries, joins, grouping and database design.",

    "numpy":
        "Practice numerical computing and array operations with NumPy.",

    "pandas":
        "Learn data cleaning, filtering and analysis using Pandas.",

    "machine learning":
        "Study supervised learning, classification, regression and model evaluation.",

    "deep learning":
        "Learn neural networks, CNNs, optimization and model training.",

    "tensorflow":
        "Practice building and training neural networks using TensorFlow.",

    "keras":
        "Learn how to create and train deep learning models with Keras.",

    "opencv":
        "Practice image processing, object detection and computer vision.",

    "matlab":
        "Practice numerical analysis, simulations and signal processing in MATLAB.",

    "vlsi":
        "Strengthen digital design, CMOS, Verilog and VLSI concepts.",

    "embedded systems":
        "Learn microcontrollers, sensors, communication protocols and embedded C.",

    "pcb design":
        "Practice schematic design, PCB layout, routing and design rules.",

    "cadence":
        "Practice schematic capture, simulation and IC design using Cadence tools.",

    "proteus":
        "Practice circuit simulation and microcontroller-based projects.",

    "git":
        "Learn branching, commits, merging and collaborative Git workflows.",

    "github":
        "Practice repositories, pull requests, issues and GitHub workflows.",

    "html":
        "Learn semantic HTML and modern webpage structure.",

    "css":
        "Practice responsive layouts, Flexbox, Grid and modern CSS.",

    "javascript":
        "Learn JavaScript fundamentals, DOM manipulation and asynchronous programming.",

    "react":
        "Build React applications using components, hooks and state management.",

    "mongodb":
        "Learn document databases, CRUD operations and MongoDB queries."
}


# ------------------------------------------
# Extract missing skills
# ------------------------------------------

missing_skills = []

with open(
    report_file,
    "r",
    encoding="utf-8"
) as file:

    for line in file:

        if line.startswith("- "):

            skill = (
                line[2:]
                .strip()
                .lower()
            )

            missing_skills.append(
                skill
            )


# ------------------------------------------
# Display recommendations
# ------------------------------------------

print("=" * 65)
print("              AI RESUME RECOMMENDATIONS")
print("=" * 65)


if not missing_skills:

    print(
        "\n🎉 No skill gaps found!"
    )

    print(
        "Your resume matches all detected job requirements."
    )

else:

    print(
        f"\nFound {len(missing_skills)} skill gaps.\n"
    )

    for number, skill in enumerate(
        missing_skills,
        start=1
    ):

        print(
            f"{number}. {skill.title()}"
        )

        recommendation = recommendations.get(
            skill,
            "Build practical projects and gain hands-on experience in this area."
        )

        print(
            f"   → {recommendation}\n"
        )


# ------------------------------------------
# Save recommendations
# ------------------------------------------

output_file = (
    Path(__file__).resolve().parent
    / "learning_recommendations.txt"
)


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "AI RESUME LEARNING RECOMMENDATIONS\n"
    )

    file.write(
        "=" * 50 + "\n\n"
    )

    for skill in missing_skills:

        file.write(
            f"{skill.title()}\n"
        )

        file.write(
            f"{recommendations.get(skill, 'Build practical projects and gain hands-on experience.')}\n\n"
        )


print(
    "Recommendations saved to:"
)

print(
    output_file
)
