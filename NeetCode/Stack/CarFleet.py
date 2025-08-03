"""
🚗 Car Fleet Problem
📘 Problem Description
You are given a one-lane highway with n cars traveling toward the same destination. Each car has a starting
position and a speed.
Cars cannot pass each other but can catch up and form fleets—groups of cars traveling together at the same
speed and position.
A car fleet is defined as:
- A non-empty set of cars driving at the same position and speed.
- A single car is also considered a fleet.
- If a car catches up to a fleet exactly at the destination, it is considered part of that fleet.

🧮 Inputs
- target (int): The position of the destination in miles.
- position (List[int]): The starting positions of the cars.
- speed (List[int]): The speeds of the cars in miles per hour.

🎯 Output
- Returns the number of distinct car fleets that will arrive at the destination.

🧠 Example
Input:
target = 10
position = [1, 4]
speed = [3, 2]

Output:
1


Explanation:
- Car at position 1 with speed 3 will catch up to the car at position 4 with speed 2.
- They arrive at the destination together, forming one fleet.

🧪 Constraints
- 1 <= n <= 10^4
- 0 < position[i] < target <= 10^6
- 0 < speed[i] <= 10^6
- All positions are unique.

🧩 Approach Summary
- Sort cars by starting position in descending order.
- Calculate time each car takes to reach the destination.
- Simulate fleet formation:
- If a car takes longer than the one ahead, it forms a new fleet.
- If it catches up before the destination, it joins the fleet ahead.

🧑‍💻 Sample Python Implementation
def carFleet(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)
    times = [(target - pos) / spd for pos, spd in cars]

    fleets = 0
    prev_time = 0
    for time in times:
        if time > prev_time:
            fleets += 1
            prev_time = time
    return fleets



📂 File Structure Suggestion
car_fleet/
├── car_fleet.py         # Main implementation
├── test_car_fleet.py    # Unit tests
└── README.md            # Problem description and usage



Let me know if you'd like a version tailored for a specific language or framework!

"""
from typing import List
class CarFleet:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

if __name__=="__main__":
    target = 10
    position = [1, 4]
    speed = [3, 2]
    position2 = [4, 1, 0, 7]
    speed2 = [2, 2, 1, 1]
    obj=CarFleet()
    print(obj.carFleet(target,position,speed))

    print(obj.carFleet(target,position2,speed2))


"""
##Understanding Probelm statement

No problem, Ravi! Let's break down the example step by step so it's crystal clear. Here's the input again:

```python
target = 10
position = [1, 4]
speed = [3, 2]
```

### 🚗 Car Details

| Car | Position | Speed | Time to Reach Target |
|-----|----------|-------|----------------------|
| A   | 1        | 3     | (10 - 1) / 3 = 3.0 hrs |
| B   | 4        | 2     | (10 - 4) / 2 = 3.0 hrs |

### 🧠 What Happens?

- **Car A** starts behind **Car B** but is faster.
- Both cars take **exactly 3 hours** to reach the destination.
- Since Car A catches up to Car B **at the destination**, they are considered part of the **same fleet**.

### ⛔ No Overtaking Allowed

Even though Car A is faster, it can't pass Car B. Instead, it catches up and drives at the same speed once it 
reaches Car B (if it catches up before the destination). But in this case, they arrive **together**, so they form **one fleet**.

### ✅ Final Answer

```python
Output: 1
```

Only **one fleet** reaches the destination.

---

Would you like to see a visual timeline or a simulation-style breakdown of how they move over time?


"""
