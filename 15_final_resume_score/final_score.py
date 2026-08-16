from pathlib import Path
import re


# ------------------------------------------
# Find project folder
# ------------------------------------------

project_folder = (
    Path(__file__).resolve().parent.parent
)


# ------------------------------------------
# Helper function
# ------------------------------------------

def read_file(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


# ------------------------------------------
# 1. Resume-Job Match Score
# ------------------------------------------

match_file = (
    project_folder
    / "05_resume_job_matching"
    / "match_report.txt"
)

match_report = read_file(
    match_file
)

match_score = 0

match_result = re.search(
    r"Resume Match Score:\s*([\d.]+)%",
    match_report
)

if match_result:

    match_score = float(
        match_result.group(1)
    )


# ------------------------------------------
# 2. ATS Score
# ------------------------------------------

ats_file = (
    project_folder
    / "12_ats_keyword_analysis"
    / "ats_report.txt"
)

ats_report = read_file(
    ats_file
)

ats_score = 0

ats_result = re.search(
    r"ATS Keyword Score:\s*([\d.]+)%",
    ats_report
)

if ats_result:

    ats_score = float(
        ats_result.group(1)
    )


# ------------------------------------------
# 3. Section Quality Score
# ------------------------------------------

section_file = (
    project_folder
    / "14_resume_section_analysis"
    / "section_analysis.txt"
)

section_report = read_file(
    section_file
)

section_score = 0

section_result = re.search(
    r"Section Score:\s*([\d.]+)%",
    section_report
)

if section_result:

    section_score = float(
        section_result.group(1)
    )


# ------------------------------------------
# 4. Resume Strength Score
# ------------------------------------------

resume_file = (
    project_folder
    / "02_text_cleaning"
    / "cleaned_resume.txt"
)

resume_text = read_file(
    resume_file
).lower()


# Important resume elements
strength_points = 0


if "education" in resume_text:
    strength_points += 20

if "skills" in resume_text:
    strength_points += 20

if "project" in resume_text:
    strength_points += 20

if "experience" in resume_text or "internship" in resume_text:
    strength_points += 15

if "certification" in resume_text:
    strength_points += 10

if "achievement" in resume_text or "award" in resume_text:
    strength_points += 10

if "github" in resume_text or "linkedin" in resume_text:
    strength_points += 5


strength_score = min(
    strength_points,
    100
)


# ------------------------------------------
# Final weighted score
# ------------------------------------------

final_score = (
    match_score * 0.35
    + ats_score * 0.25
    + section_score * 0.20
    + strength_score * 0.20
)


# ------------------------------------------
# Grade
# ------------------------------------------

if final_score >= 90:

    grade = "Excellent"

elif final_score >= 80:

    grade = "Very Good"

elif final_score >= 70:

    grade = "Good"

elif final_score >= 60:

    grade = "Average"

else:

    grade = "Needs Improvement"


# ------------------------------------------
# Display results
# ------------------------------------------

print("=" * 65)
print("                 FINAL RESUME ANALYSIS")
print("=" * 65)

print(
    f"\nResume-Job Match : {match_score:.2f}%"
)

print(
    f"ATS Score        : {ats_score:.2f}%"
)

print(
    f"Section Quality  : {section_score:.2f}%"
)

print(
    f"Resume Strength  : {strength_score:.2f}%"
)

print("\n" + "-" * 65)

print(
    f"🏆 FINAL RESUME SCORE: "
    f"{final_score:.2f}/100"
)

print(
    f"📌 Overall Grade: {grade}"
)

print("-" * 65)


# ------------------------------------------
# Recommendation
# ------------------------------------------

print("\nRECOMMENDATION")
print("-" * 65)

if final_score >= 90:

    print(
        "🔥 Excellent resume! "
        "You are strongly prepared for this job."
    )

elif final_score >= 80:

    print(
        "🚀 Very good resume! "
        "A few improvements can make it stronger."
    )

elif final_score >= 70:

    print(
        "👍 Good resume. "
        "Focus on improving your missing skills and keywords."
    )

elif final_score >= 60:

    print(
        "⚠️ Average resume. "
        "Add stronger projects, skills and achievements."
    )

else:

    print(
        "📈 Your resume needs improvement. "
        "Work on skills, projects, keywords and experience."
    )


# ------------------------------------------
# Save final report
# ------------------------------------------

output_file = (
    Path(__file__).resolve().parent
    / "final_resume_report.txt"
)


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "AI RESUME ANALYZER - FINAL REPORT\n"
    )

    file.write(
        "=" * 50 + "\n\n"
    )

    file.write(
        f"Resume-Job Match : {match_score:.2f}%\n"
    )

    file.write(
        f"ATS Score        : {ats_score:.2f}%\n"
    )

    file.write(
        f"Section Quality  : {section_score:.2f}%\n"
    )

    file.write(
        f"Resume Strength  : {strength_score:.2f}%\n\n"
    )

    file.write(
        f"FINAL SCORE      : {final_score:.2f}/100\n"
    )

    file.write(
        f"GRADE            : {grade}\n"
    )


print(
    "\nFinal report saved to:"
)

print(
    output_file
)
