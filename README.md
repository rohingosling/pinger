# Pinger

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![ping3](https://img.shields.io/badge/ping3-4.0.8-90A959?style=flat)
![PyInstaller](https://img.shields.io/badge/Packaging-PyInstaller-FFCA28?style=flat)

<p align="center">
  <img src="images/ping h 8 8 8 8 s 32.png" width="100%" alt="X">
</p>
<p align="right"><i>Terminal output.</i></p>

<br>


<p align="center">
  <img src="images/ping h 192 168 1 1 s 128 f - 2.png" width="100%" alt="X">
</p>
<p align="right"><i>CSV output.</i></p>

<br>


A Python application to ping a specified host, log the results to a CSV file, and print statistics to the console. The project supports configurable packet sizes and optional CSV logging.

**Q:** Why did I create this?<br>
**A:** Because I did'nt like the output format of the default Windows `ping` command. And, I felt like making a pinger, for fun. So, here we are. 

## 📑 Table of Contents

1. [✨ Features](#-features)
2. [🚀 Usage](#-usage)
3. [📦 Installation](#-installation)
4. [🔨 Building Executables](#-building-executables)
5. [📄 License](#-license)

## ✨ Features

- Ping a specified host with a configurable packet size.
- Log ping results to a CSV file.
- Print statistics to the console.

## 🚀 Usage

The executable takes the same command-line **arguments on every platform** — only the way you launch it differs. Build it first (see [🔨 Building Executables](#-building-executables)), then run it from the folder containing the binary:

| Platform | Launch | Privilege |
|----------|--------|-----------|
| Windows | `pinger.exe -H <host> -s <size> [-f]` | run from an **Administrator** prompt (raw ICMP) |
| Linux | `sudo ./pinger -H <host> -s <size> [-f]` | `sudo` / root (raw ICMP) |

- `<host>` : The host to ping (default: 8.8.8.8)
- `<size>` : The size of the ping packet in bytes (default: 32)
- `-f` : Enable logging to a CSV file (optional)

> Running from source instead of the executable? Use `python src/main.py` <br>with the same arguments (e.g. `python src/main.py -H 8.8.8.8 -s 32`).

**Example 1:**

- Ping Google with 32-byte packets.
- Do not write output to a CSV file, i.e. omit the `-f` argument.
- Press [Ctrl+C] to exit the program.

- Windows:

  ```cmd
  pinger.exe -H 8.8.8.8 -s 32
  ```

- Linux:

  ```sh
  sudo ./pinger -H 8.8.8.8 -s 32
  ```

- Output (identical on both platforms):

  <p align="center">
    <img src="images/ping h 8 8 8 8 s 32.png" width="100%" alt="X">
  </p>

**Example 2:**

- Ping local host with 128-byte packets.
- Write output to a CSV file, i.e. include the `-f` argument.
  - The file name will look similar to this: `ping_log_20250718_230821_192_168_1_1_128.csv`.
- Press [Ctrl+C] to exit the program.

- Windows:

  ```cmd
  pinger.exe -H 192.168.1.1 -s 128 -f
  ```

- Linux:

  ```sh
  sudo ./pinger -H 192.168.1.1 -s 128 -f
  ```

- Output (identical on both platforms):

  <p align="center">
    <img src="images/ping h 192 168 1 1 s 128 f.png" width="100%" alt="X">
  </p>

  <p align="center">
    <img src="images/ping h 192 168 1 1 s 128 f - 2.png" width="100%" alt="X">
  </p>

### Code Usage

```python
from app_config import AppConfig
from application import Application

if __name__ == "__main__":
    config = AppConfig().get_arguments()
    app = Application(config)
    app.run()
```

## 📦 Installation

There are two ways to get `pinger`: download a prebuilt executable (no Python required), or run it from source.

### Option 1 — Download the prebuilt executable (recommended)

1. Open the [**Releases**](https://github.com/rohingosling/pinger/releases/latest) page.
2. Under the latest release's **Assets**, download the binary for your platform:
    - **Windows:** `pinger.exe`
    - **Linux:** `pinger` (no file extension)
3. Run it with the arguments described in [🚀 Usage](#-usage):
    - **Windows** — from an **Administrator** PowerShell or Command Prompt, in the folder where you saved it:

      ```powershell
      .\pinger.exe -H 8.8.8.8 -s 32
      ```

      In PowerShell the leading `.\` is required, and you may need to right-click the file → **Properties → Unblock** it the first time.
    - **Linux** — mark it executable, then run it with `sudo`:

      ```sh
      chmod +x pinger
      sudo ./pinger -H 8.8.8.8 -s 32
      ```

Elevation (Administrator / `sudo`) is required because `pinger` sends raw ICMP packets.

### Option 2 — Run from source

#### Prerequisites

- Python 3.x

#### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/rohingosling/pinger.git
    ```

2. Navigate to the project directory:

    ```sh
    cd pinger
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

## 🔨 Building Executables

`pinger` can be packaged into a single self-contained executable with [PyInstaller](https://pyinstaller.org/), so it runs on machines without Python installed. The build produces `pinger.exe` on Windows and `pinger` on Linux. (Linux executables carry no file extension — they are identified by their executable permission bit and ELF header, not by a `.exe`-style suffix.)

> **PyInstaller does not cross-compile.** Build the Windows `.exe` on a Windows machine and the Linux binary on a Linux machine; one host cannot produce both. Both builds use the same `src/main.py` entry point and the dependencies in `venv_requirements.txt` (which includes PyInstaller). Because `pinger` sends raw ICMP packets, the built binary still needs Administrator (Windows) or `root` / `cap_net_raw` (Linux) privileges to run.

### Windows → `pinger.exe`

From the project folder:

```cmd
venv_create.bat
venv_install_requirements.bat
build.bat
```

`build.bat` writes the executable to `dist\pinger.exe`. Run it, for example:

```cmd
dist\pinger.exe -H 8.8.8.8 -s 32 -f
```

### Linux → `pinger`

From the project folder:

```sh
python3 -m venv venv
venv/bin/pip install -r venv_requirements.txt
bash build.sh
```

`build.sh` writes the executable to `dist/pinger`. Run it, for example:

```sh
sudo ./dist/pinger -H 8.8.8.8 -s 32 -f
```

## 📄 License

Released under the [MIT License](LICENSE) — Copyright © 2023 Rohin Gosling.
