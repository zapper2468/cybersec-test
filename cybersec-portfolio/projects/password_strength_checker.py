import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@$!%*?&#]", password):
        score += 1

    levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    return levels.get(score, "Very Weak")


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print(f"Password strength: {check_password_strength(pwd)}")
