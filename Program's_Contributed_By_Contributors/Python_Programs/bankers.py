import numpy as np

class BankersAlgorithm:
    def __init__(self, n_processes, n_resources):
        self.n_processes = n_processes
        self.n_resources = n_resources
        self.max_claim = np.zeros((n_processes, n_resources), dtype=int)
        self.allocation = np.zeros((n_processes, n_resources), dtype=int)
        self.available_resources = np.zeros(n_resources, dtype=int)
        self.need = np.zeros((n_processes, n_resources), dtype=int)
    
    def set_max_claim(self, process, resources):
        self.max_claim[process] = resources
    
    def set_allocation(self, process, resources):
        self.allocation[process] = resources
    
    def set_available_resources(self, resources):
        self.available_resources = resources
    
    def calculate_need(self):
        self.need = self.max_claim - self.allocation
    
    def is_safe(self):
        work = np.copy(self.available_resources)
        finish = np.zeros(self.n_processes, dtype=int)
        sequence = []
        
        for _ in range(self.n_processes):
            for i in range(self.n_processes):
                if finish[i] == 0 and np.all(self.need[i] <= work):
                    work += self.allocation[i]
                    finish[i] = 1
                    sequence.append(i)
        
        return all(finish), sequence
    
    def request_resources(self, process, request):
        if np.all(request <= self.need[process]):
            if np.all(request <= self.available_resources):
                self.available_resources -= request
                self.allocation[process] += request
                self.need[process] -= request
                safe, _ = self.is_safe()
                if safe:
                    return True
                else:
                    # Rollback the allocation
                    self.available_resources += request
                    self.allocation[process] -= request
                    self.need[process] += request
                    return False
            else:
                print("Request exceeds available resources. Request denied.")
                return False
        else:
            print("Request exceeds maximum claim. Request denied.")
            return False

# Example usage
if __name__ == "__main__":
    n_processes = 5
    n_resources = 3
    
    banker = BankersAlgorithm(n_processes, n_resources)
    
    # Set maximum claim for each process
    banker.set_max_claim(0, [7, 5, 3])
    banker.set_max_claim(1, [3, 2, 2])
    banker.set_max_claim(2, [9, 0, 2])
    banker.set_max_claim(3, [2, 2, 2])
    banker.set_max_claim(4, [4, 3, 3])
    
    # Set initial allocation of resources to each process
    banker.set_allocation(0, [0, 1, 0])
    banker.set_allocation(1, [2, 0
