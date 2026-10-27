import re


EDUCATION_PATTERN = re.compile(
    r"\b(?:"
    r"bachelor(?:'s)?|master(?:'s)?|"
    r"BSCS|BSIT|BBA|MBA|BSc|MSc|"
    r"B\.?\s?S\.?|M\.?\s?S\.?|"
    r"Ph\.?D\.?|intermediate|matriculation|"
    r"A[- ]levels?|O[- ]levels?"
    r")\b",
    re.IGNORECASE,
)

EXPERIENCE_HEADING = re.compile(
    r"^(?:(?:professional|work|employment|relevant)\s+)?"
    r"(?:experience|employment history|work history)"
    r"\s*:?\s*$",
    re.IGNORECASE,
)

OTHER_HEADING = re.compile(
    r"^(?:education|academic qualifications|"
    r"educational qualifications|skills|technical skills|"
    r"projects|academic projects|personal projects|"
    r"certifications|certificates|languages|"
    r"interests|references|achievements|"
    r"volunteer experience|summary|profile)"
    r"\s*:?\s*$",
    re.IGNORECASE,
)


def clean_lines(text):
    return [
        re.sub(r"\s+", " ", line).strip()
        for line in text.splitlines()
        if line.strip()
    ]


def extract_education(lines):
    results = []

    for line in lines:
        if EDUCATION_PATTERN.search(line):
            if line not in results:
                results.append(line)

    return results


def extract_experience(lines):
    results = []
    inside_experience = False

    for line in lines:
        if EXPERIENCE_HEADING.fullmatch(line):
            inside_experience = True
            continue

        if inside_experience:
            if OTHER_HEADING.fullmatch(line):
                break

            results.append(line)

    return results


def parse_resume_details(text):
    lines = clean_lines(text)

    return {
        "education": extract_education(lines),
        "experience": extract_experience(lines),
    }