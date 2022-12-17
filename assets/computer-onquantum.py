import pygame
from qiskit import IBMQ, BasicAer, transpile

from . import globals

class Computer:
    def __init__(self):
        pass
    def update(self):
        pass

class QuantumComputer(Computer):
    def __init__(self, quantum_paddles, circuit_grid) -> None:
        IBMQ.delete_account()
        IBMQ.active_account()
        IBMQ.save_account(globals.API_KEY)
        IBMQ.load_account()
        provider = IBMQ.get_provider('ibm-q')
        self.backend = provider.get_backend('ibmq_quito')
        self.paddles = quantum_paddles.paddles 
        self.lives = 3
        self.circuit_grid = circuit_grid
        self.measured_state = 0
        self.last_measurement_time = pygame.time.get_ticks() - globals.COOLDOWN_TIME

    def update(self, ball):
        current_time = pygame.time.get_ticks()
        # trigger measurement when the ball is close to quantum paddles
        if globals.FIELD_HEIGHT - 60 < ball.rect.y < globals.FIELD_HEIGHT:
            if current_time - self.last_measurement_time > globals.COOLDOWN_TIME:
                self.update_after_measurement()
                self.last_measurement_time = pygame.time.get_ticks()
        else:
            self.update_before_measurement()
    
        if pygame.sprite.collide_mask(ball, self.paddles[self.measured_state]):
            ball.bounce() 

    def update_before_measurement(self):
        simulator = BasicAer.get_backend("statevector_simulator")
        circuit = self.circuit_grid.model.compute_circuit()
        transpiled_circuit = transpile(circuit, simulator)
        statevector = simulator.run(transpiled_circuit, shots=100).result().get_statevector()

        for basis_state, amplitude in enumerate(statevector):
            self.paddles[basis_state].image.set_alpha(abs(amplitude)**2*255)

    def update_after_measurement(self):
        circuit = self.circuit_grid.model.compute_circuit()
        circuit.measure_all()
        transpiled_circuit = transpile(circuit, backend=self.backend)
        counts = self.backend.run(transpiled_circuit, shots=1024).result().get_counts()
        self.measured_state = int(list(counts.keys())[0], 2)

        for paddle in self.paddles:
            paddle.image.set_alpha(0)
        self.paddles[self.measured_state].image.set_alpha(255)
