import pytest

class TestLogicGates:
    def test_and_gate(self):
        gate = ANDGate("AND1")
        test_cases = [
            (0, 0, 0),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 1),
        ]
        for a, b, expected in test_cases:
            gate.set_pins(a, b)
            assert gate.get_output() == expected

    def test_or_gate(self):
        gate = ORGate("OR1")
        test_cases = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 1),
        ]
        for a, b, expected in test_cases:
            gate.set_pins(a, b)
            assert gate.get_output() == expected

    def test_not_gate(self):
        gate = NOTGate("NOT1")
        test_cases = [(0, 1), (1, 0)]
        for input_val, expected in test_cases:
            gate.set_pin(input_val)
            assert gate.get_output() == expected

    def test_nand_gate(self):
        gate = NANDGate("NAND1")
        test_cases = [
            (0, 0, 1),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0),
        ]
        for a, b, expected in test_cases:
            gate.set_pins(a, b)
            assert gate.get_output() == expected

    def test_nor_gate(self):
        gate = NORGate("NOR1")
        test_cases = [
            (0, 0, 1),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 0),
        ]
        for a, b, expected in test_cases:
            gate.set_pins(a, b)
            assert gate.get_output() == expected

    def test_xor_gate(self):
        gate = XORGate("XOR1")
        test_cases = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0),
        ]
        for a, b, expected in test_cases:
            gate.set_pins(a, b)
            assert gate.get_output() == expected

    def test_connector(self):
        and_gate = ANDGate("AND1")
        not_gate = NOTGate("NOT1")
        
        and_gate.set_pins(1, 1)
        Connector(and_gate, not_gate)
        
        assert not_gate.get_output() == 0

    def test_gate_labels(self):
        gates = [
            (ANDGate, "AND1"),
            (ORGate, "OR1"),
            (NOTGate, "NOT1"),
            (NANDGate, "NAND1"),
            (NORGate, "NOR1"),
            (XORGate, "XOR1"),
        ]
        
        for gate_class, label in gates:
            gate = gate_class(label)
            assert gate.get_label() == label

    def test_invalid_pin_connection(self):
        gate = ANDGate("AND1")
        with pytest.raises(AssertionError):
            gate.get_output()

    def test_binary_gate_pin_setters(self):
        gate = ANDGate("AND1")
        
        # Test individual pin setters
        gate.set_pin_a(1)
        assert gate.get_pin_a() == 1
        
        gate.set_pin_b(0)
        assert gate.get_pin_b() == 0
        
        # Test bulk pin setter
        gate.set_pins(0, 1)
        assert gate.get_pin_a() == 0
        assert gate.get_pin_b() == 1

    def test_unary_gate_pin_setter(self):
        gate = NOTGate("NOT1")
        gate.set_pin(1)
        assert gate.get_pin() == 1
