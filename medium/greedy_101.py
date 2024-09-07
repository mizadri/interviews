def activity_selection(activities):
    # Step 1: Sort activities by their finish time
    activities.sort(key=lambda x: x[1])  # Sorting by finish time
    
    # Step 2: Initialize the solution with the first activity
    selected_activities = [activities[0]]
    
    # Step 3: Iterate through the remaining activities
    for i in range(1, len(activities)):
        if activities[i][0] >= selected_activities[-1][1]:  # Feasibility check: start time >= last finish time
            selected_activities.append(activities[i])  # Greedy choice: add the current activity
    
    return selected_activities

# Example usage:
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
result = activity_selection(activities)
print("Selected activities:", result)
