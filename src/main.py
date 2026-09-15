#-----------------------------------------------------------------------------------------------------------------------
# Program: Pinger
# Author:  Rohin Gosling
#
# Description:
#
#   Entry point for Pinger, a command-line utility that repeatedly pings a host, prints live latency statistics to the
#   console, and optionally logs each result to a CSV file. Parses the command-line arguments, constructs the
#   application controller, and runs the ping loop until interrupted with Ctrl-C.
#
# Usage:
#
#   python src/main.py -H <host> -s <packet_size> [-f]
#   python src/main.py -H 8.8.8.8 -s 32
#   python src/main.py -H 192.168.1.1 -s 128 -f
#-----------------------------------------------------------------------------------------------------------------------

from app_config  import AppConfig
from application import Application

if __name__ == "__main__":

    # Parse the command-line arguments, build the application, and run the ping loop.

    config = AppConfig ().get_arguments ()
    app    = Application ( config )

    app.run ()
