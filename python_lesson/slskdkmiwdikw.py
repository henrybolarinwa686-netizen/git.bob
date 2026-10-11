"""repeat_times = "3"
print("Beep! " * repeat_times)
The Task: In Python, you can multiply a string by a number to repeat it (e.g., "Beep! " * 3), but here repeat_times is a string. Have your student test this, explain why it fails, and fix it by casting the variable into the correct data type."""

repeat_times="3"

print("Beep! " * int(repeat_times))
