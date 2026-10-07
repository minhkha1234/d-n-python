"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

# TODO: append one subject and insert another at index 1.
subjects = ["Math", "Physics", "Chemistry"]
print("Danh sách ban đầu:", subjects)

subjects.append("English")

subjects.insert(1, "Biology")

print("Danh sách sau khi sửa:", subjects)

# TODO: update the first subject.
subjects[0] = "Calculus"

# TODO: remove one known subject and pop the last subject.
subjects.remove("Chemistry")
subjects.pop()

# TODO: print the first, last and middle slice after each safe operation.
items = ["Python", "Java", "C++", "JavaScript", "Go", "Rust"]

print("Danh sách hiện tại:", items)

if items:
    first_item = items[0]
    
    last_item = items[-1]
    
    mid_index = len(items) // 2
    middle_slice = items[mid_index - 1 : mid_index + 1] if len(items) >= 2 else items[mid_index:mid_index+1]
    
    print(f"Ký tự/Phần tử đầu:  {first_item}")
    print(f"Ký tự/Phần tử cuối: {last_item}")
    print(f"Lát cắt ở giữa:     {middle_slice}")
else:
    print("Danh sách rỗng, không thể thực hiện thao tác cắt!")
print(subjects)
