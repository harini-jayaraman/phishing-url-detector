import re

url = input("Enter a URL: ")

risk_score = 0

# HTTPS check
if url.startswith("https://"):
    print("URL uses HTTPS")
else:
    print("Warning: URL does not use HTTPS")
    risk_score += 25

# URL length check
if len(url) > 75:
    print("Warning: URL is unusually long")
    risk_score += 20
else:
    print("URL length looks normal")

# @ symbol check
if "@" in url:
    print("Warning: URL contains '@' symbol")
    risk_score += 25
else:
    print("No suspicious '@' symbol found")

# IP address check
if re.search(r'https?://\d+\.\d+\.\d+\.\d+', url):
    print("Warning: URL uses an IP address")
    risk_score += 30
else:
    print("URL does not use an IP address")

# Suspicious keyword check
suspicious_words = ["login", "verify", "account", "update", "secure"]

for word in suspicious_words:
    if word in url.lower():
        print("Warning: Suspicious keyword found:", word)
        risk_score += 5

# Final result
if risk_score > 100:
    risk_score = 100

print("\nRisk Score:", risk_score, "/ 100")

if risk_score >= 50:
    print("Result: Suspicious URL")
else:
    print("Result: Low Risk URL")
if risk_score >= 70:
    print("Risk Level: HIGH")
    print("Result: Highly Suspicious URL")
elif risk_score >= 40:
    print("Risk Level: MEDIUM")
    print("Result: Suspicious URL")
else:
    print("Risk Level: LOW")
    print("Result: Low Risk URL")