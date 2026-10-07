"""Exercise 01: for, range, enumerate and zip."""

topics = ["loops", "enumerate", "zip"]
scores = [7, 8, 9]

# TODO: print numbers 1 through 5 with range.
for i in range(1, 6):
    print(i)
    
# TODO: print each topic with a one-based position using enumerate.
topics = ["Variables", "Data Types", "Conditionals", "Loops", "Functions"]

for index, topic in enumerate(topics, start=1):
    print(f"{index}. {topic}")
    
# TODO: pair topics and scores with zip(..., strict=True).
topics = ["Variables", "Data Types", "Conditionals"]
scores = [95, 88, 92]

paired_data = zip(topics, scores, strict=True)

for topic, score in paired_data:
    print(f"Chủ đề: {topic:.<15} Điểm: {score}")
    
print(topics, scores)
