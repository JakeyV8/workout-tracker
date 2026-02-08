from workout_tracker import CardioExercise, StrengthExercise, FlexibilityExercise

# Create a cardio exercise
run = CardioExercise("Morning Run", distance=3.5, duration=30)

print(f"Exercise: {run}")
print(f"Calories: {run.calculate_calories()}")
print(f"Duration: {run.get_duration()} minutes")

lifting = StrengthExercise("Bench Press",weight=135,sets=3,reps=10)
print(f"Exercise: {lifting}")
print(f"Calories: {lifting.calculate_calories()}")
print(f"Duration: {lifting.get_duration()} minutes")

yoga = FlexibilityExercise("Yoga", duration=30,intensity='MEDIUM')
print(f"Exercise: {yoga}")
print(f"Calories: {yoga.calculate_calories()}")
print(f"Duration: {yoga.get_duration()} minutes")