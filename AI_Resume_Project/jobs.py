JOBS = [
    {
        "id": 1,
        "title": "Junior Python Developer",
        "type": "Entry level",
        "skills": ["Python", "Flask", "SQL", "Git"],
    },
    {
        "id": 2,
        "title": "Frontend Developer",
        "type": "Entry level",
        "skills": ["HTML", "CSS", "JavaScript", "React", "Git"],
    },
    {
        "id": 3,
        "title": "Data Analyst",
        "type": "Entry level",
        "skills": ["Python", "SQL", "Excel"],
    },
    {
        "id": 4,
        "title": "Junior NLP Developer",
        "type": "Entry level",
        "skills": ["Python", "NLP", "Machine Learning", "Git"],
    },
    {
        "id": 5,
        "title": "Database Developer",
        "type": "Entry level",
        "skills": ["SQL", "SQL Server", "Git"],
    },
    {
        "id": 6,
        "title": "Backend Developer",
        "type": "Entry level",
        "skills": ["Python", "Django", "MySQL", "Git"],
    },
]


def recommend_jobs(candidate_skills):
    candidate = {skill.casefold() for skill in candidate_skills}
    results = []

    for job in JOBS:
        required = job["skills"]

        matched = [
            skill for skill in required
            if skill.casefold() in candidate
        ]
        missing = [
            skill for skill in required
            if skill.casefold() not in candidate
        ]

        score = round(len(matched) / len(required) * 100)

        results.append({
            **job,
            "matched": matched,
            "missing": missing,
            "score": score,
        })

    return sorted(
        results,
        key=lambda job: (-job["score"], job["title"]),
    )