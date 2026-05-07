import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Days
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Step 2: User input for steps
print("Enter steps for 7 days:")
steps = []

for day in days:
    s = int(input(f"{day}: "))
    steps.append(s)

steps = np.array(steps)

# Step 3: Calories (simple formula)
# 1 step = 0.04 calories
calories = steps * 0.04

# Step 4: Create DataFrame
data = pd.DataFrame({
    "Day": days,
    "Steps": steps,
    "Calories": calories
})

print("\nFitness Data:\n")
print(data)

# Step 5: Analysis
print("\nAverage Steps:", np.mean(steps))
print("Total Calories Burned:", np.sum(calories))

# Step 6: Goal Check
goal = 8000
print("\nGoal Analysis (8000 steps):")

for i in range(len(days)):
    if steps[i] >= goal:
        print(days[i], ": Goal Achieved ✅")
    else:
        print(days[i], ": Not Achieved ❌")

# Step 7: Plot Steps Graph
plt.plot(days, steps, marker='o')
plt.title("Weekly Steps Count")
plt.xlabel("Days")
plt.ylabel("Steps")

plt.plot(days, steps, marker='o')
plt.axhline(y=8000, linestyle='--')  # goal line
plt.title("Steps vs Goal")
plt.show()

# Step 8: Plot Calories Graph
plt.bar(days, calories)
plt.title("Calories Burned")
plt.xlabel("Days")
plt.ylabel("Calories")
plt.show()

print("Steps:", steps)