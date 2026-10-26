"""Exercise 01: class, object and methods."""


class Progress:
    """Track completed items out of a total."""

    def __init__(self, completed: int, total: int) -> None:
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        """Return completion as a percentage, avoiding division by zero."""
        if self.total <= 0:
            return 0.0
        return self.completed / self.total * 100

    def __str__(self) -> str:
        """Return a readable summary of progress."""
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.1f}%)"


def main() -> None:
    """Create a Progress object and display its information."""
    progress = Progress(completed=3, total=4)
    print(progress)
    print(f"Percentage: {progress.percentage():.1f}%")


if __name__ == "__main__":
    main()
