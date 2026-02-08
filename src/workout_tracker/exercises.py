from datetime import datetime


class Exercise:
    """Base class for all exercise types.
    
    Attributes:
        name (str): The name of the exercise
        date (str): The date the exercise was performed (YYYY-MM-DD format)
    """
    
    def __init__(self, name: str, date: str = None):
        """Initialize an Exercise.
        
        Args:
            name: The name of the exercise
            date: The date performed (defaults to today if not provided)
        """
        self.name = name
        if date == None:
            self.date = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date = datetime.strftime(date,"%Y-%m-%d")
    
    def calculate_calories(self) -> float:
        """Calculate calories burned for this exercise.
        
        Subclasses must override this method.
        
        Returns:
            float: Estimated calories burned
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def get_duration(self) -> float:
        """Get the duration of the exercise in minutes.
        
        Subclasses must override this method.
        
        Returns:
            float: Duration in minutes
        """
        # This is a base implementation that subclasses will override
        return 0.0
    
    def __str__(self) -> str:
        """Return a string representation of the exercise."""
        # TODO: Return a string like "ExerciseName: 100 calories"
        # Use self.calculate_calories() to get the calories
        return f"{self.name}: {self.calculate_calories} calories"
class CardioExercise(Exercise):
    """Cardio exercise with distance and time tracking.
    
    Attributes:
        name (str): Exercise name
        date (str): Date performed
        distance (float): Distance covered in miles
        duration (float): Time spent in minutes
    """
    
    def __init__(self, name: str, distance: float, duration: float, date: str = None):
        """Initialize a CardioExercise.
        
        Args:
            name: Exercise name (e.g., "Running", "Cycling")
            distance: Distance covered in miles
            duration: Time spent in minutes
            date: Date performed (optional)
        """
        # TODO: Call parent class __init__ with super()
        super().__init__(name,date)
        self.distance = distance
        self.duration = duration
        # TODO: Set self.distance
        # TODO: Set self.duration
    
    def calculate_calories(self) -> float:
        """Calculate calories burned based on distance.
        
        Formula: distance * 100
        
        Returns:
            float: Estimated calories burned
        """
        return self.distance*100
    
    def get_duration(self) -> float:
        """Get the duration of the cardio exercise.
        
        Returns:
            float: Duration in minutes
        """
        return self.duration
    
    def __str__(self) -> str:
        """Return detailed string representation."""
        # TODO: Return something like "Running (3.5 miles, 30 min): 350 calories"
        # Include self.name, self.distance, self.duration, and self.calculate_calories()
        return f"{self.name} ({self.distance} miles, {self.duration} min): {self.calculate_calories()} calories"
class StrengthExercise(Exercise):    
    def __init__(self, name: str, weight: float, reps: int, sets: int ,date: str = None):
        super().__init__(name,date)
        self.reps = reps
        self.sets = sets
        self.weight = weight
    
    def calculate_calories(self) -> float:
        return self.weight*self.reps*self.sets*0.05
    
    def get_duration(self) -> float:
        return self.sets*3
    
    def __str__(self) -> str:
        return f"{self.name} ({self.weight} lbs x {self.reps} reps x {self.sets} sets): {self.calculate_calories()} calories"