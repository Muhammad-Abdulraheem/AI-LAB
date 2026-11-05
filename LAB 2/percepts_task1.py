class reflexagent:
    def evaluate_percept(self, percept):
        temp = percept.get('temperature', 20)
        occupied = percept.get('occupied', False)
        
        if not occupied:
            return "off"
        elif temp > 25:
            return "coll"
        elif temp < 18:
            return "heat"
        else:
            return "idle"

if __name__ == "__main__":
    agent = reflexagent()
    sample_percept = {"temperature": 26, "occupied": True}
    action = agent.evaluate_percept(sample_percept)
    print(f"Percept: {sample_percept} ==> Action/Mode: {action}")