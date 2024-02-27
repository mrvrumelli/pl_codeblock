import pennylane as qml
import pennylane.numpy as np

dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev)
def circuit(angles):
    """
    The quantum circuit that you will simulate.

    Args:
        angles (list(float)): The gate angles in the circuit.

    Returns:
        (numpy.tensor): The probability vector of the underlying quantum state
        that this circuit produces.
    """

    qml.RX(angles[0], 0)
    qml.RX(angles[1], 1)

    return qml.probs(wires=[0, 1])
