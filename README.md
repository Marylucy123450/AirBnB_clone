# AirBnB_clone
The goal of this project is to deploy on my server a simple copy of the AirBnB website.

## Project Description

This project is a simplified clone of the AirBnB website, designed to showcase the implementation of a command-line interface (CLI) and a simple storage engine for managing different types of objects.

## Command Interpreter

The command interpreter, named `console.py`, provides a text-based interface for interacting with the AirBnB clone. It supports various commands for managing different classes, including `State`, `City`, `Amenity`, `Place`, `Review`, and `User`.

### Starting the Command Interpreter

To start the command interpreter, run the following command in your terminal:

```bash
./console.py
```

### Using the Command Interpreter

The command interpreter supports the following commands:

- `create`: Creates a new instance of a specified class and saves it to the JSON file.
- `show`: Displays details of a specific instance by class name and instance ID.
- `destroy`: Deletes an instance by class name and instance ID.
- `all`: Displays details of all instances or all instances of a specific class.
- `update`: Updates the attributes of an instance by class name and instance ID.

### Examples

Here are some examples of using the command interpreter:

1. **Creating a new User:**

```bash
create User email="test@example.com" password="pass123" first_name="John" last_name="Doe"
```

2. **Showing details of a User:**

```bash
show User 1234-5678
```

3. **Destroying a Place:**

```bash
destroy Place 9876-5432
```

4. **Listing all instances:**

```bash
all
```

5. **Updating the name of a City:**

```bash
update City 1111-2222 name="New York"
```

Follow me on Twitter 🐦, connect with me on LinkedIn 🔗, and check out my GitHub 🐙. You won't be disappointed!

👉 Twitter: https://twitter.com/NdiranguMuturi1  
👉 LinkedIn: https://www.linkedin.com/in/isaac-muturi-3b6b2b237  
👉 GitHub: https://github.com/Isaac-Ndirangu-Muturi-749  

So, what are you waiting for? Join me on my tech journey and learn something new today! 🚀🌟