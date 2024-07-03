import argparse

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Class to handle command-line arguments and store program configurations.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

class AppConfig:    
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Constructor
    #
    # Initialize the AppConfig class and parse command-line arguments.
    #    
    # Attributes:
    #   host (str):                  The host to ping.
    #   packet_size (int):           The size of the ping packet in bytes.
    #   file_logging_enabled (bool): Flag to enable logging to CSV file.
    #
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__ ( self ):
        
        self.parser = argparse.ArgumentParser ( description = 'Ping a host with a specified packet size and report statistics.' )

        self.parser.add_argument ( '-H', '--host', type   = str,          default = '8.8.8.8', help = 'Host to ping (default: 8.8.8.8)'    )
        self.parser.add_argument ( '-s', '--size', type   = int,          default = 32,        help = 'Packet size in bytes (default: 32)' )
        self.parser.add_argument ( '-f', '--file', action = 'store_true',                      help = 'Enable logging to CSV file'         )

        self.args = self.parser.parse_args ()
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Return the parsed command-line arguments.
    #
    # Returns:
    #   argparse.Namespace: The parsed arguments.
    #
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_arguments ( self ):
        
        return self.args
