from datetime import datetime

CURRENT_DATE = datetime.now().date


class Project:
    """project class for storing details of a project."""

    def __init__(self, name="", date="", priority=0, cost_est=0, completion_rate=0):
        """Initialise a Project."""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost_est = cost_est
        self.completion_rate = completion_rate

    def __str__(self):
        """Return a string representation of a Project."""
        return f"{self.name} ({self.date}) estimated ${self.cost_est:,.2f} in cost at {self.completion_rate}% " \
               f"complete at a level {self.priority} priority "

    def is_complete(self):
        return self.completion_rate == 100

    def __lt__(self, other):
        """Less than, used for sorting Projects - by date started."""
        return self.date < other.date
