print("Temperature Modeling")
print("1. Hard-coded values")
print("2. Keyboard input")
print("3. Input from file (single set)")
print("4. Input from file (multiple sets)")

choice = input("Select option (1-4): ")

if choice == "1":
    # Hard-coded coefficients
    a, b, c, time = 2, 3, 4, 5
    temperature = a * time**2 + b * time + c
    print(f"The Temperature at time {time} is {temperature:.2f}")

elif choice == "2":
    # Keyboard input
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    time = float(input("Enter time: "))
    temperature = a * time**2 + b * time + c
    print(f"The Temperature at time {time} is {temperature:.2f}")

elif choice == "3":
    # Single set file input
    try:
        with open("weather_single.txt", "r") as f:
            a, b, c, time = map(float, f.readline().split())
            temperature = a * time**2 + b * time + c
            print(f"The Temperature at time {time} is {temperature:.2f}")
    except FileNotFoundError:
        print("File 'weather_single.txt' not found.")
    except ValueError:
        print("Invalid values in file.")

elif choice == "4":
    # Multiple set file input
    try:
        with open("weather_multiple.txt", "r") as f:
            for idx, line in enumerate(f, start=1):
                try:
                    a, b, c, time = map(float, line.strip().split())
                    temperature = a * time**2 + b * time + c
                    print(f"[{idx}] Temperature at time {time} is {temperature:.2f}")
                except ValueError:
                    print(f"[{idx}] Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print("File 'weather_multiple.txt' not found.")
else:
    print("Invalid choice. Please select between 1 and 4.")

