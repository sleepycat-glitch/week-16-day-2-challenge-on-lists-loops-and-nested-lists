# School Supply Order Tracking – Logic Challenge

## Objective
# Students will apply their understanding of lists, nested lists, slicing, sorting, list grouping, and logical decision-making to solve a real-world data organization problem without using code.

# ---

## Scenario
# You are helping the main office organize student supply requests for the week. Each request includes:

# - Student name  
# - Item requested  
# - Quantity requested  

# All requests must be stored together in one organized system.

# ---

## Student Tasks (No Coding – Logic Only)

### 1. Create Student Requests
# Create a collection that stores information for **3 different student requests**.  
# Each student request must include:
# - Student name  
# - Item requested  
# - Quantity requested  



# ---

### 2. Identify Key Information
# From your collection:
# - Identify the **first student’s name**
# - Identify the **last student’s requested item only**



# ---

### 3. Quantity Extraction
# Create a **separate list that contains only the quantities requested** by the students.

# ---

### 4. Order Size Analysis
# Analyze the quantities:
# - If **any quantity is greater than 5**, label the order:
#   “Large order detected!”
# - Otherwise label the order:
#   “Orders within normal limits.”


# ---

### 5. Quantity Organization
# Re-organize the quantity list from **smallest to largest** and display the final result.

# ---

## Challenge Extension: Classroom Storage Grid

# You are also given a grid showing classroom supply counts:

# Classroom 1: 8, 12, 5  
# Classroom 2: 7, 3, 9  
# Classroom 3: 10, 6, 4  

# Answer the following:

# 1. What is the **middle number** in the second classroom’s list?
# 2. Create a new list that extracts **only the last number** from each classroom.
# 3. Explain **why this information must be stored as a nested structure instead of a single list.**


# ---

## What This Assignment Tests
# - Understanding how grouped data is stored
# - Nested structure reasoning
# - Data extraction using position
# - Organizational logic
# - Real-world decision-making with quantities

# ---

## Submission Requirements
# - All answers must be written in words and/or tables.
# - No programming code may be used.
# - Show clear reasoning for each response.

# ---

## Academic Integrity
# This is an individual logic and reasoning task. All work must be your own.

# ---

# Instructor: Marvin Evins  
# Course:  AP Computer Science Principles  


student_name = [ ]
item_requested = [ ]
quantity_requested = [ ] 
name = input("Please type in student's first and last name: ")
student_name.append(name)
item = input("What item(s) would you like to purchase?: ")
item_requested.append(item)
quantity = int(input("How many of the item you requested would you like?: "))
quantity_requested.append(quantity)

search = input("Please input the first name of the student you would like to find: ")
if search in student_name:
    print(search)
else:
    print("Not found.")
print(item_requested[-1])

print(quantity_requested)

order_size = [ ]
if quantity>5:
    order_size.append("Large order detected!")
else:
    order_size.append("Orders within normal limits.")

temp = quantity_requested
temp.sort()
print(temp)

classrooms = [
    [8,12,5], 
    [7,3,9],
    [10,6,4]
]

print(classrooms[1][1])
first_col = [row[-1] for row in classrooms]
print(first_col)