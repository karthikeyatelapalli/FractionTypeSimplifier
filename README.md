# Fraction Type Simplifier

This Python program is a teaching aid for elementary school educators to demonstrate fractions, their classification, and simplification. It classifies fractions into **proper**, **improper**, and **mixed** types based on their numerator and denominator and uses the **greatest common divisor (GCD)** to simplify them. This interactive tool provides instant feedback and detailed explanations, making it an excellent resource for both teachers and students.

---

## **Table of Contents**
1. [Features](#features)
2. [How the Program Works](#how-the-program-works)
3. [How to Run](#how-to-run)
4. [Input Examples](#input-examples)
5. [Detailed Output Breakdown](#detailed-output-breakdown)
6. [Error Handling](#error-handling)
7. [Dependencies](#dependencies)
8. [License](#license)

---

## **Features**

### **1. Fraction Classification**
The program classifies fractions into the following types:
- **Proper Fractions**: Numerator < Denominator (e.g., 3/7).
- **Improper Fractions**: Numerator >= Denominator (e.g., 9/5).
- **Mixed Fractions**: Improper fractions represented as a combination of a whole number and a proper fraction (e.g., 9/5 becomes 1 and 4/5).

### **2. Fraction Simplification**
- Uses the **greatest common divisor (GCD)** to simplify fractions.
- Indicates if the fraction cannot be reduced further.

### **3. User Interaction**
- Provides a user-friendly interface with clear prompts.
- Ensures input validation for both numerator and denominator values.

---

## **How the Program Works**
1. **Input Validation**: 
   - The user is prompted to enter a numerator and denominator.
   - If either value is less than or equal to zero, the program asks the user to re-enter valid values.

2. **Classification**:
   - The program determines whether the fraction is proper or improper.
   - For improper fractions, it calculates the whole number and the remaining proper fraction (mixed number).

3. **Simplification**:
   - The program calculates the GCD of the numerator and denominator.
   - If the GCD > 1, the fraction is simplified; otherwise, it is indicated as irreducible.

4. **Output**:
   - Displays the type of fraction.
   - Shows the simplified fraction or mixed number if applicable.

---

## **How to Run**

### **Requirements**
- Python 3.x
- No additional libraries required (uses the built-in `math` module).

### **Steps**
1. Save the program as `fraction_simplifier.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder containing `fraction_simplifier.py`.
4. Run the program:
   ```bash
   python3 fraction_simplifier.py
