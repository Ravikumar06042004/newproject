import re

# -------------------- OOP Classes --------------------

class Candidate:
    def __init__(self, name, email, skills):
        self.name = name
        self.email = email
        self.skills = skills

    def __str__(self):
        return f"{self.name} ({self.email}) - Skills: {', '.join(self.skills)}"


class Job:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return f"Job: {self.title} | Description: {self.description}"


# -------------------- Iterator Class --------------------

class CandidateIterator:
    def __init__(self, candidates):
        self._candidates = candidates
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._candidates):
            raise StopIteration
        cand = self._candidates[self._index]
        self._index += 1
        return cand


# -------------------- Utility Functions --------------------

# Regex to validate email
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Regex to extract skills from job description
def extract_skills(text):
    # Capture words (like Python, SQL, etc.)
    return re.findall(r'\b[A-Za-z\+\#]{2,}\b', text)

# Lambda to calculate match score between candidate and job skills
calculate_score = lambda cand_skills, job_skills: round(
    len(set(cand_skills) & set(job_skills)) / len(job_skills) * 100, 2
) if job_skills else 0


# -------------------- Main Execution --------------------

if __name__ == "__main__":
    print("=== 🧠 JobMatcher Pro ===\n")

    # Sample candidates
    candidates = [
        Candidate("Ravi Kumar", "ravi@gmail.com", ["Python", "Django", "SQL"]),
        Candidate("Vamsi", "vamsi@gmail.com", ["Java", "Spring", "SQL"]),
        Candidate("Sai", "sai@gmail.com", ["Python", "Machine", "Learning"]),
    ]

    # Sample jobs
    jobs = [
        Job("Python Developer", "Looking for Python, Django, SQL skills"),
        Job("Data Analyst", "Required: Python, Pandas, Excel experience")
    ]

    # Step 1: Validate emails using regex
    print("📧 Email Validation")
    for c in candidates:
        status = "Valid ✅" if is_valid_email(c.email) else "Invalid ❌"
        print(f" - {c.name}: {status}")

    # Step 2: Match candidates to jobs
    print("\n📊 Job Matching Results")
    for job in jobs:
        job_skills = extract_skills(job.description)
        print(f"\n{job}")
        for c in candidates:
            score = calculate_score(c.skills, job_skills)
            print(f" - {c.name}: Match Score = {score}%")

    # Step 3: Iterate over candidates
    print("\n🔁 Iterating through candidates")
    iterator = CandidateIterator(candidates)
    for cand in iterator:
        print(" -", cand)