def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students."""
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    """Return scores that are at or above the provided threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""
    # Failing score is 40, passing range is divided into 4 equal intervals
    interval = (highest - 40) // 4
    return [
        41,
        41 + interval,
        41 + interval * 2,
        41 + interval * 3
    ]


def student_ranking(student_scores, student_names):
    """Organize student rank, name, and score in descending order."""
    ranking = []
    for index, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        ranking.append(f"{index}. {name}: {score}")
    return ranking


def perfect_score(student_info):
    """Return the first student who scored a perfect 100."""
    for student in student_info:
        if student[1] == 100:
            return student
    return []
