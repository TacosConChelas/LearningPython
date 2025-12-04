"""                 2) ----- The Config Parser (Logic Challenge)
Context: System configuration files often contain comments (lines starting with #) and empty lines 
    to make them readable for humans. However, your Python script needs clean data (Key/Value pairs) to configure a network device automatically.
Task: Implement a generator parse_config(path) that reads a configuration file line by line.
    Skip any line that is empty (or contains only whitespace).
    Skip any line that starts with a # (comments).
    For valid lines (e.g., key=value), split them by the = symbol and yield a tuple (key, value).
Example: Input line: hostname=CoreRouter01 Yields: ('hostname', 'CoreRouter01')
Hints:
    Use line.strip() to clean whitespace from both ends. If the result is an empty string "", it was an empty line.
    Use line.split('=') to separate the key from the value.
"""
def main():
    print("--- Loading Configuration ---")
    # Tu código aquí:
    # for setting in parse_config("router_config.conf"):
    #     print(f"Setting {setting[0]} to {setting[1]}")
    for setting in parse_config("router_config.conf"):
        print(f"Setting {setting[0]} to {setting[1]}")
        # print(setting)

def parse_config(path):
    with open(path) as file_config:
        for line in file_config:
            # we clean for any space in the line
            line = line.strip()
            # if after that the line is not False (because it doesn't have nothing for line.strip()) or if it doesn't starts with #
            if line and not line.startswith("#"):
                # the code execute
                yield line.split("=", 1)
                # yield line
if __name__ == "__main__":
    main()