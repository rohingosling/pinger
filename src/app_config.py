#-----------------------------------------------------------------------------------------------------------------------
# Module:  app_config.py
# Project: Pinger
# Author:  Rohin Gosling
#
# Description:
#
#   Command-line argument parsing for Pinger. Defines the AppConfig class, which builds the argument parser for the
#   host, packet size, and CSV-logging options and exposes the parsed arguments. The parser is a BannerArgumentParser,
#   which prepends a titled version banner to the help text shown by the -h/--help options.
#-----------------------------------------------------------------------------------------------------------------------

import argparse

# Application identity, shown in the banner that heads the command-line help text.

APPLICATION_NAME    = 'Pinger'
APPLICATION_VERSION = '1.0.0'
APPLICATION_TITLE   = f'{APPLICATION_NAME} (version {APPLICATION_VERSION})'


#-----------------------------------------------------------------------------------------------------------------------
# Class: BannerArgumentParser
#
# Description:
#
#   An argparse.ArgumentParser that prepends the application title banner, surrounded by blank lines, to the standard
#   help text. The banner is shown whenever the help is displayed via the -h or --help options.
#-----------------------------------------------------------------------------------------------------------------------

class BannerArgumentParser ( argparse.ArgumentParser ):

    #-------------------------------------------------------------------------------------------------------------------
    # Function: format_help
    #
    # Description:
    #
    #   Build the help text, prepending the application title banner wrapped in blank lines to the parser's standard
    #   help output.
    #
    # Arguments:
    #
    #   None.
    #
    # Returns:
    #
    #   The help text string, led by the title banner.
    #-------------------------------------------------------------------------------------------------------------------

    def format_help ( self ):

        # Prepend the title banner, wrapped in blank lines, to the standard help text.

        return f'\n{APPLICATION_TITLE}\n\n' + super ().format_help ()


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

        self.parser = BannerArgumentParser (
            description = 'Ping a host with a specified packet size and report statistics.'
        )

        self.parser.add_argument (
            '-H',
            '--host',
            type    = str,
            default = '8.8.8.8',
            help    = 'Host to ping (default: 8.8.8.8)'
        )
        self.parser.add_argument (
            '-s',
            '--size',
            type    = int,
            default = 32,
            help    = 'Packet size in bytes (default: 32)'
        )
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
