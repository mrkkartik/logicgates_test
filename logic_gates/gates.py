from typing import Optional, Union


class LogicGate:
    """Base class for all logic gates."""

    def __init__(self, lbl: str):
        """
        Initialize a logic gate.

        Args:
            lbl (str): Label to identify the gate
        """
        self.name = lbl
        self.output = None

    def get_label(self) -> str:
        """Return the label of the gate."""
        return self.name

    def get_output(self) -> int:
        """
        Calculate and return the output of the gate.

        Returns:
            int: The output value (0 or 1)
        """
        self.output = self.perform_gate_logic()
        return self.output

    def perform_gate_logic(self) -> int:
        """
        Perform the logic operation of the gate.

        This method should be overridden by subclasses.

        Returns:
            int: Result of the logic operation
        """
        raise NotImplementedError("perform_gate_logic() must be implemented by each gate")


class BinaryGate(LogicGate):
    """Base class for gates with two inputs."""

    def __init__(self, lbl: str):
        """
        Initialize a binary gate.

        Args:
            lbl (str): Label to identify the gate
        """
        super().__init__(lbl)
        self.pin_a: Optional[int] = None
        self.pin_b: Optional[int] = None

    def set_a(self, a: int) -> None:
        """Set the value of pin A."""
        self.pin_a = a

    def set_b(self, b: int) -> None:
        """Set the value of pin B."""
        self.pin_b = b

    def set_pin_a(self, value: int) -> None:
        """Set the value of pin A."""
        self.pin_a = value

    def set_pin_b(self, value: int) -> None:
        """Set the value of pin B."""
        self.pin_b = value

    def set_pins(self, value_a: int, value_b: int) -> None:
        """Set both input pins at once."""
        self.pin_a = value_a
        self.pin_b = value_b

    def set_next_pin(self, source: int) -> None:
        """
        Set the next available pin with the provided source.

        Args:
            source (int): Value to set on the next available pin
        """
        if self.pin_a is None:
            self.pin_a = source
        else:
            if self.pin_b is None:
                self.pin_b = source
            else:
                raise ValueError("Cannot Connect: NO EMPTY PINS on this gate")

    def get_pin_a(self) -> Optional[int]:
        """Get the value of pin A."""
        return self.pin_a

    def get_pin_b(self) -> Optional[int]:
        """Get the value of pin B."""
        return self.pin_b


class UnaryGate(LogicGate):
    """Base class for gates with one input."""

    def __init__(self, lbl: str):
        """
        Initialize a unary gate.

        Args:
            lbl (str): Label to identify the gate
        """
        super().__init__(lbl)
        self.pin: Optional[int] = None

    def set_pin(self, value: int) -> None:
        """Set the input pin value."""
        self.pin = value

    def get_pin(self) -> Optional[int]:
        """Get the input pin value."""
        return self.pin

    def set_next_pin(self, source: int) -> None:
        """
        Set the pin with the provided source.

        Args:
            source (int): Value to set on the pin

        Raises:
            ValueError: If the pin is already set
        """
        if self.pin is None:
            self.pin = source
        else:
            raise ValueError("Cannot Connect: NO EMPTY PINS on this gate")


class ANDGate(BinaryGate):
    """Implementation of AND gate."""

    def perform_gate_logic(self) -> int:
        """Perform AND operation on inputs."""
        assert self.pin_a is not None and self.pin_b is not None
        return int(bool(self.pin_a and self.pin_b))


class ORGate(BinaryGate):
    """Implementation of OR gate."""

    def perform_gate_logic(self) -> int:
        """Perform OR operation on inputs."""
        assert self.pin_a is not None and self.pin_b is not None
        return int(bool(self.pin_a or self.pin_b))


class NOTGate(UnaryGate):
    """Implementation of NOT gate."""

    def perform_gate_logic(self) -> int:
        """Perform NOT operation on input."""
        assert self.pin is not None
        return int(not bool(self.pin))


class NANDGate(ANDGate):
    """Implementation of NAND gate."""

    def perform_gate_logic(self) -> int:
        """Perform NAND operation on inputs."""
        return int(not bool(super().perform_gate_logic()))


class NORGate(ORGate):
    """Implementation of NOR gate."""

    def perform_gate_logic(self) -> int:
        """Perform NOR operation on inputs."""
        return int(not bool(super().perform_gate_logic()))


class XORGate(BinaryGate):
    """Implementation of XOR gate."""

    def perform_gate_logic(self) -> int:
        """Perform XOR operation on inputs."""
        assert self.pin_a is not None and self.pin_b is not None
        return int(bool(self.pin_a) != bool(self.pin_b))


class Connector:
    """Class to connect gates together."""

    def __init__(self, from_gate: LogicGate, to_gate: Union[BinaryGate, UnaryGate]):
        """
        Initialize a connector between two gates.

        Args:
            from_gate (LogicGate): Gate to connect from
            to_gate (Union[BinaryGate, UnaryGate]): Gate to connect to
        """
        self.from_gate = from_gate
        self.to_gate = to_gate
        to_gate.set_next_pin(from_gate.get_output())

    def get_from(self) -> LogicGate:
        """Get the source gate."""
        return self.from_gate

    def get_to(self) -> Union[BinaryGate, UnaryGate]:
        """Get the destination gate."""
        return self.to_gate


def main():
    """Example usage of logic gates."""
    # Create gates
    g1 = ANDGate("G1")
    g2 = ANDGate("G2")
    g3 = ORGate("G3")
    g4 = NOTGate("G4")

    # Set input values
    g1.set_pins(1, 1)
    g2.set_pins(0, 1)
    
    # Connect gates
    g3.set_pins(g1.get_output(), g2.get_output())
    g4.set_pin(g3.get_output())

    # Get final output
    result = g4.get_output()
    print(f"Circuit Output: {result}")


if __name__ == "__main__":
    main()
