#-----------------------------------------------------------------------------------------------------------------------
# Module:  application.py
# Project: Pinger
# Author:  Rohin Gosling
#
# Description:
#
#   Application controller for Pinger. Defines the Application class, which orchestrates the ping loop, integrating the
#   Pinger statistics engine with optional CSVLogger output and handling graceful shutdown.
#-----------------------------------------------------------------------------------------------------------------------

import time
from pinger     import Pinger
from csv_logger import CSVLogger
from datetime   import datetime


#-----------------------------------------------------------------------------------------------------------------------
# Class: Application
#
# Description:
#
#   Orchestrates the ping application, integrating the Pinger and CSVLogger components and running the main ping loop
#   until the user interrupts it.
#
# Attributes:
#
#   config     : The parsed command-line configuration.
#   pinger     : The Pinger instance that performs pings and tracks statistics.
#   csv_logger : The CSVLogger instance when CSV logging is enabled, otherwise None.
#-----------------------------------------------------------------------------------------------------------------------

class Application:

    #-------------------------------------------------------------------------------------------------------------------
    # Function: __init__
    #
    # Description:
    #
    #   Store the configuration and create the Pinger and, when CSV logging is enabled, the CSVLogger.
    #
    # Arguments:
    #
    #   config : The parsed command-line configuration (argparse.Namespace).
    #
    # Returns:
    #
    #   None.
    #-------------------------------------------------------------------------------------------------------------------

    def __init__ ( self, config ):

        # Store the configuration and create the Pinger and (optional) CSVLogger.

        self.config     = config
        self.pinger     = Pinger ( config.host, config.size )
        self.csv_logger = CSVLogger ( self.generate_file_name (), self.generate_csv_header () ) if config.file else None

    #-------------------------------------------------------------------------------------------------------------------
    # Function: generate_file_name
    #
    # Description:
    #
    #   Build a timestamped CSV file name from the current time, the target host, and the packet size.
    #
    # Arguments:
    #
    #   None.
    #
    # Returns:
    #
    #   The generated CSV file name string.
    #-------------------------------------------------------------------------------------------------------------------

    def generate_file_name ( self ):

        # Build a timestamped CSV file name from the current time, host, and packet size.

        time_now       = datetime.now ().strftime ( "%Y%m%d_%H%M%S" )
        host_formatted = self.config.host.replace ( '.', '_' )

        # Return data to caller.

        return f'ping_log_{time_now}_{host_formatted}_{self.config.size}.csv'

    #-------------------------------------------------------------------------------------------------------------------
    # Function: generate_csv_header
    #
    # Description:
    #
    #   Return the CSV header row naming each logged statistic.
    #
    # Arguments:
    #
    #   None.
    #
    # Returns:
    #
    #   The CSV header row as a list of column names.
    #-------------------------------------------------------------------------------------------------------------------

    def generate_csv_header ( self ):

        # Return the CSV header row.

        return [ 'time_stamp', 'host', 'packet_size', 'delay', 'min', 'max', 'average', 'packet_count', 'lost_packet_count', 'lost_packet_percentage', 'success' ]

    #-------------------------------------------------------------------------------------------------------------------
    # Function: run
    #
    # Description:
    #
    #   Run the main loop: ping the host once per interval, update and print statistics, and optionally log each result,
    #   until interrupted with Ctrl-C or stopped by an error. The CSV log file is closed on shutdown.
    #
    # Arguments:
    #
    #   None.
    #
    # Returns:
    #
    #   None.
    #-------------------------------------------------------------------------------------------------------------------

    def run ( self ):

        # Ping the host once per interval, printing and optionally logging each result, until interrupted.

        try:

            while True:

                delay = self.pinger.ping_once ()
                self.pinger.update_statistics ( delay )
                self.pinger.print_console_output ()

                if self.csv_logger:
                    self.csv_logger.write_row ( self.pinger.get_csv_row ( delay ) )

                time.sleep ( self.pinger.ping_interval )

        except KeyboardInterrupt:

            # Ctrl-C: stop cleanly and close the log file.

            print ( '\nPing process interrupted by user.\n' )

            if self.csv_logger:
                self.csv_logger.close ()

        except Exception as e:

            # Any other failure: report it and close the log file.

            print ( f"Ping to {self.config.host} failed with error: {str(e)}" )

            if self.csv_logger:
                self.csv_logger.close ()
