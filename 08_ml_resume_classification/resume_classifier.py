import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# ------------------------------------------
# Create sample resume dataset
# ------------------------------------------

data = {

    "resume": [

        "python java javascript react node mongodb software development",
        "python java html css javascript web development",
        "c java javascript react frontend backend software engineer",

        "python pandas numpy machine learning data analysis",
        "python pandas matplotlib scipy data science statistics",
        "numpy pandas machine learning data visualization python",

        "python tensorflow keras deep learning neural networks",
        "machine learning deep learning tensorflow computer vision",
        "python artificial intelligence neural networks keras",

        "vlsi verilog cadence digital electronics",
        "embedded systems pcb design microcontrollers vlsi",
        "matlab proteus pcb design electronics embedded systems"
    ],

    "category": [

        "Software",
        "Software",
        "Software",

        "Data Science",
        "Data Science",
        "Data Science",

        "AI/ML",
        "AI/ML",
        "AI/ML",

        "ECE/VLSI",
        "ECE/VLSI",
        "ECE/VLSI"
    ]
}


df = pd.DataFrame(data)


print("=" * 60)
print("          ML RESUME CLASSIFICATION")
print("=" * 60)

print(
    "\nDataset size:",
    df.shape
)

print(
    "\nCategories:"
)

print(
    df["category"].value_counts()
)


# ------------------------------------------
# Split data
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    df["resume"],
    df["category"],
    test_size=0.25,
    random_state=42,
    stratify=df["category"]
)


# ------------------------------------------
# Convert text into numerical features
# ------------------------------------------

vectorizer = TfidfVectorizer(
    stop_words="english"
)

X_train_tfidf = vectorizer.fit_transform(
    X_train
)

X_test_tfidf = vectorizer.transform(
    X_test
)


# ------------------------------------------
# Train ML model
# ------------------------------------------

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train_tfidf,
    y_train
)


# ------------------------------------------
# Test model
# ------------------------------------------

predictions = model.predict(
    X_test_tfidf
)

accuracy = accuracy_score(
    y_test,
    predictions
)


print(
    f"\nModel Accuracy: "
    f"{accuracy * 100:.2f}%"
)


# ------------------------------------------
# Confusion matrix
# ------------------------------------------

categories = [
    "Software",
    "Data Science",
    "AI/ML",
    "ECE/VLSI"
]

cm = confusion_matrix(
    y_test,
    predictions,
    labels=categories
)


plt.figure(
    figsize=(9, 7)
)

plt.imshow(
    cm,
    cmap="Blues"
)

plt.title(
    "Resume Classification using Machine Learning",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Predicted Category"
)

plt.ylabel(
    "Actual Category"
)

plt.xticks(
    range(4),
    categories,
    rotation=25
)

plt.yticks(
    range(4),
    categories
)


# Add values
for i in range(4):

    for j in range(4):

        plt.text(
            j,
            i,
            cm[i, j],
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold"
        )


plt.colorbar(
    label="Number of Resumes"
)

plt.tight_layout()

plt.savefig(
    "Figure_8.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ------------------------------------------
# Test a new resume
# ------------------------------------------

new_resume = """
Python machine learning numpy pandas
tensorflow deep learning neural networks
computer vision artificial intelligence
"""


new_resume_tfidf = vectorizer.transform(
    [new_resume]
)

prediction = model.predict(
    new_resume_tfidf
)[0]


probabilities = model.predict_proba(
    new_resume_tfidf
)[0]

confidence = max(
    probabilities
) * 100


print("\n" + "=" * 60)

print(
    "NEW RESUME ANALYSIS"
)

print("=" * 60)

print(
    "\nPredicted Category:",
    prediction
)

print(
    f"Confidence: {confidence:.2f}%"
)
