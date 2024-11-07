# logicgates_test
Build and Test

# Logic Gates

A Python implementation of digital logic gates including AND, OR, NOT, NAND, NOR, and XOR gates.

## Features

- Basic logic gates (AND, OR, NOT)
- Compound logic gates (NAND, NOR, XOR)
- Gate connectors for building circuits
- Comprehensive test suite

## Installation

This project uses Poetry for dependency management. To install:

1. Install Poetry if you haven't already:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Clone the repository:
```bash
git clone 
cd logic-gates
```

3. Install dependencies:
```bash
poetry install
```

## Development

### Running Tests

Run the test suite with coverage:

```bash
poetry run pytest
```

### Code Formatting

Format code with Black:
```bash
poetry run black .
```

Sort imports with isort:
```bash
poetry run isort .
```

Check code style with flake8:
```bash
poetry run flake8
```

## Usage

```python
from logic_gates.gates import ANDGate, ORGate, NOTGate, Connector

# Create gates
and_gate = ANDGate("AND1")
not_gate = NOTGate("NOT1")

# Set input values
and_gate.set_pins(1, 1)

# Connect gates
Connector(and_gate, not_gate)

# Get output
result = not_gate.get_output()
```
