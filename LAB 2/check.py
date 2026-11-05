from models import modelbase

def run_tests():
    agent = modelbase()
    
    test = [
        {"temperature": 20, "occupied": False},
        {"temperature": 22, "occupied": True},
        {"temperature": 26, "occupied": True},
        {"temperature": 26, "occupied": True},
        {"temperature": 16, "occupied": True},
        {"temperature": 20, "occupied": False}
    ]

    print(f"{'Test #':<8}{str('Percept'):<32}{'Target Mode':<15}{'Send Command?':<15}")
    print("-" * 70)

    for i, percept in enumerate(test, 1):
        target_mode, send_cmd = agent.update_state(percept)
        print(f"{i:<8}{str(percept):<32}{target_mode:<15}{str(send_cmd):<15}")

if __name__ == "__main__":
    run_tests()