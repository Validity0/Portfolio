const display = document.getElementById('text-box');
const buttons = document.querySelectorAll('.buttons button');

let currentNumber = '0';
let previousNumber = '';
let operation = '';

// Function to update display
function updateDisplay() {
    display.value = currentNumber;
}

// Function to perform arithmetic operations
function calculate(num1, operator, num2) {
    switch (operator) {
        case '+':
            return num1 + num2;
        case '-':
            return num1 - num2;
        case '*':
            return num1 * num2;
        case '/':
            return num1 / num2;
        default:
            return NaN; // Invalid operator
    }
}

// Event listeners for each button
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.textContent;

        if (!isNaN(value) || value === '.') {
            if (currentNumber === '0' && value !== '.') {
                currentNumber = value;
            } else {
                currentNumber += value;
            }
        } else if (value === 'C') {
            currentNumber = '0';
            previousNumber = '';
            operation = '';
        } else if (value === '=') {
            if (operation !== '' && previousNumber !== '') {
                currentNumber = calculate(parseFloat(previousNumber), operation, parseFloat(currentNumber));
                operation = '';
                previousNumber = '';
            }
        } else {
            if (operation !== '') {
                currentNumber = calculate(parseFloat(previousNumber), operation, parseFloat(currentNumber));
            }
            previousNumber = currentNumber;
            currentNumber = '';
            operation = value;
        }

        updateDisplay();
    });
});