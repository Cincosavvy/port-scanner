# port-scanner
interacting with network and services and identifying open ports

## Features
- Scans a range of ports (default: 1 to 1024).
- Identifies open ports on remote systems.
- Uses `socket` library to check each port and reports whether it's open or closed.
- Displays the results with colorful output (using `termcolor`).
- Can be customized for scanning any IP or domain and any port range.

## Requirements

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/cincosavvy/port-scanner.git
