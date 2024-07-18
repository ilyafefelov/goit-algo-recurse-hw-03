import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Кількість дисків
num_disks = 3

# Ініціалізація стрижнів
initial_rods = {"A": list(range(num_disks, 0, -1)), "B": [], "C": []}
rods = {"A": list(range(num_disks, 0, -1)), "B": [], "C": []}

# Ініціалізація кроків
steps = []


def hanoi(n, source, auxiliary, target):
    if n > 0:
        hanoi(n - 1, source, target, auxiliary)
        steps.append((source, target))
        hanoi(n - 1, auxiliary, source, target)


hanoi(num_disks, "A", "B", "C")

# Налаштування графіки
fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(0, num_disks + 1)


# Функція для оновлення графіки
def update(num):
    ax.clear()
    ax.set_xlim(-1, 3)
    ax.set_ylim(0, num_disks + 1)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["A", "B", "C"])

    # Відновлення стану стрижнів
    rods["A"] = initial_rods["A"][:]
    rods["B"] = []
    rods["C"] = []

    for i in range(num + 1):
        source, target = steps[i]
        disk = rods[source].pop()
        rods[target].append(disk)
        # Print the step
        print(f"Move disk {disk} from {source} to {target}")

    for rod in ["A", "B", "C"]:
        for i, disk in enumerate(rods[rod]):
            ax.add_patch(
                plt.Rectangle(
                    (["A", "B", "C"].index(rod) - disk / 10, i),
                    disk / 5,
                    0.8,
                    edgecolor="black",
                    facecolor="blue",
                )
            )


ani = animation.FuncAnimation(
    fig, update, frames=len(steps), interval=1000, repeat=False
)

plt.show()
