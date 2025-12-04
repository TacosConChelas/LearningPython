"""                     1) ----- The Error Filter
    Context: You are analyzing a massive server log file. You don't care 
    about "INFO" or "WARNING" messages; you only need to extract the critical 
    failures to alert the team.
Task: Implement a generator get_critical_errors(path) that opens a log file. It should 
iterate through the file and yield only the lines that contain the tag "[ERROR]".
    The lines yielded should be stripped of the trailing newline character.

    Use with open(...) to handle the file safely.
Hint: You can use the string method line.startswith("...") or simply the 
in operator (e.g., 'x' in line) to check the condition.    
"""
def main():
    print("--- Critical Errors Found ---")
    # Tu código aquí para iterar sobre el generador e imprimir las líneas
    # for error in get_critical_errors("server_logs.txt"): ...
    for error in get_critical_errors("server_logs.txt"):
        print(error)

def get_critical_errors(path):
    # Tu implementación aquí
    with open(path) as log_file:
        for line in log_file:
            if '[ERROR]' in line:
                yield line.strip()
    

if __name__ == "__main__":
    main()