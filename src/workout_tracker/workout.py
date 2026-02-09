from typing import List
from workout_tracker.exercises import Exercise

class Workout:
    def __init__(self):
        self._exercises = []
    def add_exercise(self, exercise: Exercise) -> None:
        if isinstance(exercise, Exercise) == False:
            raise TypeError("Only Exercise objects can be added to a workout")
        self._exercises.append(exercise)
    def get_exercises(self) -> List[Exercise]:
        return self._exercises.copy()
    def total_calories(self) -> float:
        return sum(exercise.calculate_calories() for exercise in self._exercises)
    def total_duration(self) -> float:
        return sum(exercise.get_duration()for exercise in self._exercises)
    def exercise_count(self) -> int:
        return len(self._exercises)
    def get_summary(self) -> str:
        if len(self._exercises) == 0:
            return "Empty workout - no exercises added"
        else:
            strings = ["=== Workout Summary ===",]
            for index,exercise in enumerate(self._exercises,start =1):
                line = str(exercise)
                strings.append(f"{index:.0f}. {line}")
            strings.append("-----------------------")
            strings.append(f"Total: {self.total_calories():.0f} calories, {self.total_duration():.0f} minutes")
            multiline = "\n".join(strings)
            return multiline
    def __str__(self) -> str:
        return f"Workout with {self.exercise_count()} exercise(s), {self.total_calories()} calories"
    def __len__(self) -> int:
        return self.exercise_count()
            


