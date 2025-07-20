# Day 6 : Lists in Python


movies = ["Sultan", "Dangal", "PK", "3 Idiots", "Chhichhore"]

# Basic Practice

print(movies[0]) # First movie
print(movies[-1]) # Last movie
print(len(movies)) # Total number of movies
all_movies = movies + ["Lagaan", "Zindagi Na Milegi Dobara"] # Add movies to the list
print(all_movies) # Print the updated list of movies
print(movies.append("Kabir Singh")) # Add a movie to the end of the list
print(movies.insert(3,"Barfi")) #insert a movie at index 3
print(movies.sort()) # Sort the list of movies
print(movies) # Print the updated list of movies


# Intermediate Practice

dishes = []
dishes.append(input("Enter your 1st favourite dish: ")) # Add first dish
dishes.append(input("Enter your 2nd favourite dish: ")) # Add second dish
dishes.append(input("Enter your 3rd favourite dish: ")) # Add third dish
print(dishes)  # Print the list of dishes
dishes[1] = "Pasta"  # Change the second dish to Pasta
print(dishes.pop()) # Remove the last dish from the list
print(dishes)  # Print the list of dishes


# Bonus Challenge: To-Do List Manager

tasks = []

tasks.append(input("Enter your first task: "))  # Add first task
tasks.append(input("Enter your second task: "))  # Add second task
tasks.append(input("Enter your third task: "))  # Add third task
tasks.append(input("Enter your fourth task: "))  # Add fourth task
tasks.append(input("Enter your fifth task: "))  # Add fifth task
print(tasks)  # Print the list of tasks

tasks.remove(input("Which task do you want to remove? : "))  # Remove a task
print(tasks)  # Print the updated list of tasks