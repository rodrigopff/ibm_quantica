from typing import Union
from numpy import csingle
from qiskit import *
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


from qiskit import IBMQ
from qiskit.providers import backend
# IBMQ.save_account('e21e6f697679252bcafc5764524323d92ae7f5f6b1e8c707bfeaa096969913ef54b739890a0b3510c7a950a4907143f21e0fc77352ba1913ebc3a1fdac132c52')

list = IBMQ.load_account()
# IBMQ.load_account()
# print("Available backends:")
# for prov in IBMQ.providers() :
#     print(prov)

provider=IBMQ.get_provider('ibm-q')
# provider = IBMQ.get_provider(hub='ibm-q')
# for backend in provider.backends():
#     print(backend)


# quantum_computer=provider.get_backend('ibmq_manila')
# quantum_computer=provider.get_backend('ibmq_qasm_simulator')
# quantum_computer=provider.get_backend('ibmq_bogota')
quantum_computer=provider.get_backend('ibmq_belem')

for backend in provider.backends(): 
    print(backend.configuration().to_dict()['backend_name'] + "  " + str(backend.configuration().to_dict()['n_qubits']))
    print(backend.status().to_dict())

# 2 Quibits
qr=QuantumRegister(2)
cr=ClassicalRegister(2)
circuit=QuantumCircuit(qr,cr)

# 2 quibits
circuit.h(qr[0])
circuit.cx(qr[0],qr[1])
circuit.measure(qr,cr)
circuit.draw('mpl')
print("Desennhado o circuito ... ")
plt.show()
# str = quantum_computer.configuration().to_dict()['backend_name'] + "  " +str(quantum_computer.configuration().to_dict()['n_qubits'])
# print (str)

## Executa o circuito na nuvem da IBM 
print("executando na nuvem da IBM .... aguarde ....")
execute_circuit=execute(circuit,backend=quantum_computer)
result=execute_circuit.result()
print("fim da execucao na nuvem da IBM .... desenhando resultados ....")
print(result.get_counts(circuit))
plot_histogram(result.get_counts(circuit))
plt.show()



