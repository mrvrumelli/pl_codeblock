import json
import pennylane as qml
import pennylane.numpy as np

# initialize a device
dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev)
def simple_circuit(angle):

    """
    In this function:
        * Rotate the qubit around the y-axis by angle
        * Measure the expectation value of the Pauli X observable

    Args:
        angle (float): how much to rotate a state around the y-axis

    Returns:
        Union[tensor, float]: The expectation value of the Pauli X observable
    """
    
    qml.RY(angle, 0)

    return qml.expval(qml.PauliX(0))