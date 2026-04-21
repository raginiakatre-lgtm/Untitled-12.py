# Smart Task Scheduler using Priority & Deadline

class Task:
    def __init__(self, name, priority, deadline):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def __repr__(self):
        return f"{self.name} (Priority: {self.priority}, Deadline: {self.deadline})"


def sort_tasks(tasks):
    # Sort by deadline first, then by priority
    return sorted(tasks, key=lambda x: (x.deadline, x.priority))


def display_tasks(tasks, title):
    print("\n" + title)
    print("-" * len(title))
    for task in tasks:
        print(task)


def main():
    tasks = []

    print("=== SMART TASK SCHEDULER ===")
    n = int(input("Enter number of tasks: "))

    # Taking user input
    for i in range(n):
        print(f"\nEnter details for Task {i+1}")
        name = input("Task Name: ")
        priority = int(input("Priority (lower number = higher priority): "))
        deadline = int(input("Deadline (in days): "))

        tasks.append(Task(name, priority, deadline))

    # Display original tasks
    display_tasks(tasks, "Original Task List")

    # Sort tasks
    scheduled_tasks = sort_tasks(tasks)

    # Display scheduled tasks
    display_tasks(scheduled_tasks, "Scheduled Task Order")


if __name__ == "__main__":
    main()