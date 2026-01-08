import matplotlib.pyplot as plt
from typing import List, Dict


def fetch_student_data() -> List[Dict]:
    """Mock API response."""
    return [
        {"name": "Amit", "score": 78},
        {"name": "Neha", "score": 88},
        {"name": "Rahul", "score": 92},
        {"name": "Priya", "score": 85},
        {"name": "Karan", "score": 81},
        {"name": "Anjali", "score": 90},
        {"name": "Vikram", "score": 76},
        {"name": "Pooja", "score": 89},
    ]


def calculate_average(scores: List[int]) -> float:
    """Calculate average score."""
    return sum(scores) / len(scores)
def visualize_scores(names: List[str], scores: List[int]) -> None:
    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, scores)
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.title("Student Test Scores")
    plt.ylim(0, 100)
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1,
            f"{height}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()
    plt.show()


def main():
    students = fetch_student_data()
    names = [student["name"] for student in students]
    scores = [student["score"] for student in students]

    avg_score = calculate_average(scores)
    print(f"Average Score: {avg_score:.2f}")

    visualize_scores(names, scores)


if __name__ == "__main__":
    main()
