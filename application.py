import time
from   pinger     import Pinger
from   csv_logger import CSVLogger
from   datetime   import datetime

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Class to orchestrate the ping application, integrating Pinger and CSVLogger.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

class Application:

    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Initialize the PingApplication with the given configuration.
    #    
    # Args:
    #   config (argparse.Namespace): The configuration parsed from command-line arguments.
    #
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def __init__ ( self, config ):
        
        self.config     = config
        self.pinger     = Pinger    ( config.host, config.size )
        self.csv_logger = CSVLogger ( self.generate_file_name(), self.generate_csv_header() ) if config.file else None
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Generate the CSV file name based on current time, host, and packet size.
    #
    # Returns:
    #   str: The generated file name.
    #
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    def generate_file_name ( self ):
     
        time_now       = datetime.now ().strftime ( "%Y%m%d_%H%M%S" )
        host_formatted = self.config.host.replace ( '.', '_' )
        
        return f'ping_log_{time_now}_{host_formatted}_{self.config.size}.csv'
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Generate the CSV header row.
    #
    # Returns:
    #   list: The CSV header row.
    #
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    def generate_csv_header ( self ):
        
        return [ 'time_stamp', 'host', 'packet_size', 'delay', 'min', 'max', 'average', 'packet_count', 'lost_packet_count', 'lost_packet_percentage', 'success' ]
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Main loop to perform pings and log results.
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    def run ( self ):
        
        try:

            while True:

                delay = self.pinger.ping_once ()
                self.pinger.update_statistics ( delay )
                self.pinger.print_console_output ()
                
                if self.csv_logger:
                    self.csv_logger.write_row ( self.pinger.get_csv_row ( delay ) )
                
                time.sleep ( self.pinger.ping_interval )

        except KeyboardInterrupt:

            print ( '\nPing process interrupted by user.\n' )

            if self.csv_logger:
                self.csv_logger.close ()

        except Exception as e:

            print ( f"Ping to {self.config.host} failed with error: {str(e)}" )

            if self.csv_logger:
                self.csv_logger.close ()
