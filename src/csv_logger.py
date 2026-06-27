#-----------------------------------------------------------------------------------------------------------------------
# Module:  csv_logger.py
# Project: Pinger
# Author:  Rohin Gosling
#
# Description:
#
#   CSV logging for Pinger. Defines the CSVLogger class, which creates a CSV file, writes the header row, and appends a
#   row of ping statistics per call, closing the file on shutdown.
#-----------------------------------------------------------------------------------------------------------------------

import csv


#-----------------------------------------------------------------------------------------------------------------------
# Class: CSVLogger
#
# Description:
#
#   Manages CSV file operations for logging ping statistics: opens the file, writes the header, appends rows, and closes
#   the file.
#
# Attributes:
#
#   file_name : The path of the CSV file being written.
#   file      : The open file handle.
#   writer    : The csv.writer wrapping the file.
#-----------------------------------------------------------------------------------------------------------------------

class CSVLogger:

    #-------------------------------------------------------------------------------------------------------------------
    # Function: __init__
    #
    # Description:
    #
    #   Open the CSV file for writing and write the header row.
    #
    # Arguments:
    #
    #   file_name : The name of the CSV file to create.
    #   header    : The header row to write first.
    #
    # Returns:
    #
    #   None.
    #-------------------------------------------------------------------------------------------------------------------

    def __init__ ( self, file_name, header ):

        # Open the CSV file for writing and write the header row.

        self.file_name = file_name
        self.file      = open ( self.file_name, mode = 'w', newline = '' )
        self.writer    = csv.writer ( self.file )

        self.writer.writerow ( header )

    #-------------------------------------------------------------------------------------------------------------------
    # Function: __del__
    #
    # Description:
    #
    #   Ensure the file is closed when the CSVLogger object is destroyed.
    #
    # Arguments:
    #
    #   None.
    #
    # Returns:
    #
    #   None.
    #-------------------------------------------------------------------------------------------------------------------

    def __del__ ( self ):

        # Ensure the file is closed when the object is garbage-collected.

        self.close ()

    #-------------------------------------------------------------------------------------------------------------------
    # Function: write_row
    #
    # Description:
    #
    #   Write a single row of data to the CSV file.
    #
    # Arguments:
    #
    #   row : The row of data to write to the CSV file.
    #
    # Returns:
    #
    #   None.
    #-------------------------------------------------------------------------------------------------------------------

    def write_row ( self, row ):

        # Write a single row of data to the CSV file.

        self.writer.writerow ( row )

    #-------------------------------------------------------------------------------------------------------------------
    # Function: close
    #
    # Description:
    #
    #   Close the CSV file.
    #
    # Arguments:
    #
    #   None.
    #
    # Returns:
    #
    #   None.
    #-------------------------------------------------------------------------------------------------------------------

    def close ( self ):

        # Close the CSV file.

        self.file.close ()
