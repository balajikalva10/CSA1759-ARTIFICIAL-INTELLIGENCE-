# Room setup (0 = clean, 1 = dirty)
room = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0]
]

def clean():
    x, y = 0, 0  # Starting position
    while True:
        if room[x][y] == 1:
            room[x][y] = 0
            print(f"Cleaning at ({x}, {y})")
        else:
            print(f"Already clean at ({x}, {y})")

        if all(all(cell == 0 for cell in row) for row in room):
            print("Room is fully clean!")
            break

        # Search for the next dirty spot
        for i in range(len(room)):
            for j in range(len(room[i])):
                if room[i][j] == 1:  # Found a dirty spot
                    print(f"Moving to ({i}, {j})")
                    x, y = i, j
                    break
            else:
                continue  # This continues the outer loop if no break happened in the inner loop
            break  # This breaks the outer loop when a dirty spot is found

clean()
