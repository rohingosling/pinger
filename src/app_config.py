#-----------------------------------------------------------------------------------------------------------------------
# Module:  app_config.py
# Project: Pinger
# Author:  Rohin Gosling
#
# Description:
#
#   Command-line argument parsing for Pinger. Defines the AppConfig class, which builds the argparse parser for the
#   host, packet size, and CSV-logging options and exposes the parsed arguments.
#-----------------------------------------------------------------------------------------------------------------------

import argparse


#-----------------------------------------------------------------------------------------------------------------------
# Class: AppConfig
#
# Description:
#
#   Parses and stores the program configuration from the command line: the target host, the ping packet size, and
#   whether logging to a CSV file is enabled.
#
# Attributes:
#
#   parser : The argparse.ArgumentParser configured with the program's options.
#   args   : The parsed command-line arguments (host, size, file).
#-----------------------------------------------------------------------------------------------------------------------

class AppConfig:

    #-------------------------------------------------------------------------------------------------------------------
    # Function: __init__
    #
    # Description:
    #
    #   Build the argument parser with the -H/--host, -s/--size, and -f/--file options and parse the command line.
    #
    # Arguments:
    #
    #   None.
    #
    # Returns:
    #
    #   None.
    #-------------------------------------------------------------------------------------------------------------------

    def __init__ ( self ):

        # Build the command-line argument parser and parse the arguments.

        self.parser = argparse.ArgumentParser ( description = 'Ping a host with a specified packet size and report statistics.' )

        self.parser.add_argument ( '-H', '--host', type = str, default = '8.8.8.8', help = 'Host to ping (default: 8.8.8.8)' )
        self.parser.add_argument ( '-s', '--size', type = int, default = 32, help = 'Packet size in bytes (default: 32)' )
        self.parser.add_argument ( '-f', '--file', action = 'store_true', help = 'Enable logging to CSV file' )

        self.args = self.parser.parse_args ()

    #-------------------------------------------------------------------------------------------------------------------
    # Function: get_arguments
    #
    # Description:
    #
    #   Return the parsed command-line arguments.
    #
    # Arguments:
    #
    #   None.
    #
    # Returns:
    #
    #   The parsed argparse.Namespace of command-line arguments.
    #-------------------------------------------------------------------------------------------------------------------

    def get_arguments ( self ):

        # Return the parsed command-line arguments.

        return self.args
