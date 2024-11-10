# Define facts about the shape
facts = {
    "Triangle": {"sides": 3, "sum_of_angles": 180},
    "Pentagon": {"sides": 5, "sum_of_angles": 540} # 5 sides AND sum of angles = 540
}

# Define rule ofunction t check if a shape is a triangle
def is_triangle(properties):
    return properties.get("sides") == 3 and properties.get("sum_of_angles") == 180
def is_pentagon(properties):
    return properties.get("sides") == 5 and properties.get("sum_of_angles") == 540
# List of rules with only the triangle rule
rules = [
    ("is_triangle", is_triangle),
    ("is_pentagon", is_pentagon)
]

# Forward chaining: Apply the rule to check if the shape is a triangle
for shape, properties in facts.items():
    for rule_name, rule_function in rules:
        if rule_function(properties):
            properties[rule_name] = True  # Mark the shape as matching the triangle rule

# Display result for Triangle
for shape, properties in facts.items():
    print(f"{shape} is a Triangle: {properties.get('is_triangle')}")
    print(f"{shape} is a Pentagon: {properties.get('is_pentagon')}")
