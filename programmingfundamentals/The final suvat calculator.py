import math

def suvat_calculator():
    while True:
        print("Welcome to the SUVAT calculator")
        print("Please enter your values (use '?' for the missing value): ")

        # Input values and check for missing entries
        s = input("Enter displacement (s) in meters: ")
        u = input("Enter initial velocity (u) in m/s: ")
        v = input("Enter final velocity (v) in m/s: ")
        a = input("Enter acceleration (a) in m/s²: ")
        t = input("Enter time (t) in seconds: ")

        # Convert inputs to float if not missing
        s = float(s) if s != "?" else None
        u = float(u) if u != "?" else None
        v = float(v) if v != "?" else None
        a = float(a) if a != "?" else None
        t = float(t) if t != "?" else None

        # Calculate missing value based on known values
        if s is None and u is not None and t is not None and a is not None:
            print("Equation: s = ut + 0.5at²")
            s = u * t + 0.5 * a * t**2
            s = abs(s) #convert negative to positive
            print(f"Displacement (s) = {round(s, 2)} meters")

        elif u is None and s is not None and t is not None and a is not None:
            print("Equation: s = ut + 0.5at² rearranged to u = (s - 0.5at²) / t")
            u = (s - 0.5 * a * t**2) / t
            u = abs(u) #convert negative to positive
            print(f"Initial velocity (u) = {round(u, 2)} m/s")

        elif v is None and u is not None and a is not None and s is not None:
            print("Equation: v² = u² + 2as rearranged to v = √(u² + 2as)")
            if u**2 + 2 * a * s < 0:
                print("Error: Cannot calculate the square root of a negative number. Check your inputs.")
            else:
                v = math.sqrt(u**2 + 2 * a * s)
                v = abs(v) #convert negative to positive
                print(f"Final velocity (v) = {round(v, 2)} m/s")

        elif a is None and u is not None and v is not None and t is not None:
            print("Equation: v = u + at rearranged to a = (v - u) / t")
            a = (v - u) / t
            a = abs(a) #convert negative to positive
            print(f"Acceleration (a) = {round(a, 2)} m/s²")

        elif t is None and u is not None and v is not None and a is not None:
            print("Equation: v = u + at rearranged to t = (v - u) / a")
            if a == 0:
                print("Error: Cannot divide by zero. Check your inputs.")
            else:
                t = (v - u) / a
                t = abs(t) #convert negative to positive
                print(f"Time (t) = {round(t, 2)} seconds")

        else:
            print("Error: Not enough information or incorrect input. Please try again.")
            continue

        # Check for negative values (physical validation)
        if s is not None and s < 0:
            print("Warning: Displacement (s) cannot be negative. Check your inputs.")
        if u is not None and u < 0:
            print("Warning: Initial velocity (u) cannot be negative. Check your inputs.")
        if v is not None and v < 0:
            print("Warning: Final velocity (v) cannot be negative. Check your inputs.")
        if t is not None and t <= 0:
            print("Warning: Time (t) must be greater than zero. Check your inputs.")
        if a is not None and a < 0:
            print("Note: Negative acceleration (a) may indicate deceleration. Verify if this is correct.")

        # Ask the user if they want to continue
        response = input("Do you want to calculate another SUVAT problem? (yes/y or no/n): ").lower()
        if response in ["n", "no"]:
            print("Goodbye!")
            break

# Run the SUVAT calculator
suvat_calculator()