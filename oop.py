class Person:
  """
  This class represents a person with attributes like name, age, and gender.
  """

  def __init__(self, name, age, gender):
    """
    This method initializes the Person object with the provided name, age, and gender.

    Args:
      name: The person's name (string).
      age: The person's age (integer).
      gender: The person's gender (string).
    """
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    """
    This method introduces the person by printing their name, age, and gender.
    """
    print(f"Hello! My name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person("Alice", 30, "Female")

# Call the introduce method to display person1's information
person1.introduce()