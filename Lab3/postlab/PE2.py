"""
  LAB 03
  PROGRAMMING PROBLEM 02

  This project assumes that you have completed Project 1. Place several Student objects into a list and shuffle it. Then run the sort method with this list and display all of the students' information.
"""

from clear import clearSYS
import random
from typing import List

class Student(object):
    """Represents a student."""

    def __init__(self, name: str, number: int) -> None:
        """All scores are initially 0."""
        self.name: str = name
        self.scores: List[int] = []
        for count in range(number):
            self.scores.append(0)

    def getName(self) -> str:
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i: int, score: int) -> None:
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i: int) -> int:
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self) -> float:
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self) -> int:
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self) -> str:
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, other: "Student") -> bool:
        """Compares two students for equality based on their names."""
        return self.name == other.name

    def __lt__(self, other: "Student") -> bool:
        """Compares if this student's name is less than the other's."""
        return self.name < other.name

    def __ge__(self, other: "Student") -> bool:
        """Compares if this student's name is greater than or equal to the other's."""
        return self.name >= other.name

def randScore(student: Student) -> None: 
    """Sets random scores for the student."""
    for i in range(1, len(student.scores) + 1):
        student.setScore(i, random.randint(70, 100))

def printStudentNames(students: List[Student]) -> None:
    """Prints the students' names."""
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student.getName()}")
    print()

def main() -> None:
    """Testing comparison operators."""

    # Clear the screen
    clearSYS()

    # Initialize students
    names: List[str] = ["Ken", "John", "Alice", "Bob", "Eve", "Habiba", "Tyler", "Nadia", "Water", "Kian", "Branch", "Rihanna", "Thompson", "Evelyn", "Bernard", "Hamish", "Benson", "Arran", "Stafford", "Jada", "Irwin", "Nannie", "Hill", "Hugh", "Hoover", "Poppie", "Duran", "Scarlet", "Holder", "Madiha", "Donaldson", "Stevie", "Baxter", "Myrtle", "Middleton", "Joshua", "Hess", "Mila", "Mercado", "Brendan", "Howard", "Kendra", "Walker", "Blanche", "Barnes", "Cameron", "Mullen", "Jamal", "Acevedo", "Maximus", "Rivers", "Chiara", "Finley", "Betsy", "Friedman", "Lincoln", "Blevins", "Jonah", "Beck", "Bailey", "Campbell", "Jaime", "Jefferson", "Jordan", "Paul"] # 65 random names for testing

    studentCount: int = 10 # Number of students set for testing
    subjects: int = 5 # Number of subjects set for testing

    # Generate random students with random scores
    students: List[Student] = [Student(random.choice(names), subjects) for _ in range(studentCount)]
    for student in students:
        randScore(student)

    # Shuffle the list of students
    random.shuffle(students)
    print("Students (shuffled):")
    printStudentNames(students)

    # Sort the list of students
    students.sort()
    print("Students (sorted):")
    printStudentNames(students)

if __name__ == "__main__":
    main()
