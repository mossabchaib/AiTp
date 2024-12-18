# Define facts about the shape
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QWidget, QFrame
)
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
#for shape, properties in facts.items():
 #   print(f"{shape} is a Triangle: {properties.get('is_triangle')}")
  #  print(f"{shape} is a Pentagon: {properties.get('is_pentagon')}")
 


class ShapeIdentifierApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shape Identifier AI")
        self.resize(500, 400)
        self.setStyleSheet("background-color: #2C2F33; color: #FFFFFF;")  # Dark theme

        # Initialize the UI
        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Title label
        title_label = QLabel("Shape Identifier AI")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #7289DA;")
        layout.addWidget(title_label)

        # Input for traits
        self.traits_input = QLineEdit()
        self.traits_input.setPlaceholderText("Enter traits (e.g., '3 sides')")
        self.traits_input.setStyleSheet(
            """
            QLineEdit {
                padding: 10px;
                font-size: 14px;
                border: 2px solid #99AAB5;
                border-radius: 8px;
                background-color: #23272A;
                color: #FFFFFF;
            }
            QLineEdit:focus {
                border-color: #7289DA;
            }
            """
        )
        layout.addWidget(QLabel("Traits:"))
        layout.addWidget(self.traits_input)

        # Button to identify shape
        self.identify_button = QPushButton("Identify Shape")
        self.identify_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.identify_button.setStyleSheet(
            """
            QPushButton {
                background-color: #7289DA;
                color: #FFFFFF;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #99AAB5;
            }
            QPushButton:pressed {
                background-color: #677BC4;
            }
            """
        )
        layout.addWidget(self.identify_button)

        # Output area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet(
            """
            QTextEdit {
                padding: 10px;
                font-size: 14px;
                border: 2px solid #99AAB5;
                border-radius: 8px;
                background-color: #23272A;
                color: #FFFFFF;
            }
            """
        )
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output_area)

        # Container with the layout
        container = QFrame()
        container.setLayout(layout)
        container.setStyleSheet("background-color: #2C2F33; border-radius: 10px;")
        self.setCentralWidget(container)

        # Connect button to a placeholder function
        self.identify_button.clicked.connect(self.identify_shape)

    def identify_shape(self):
        """
        Placeholder function for identifying the shape.
        This should be connected to your AI logic.
        """
        traits = self.traits_input.text().strip()
        if traits:
            # Placeholder output
            self.output_area.setText(f"Processing traits: {traits}")
        else:
            self.output_area.setText("Please enter traits to identify the shape.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShapeIdentifierApp()
    window.show()
    sys.exit(app.exec())
