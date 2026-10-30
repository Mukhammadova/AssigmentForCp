def replace_value(values, index, new_value):
    values[index] = new_value
    return None

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def summarize(values):
    stats_record = (min(values), max(values), sum(values))
    return stats_record

days = int(input("Enter the number of days: "))

original = []
for _ in range(days):
    hours = int(input("Enter sleep time in hours: "))
    original.append(hours)

updated = original[:]

change_index = int(input("Enter the index to correct: "))
new_hours = int(input("Enter the new sleep time: "))
replace_value(updated, change_index, new_hours)

target = int(input("Enter the sleep time to search for: "))

found_index = find_first(updated, target)
target_count = updated.count(target)

minimum, maximum, total = summarize(updated)

sorted_list = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum sleep time: {minimum} hours")
print(f"Maximum sleep time: {maximum} hours")
print(f"Total sleep time: {total} hours")

if found_index != -1:
    print(f"First matching index: {found_index}")
else:
    print("Target not found")

print(f"Matching values: {target_count}")