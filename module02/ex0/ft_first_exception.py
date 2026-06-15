def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print("=== Velocidade do Carro ===\n")
    inputs = ["123","abc"]
    for input in inputs: 
        try: 
            print(f"Input data is '{input}'")
            temp = input_temperature(input)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e: 
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")
    

if __name__ == "__main__":
    test_temperature()
 