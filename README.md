# Ping Logger

A Python application to ping a specified host, log the results to a CSV file, and print statistics to the console. The project supports configurable packet sizes and optional CSV logging.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)
5. [License](#license)
6. [Contact Information](#contact-information)
7. [Acknowledgements](#acknowledgements)

## Installation

### Prerequisites

- Python 3.x

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project directory:
    ```sh
    cd your-repo
    ```

3. Create and activate the virtual environment using the provided batch files:
    - To create the virtual environment and activate it, run:
      ```sh
      venv_create.bat
      ```
    - If you need to activate the virtual environment later, run:
      ```sh
      venv_activate.bat
      ```
    - To deactivate the virtual environment, run:
      ```sh
      venv_deactivate.bat
      ```
    - To delete the virtual environment, run:
      ```sh
      venv_delete.bat
      ```

4. Install the required packages:
    ```sh
    venv_install_requirements.bat
    ```

5. To save the current list of installed packages to `venv_requirements.txt`, run:
    ```sh
    venv_save_requirements.bat
    ```

## Usage

CLI Usage:

```cmd
python main.py -H <host> -s <packet_size> [-f]
```
- `<host>` : The host to ping (default: 8.8.8.8)
- `<packet_size>` : The size of the ping packet in bytes (default: 32)
- `-f` : Enable logging to a CSV file (optional)

Example 1:
- Ping Google with 32-byte packets.
- Do not write output to CSV file, i.e. do not include the `-f` argument.

```cmd
python main.py -H 8.8.8.8 -s 32
```

Example 2:
- Ping local host with 128-byte packets.
- Write output to CSV file, i.e. Include the `-f` argument.

```cmd
python main.py -H 192.168.1.1 -s 128 -f
```

Code Usage:

```python
from app_config import AppConfig
from application import Application

if __name__ == "__main__":
    config = AppConfig().get_arguments()
    app = Application(config)
    app.run()
```

## Features
- Ping a specified host with a configurable packet size.
- Log ping results to a CSV file.
- Print statistics to the console.

## Contributing
Contributions are welcome! Please follow the contribution guidelines.
1. Fork the project.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact Information
- Twitter: [@rohingosling](https://x.com/rohingosling)
- Project Link: [https://github.com/your-username/your-repo](https://github.com/rohingosling/pinger)

## Acknowledgments
- [ping3](https://github.com/kyan001/ping3)
