
import time
from   ping3    import ping
from   datetime import datetime

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Class to perform ping operations and maintain ping statistics.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

class Pinger:

    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Constructor
    #
    # Initialize the Pinger class with the host and packet size.
    #    
    # Args:
    #   host (str): The host to ping.
    #   packet_size (int): The size of the ping packet in bytes.
    #
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__ ( self, host, packet_size ):
        
        self.host              = host
        self.packet_size       = packet_size
        
        self.delay_min         = float ( 'inf' )
        self.delay_max         = 0
        self.delay_sum         = 0
        self.ping_count        = 0
        self.packet_loss_count = 0
        self.ping_interval     = 1
        self.delay_average     = 0

    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Perform a single ping operation.
    #     
    # Returns:
    #   float: The delay in seconds if successful, None otherwise.
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    def ping_once ( self ):
        
        return ping ( self.host, size=self.packet_size )
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Update statistics based on the ping result.
    #
    # Args:
    #   delay (float): The delay in seconds returned by the ping.
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    def update_statistics ( self, delay ):
        
        if delay is not None:
            delay_ms = delay * 1000  # Convert delay to milliseconds
            
            # Update min delay
            if delay_ms < self.delay_min:
                self.delay_min = delay_ms
            
            # Update max delay
            if delay_ms > self.delay_max:
                self.delay_max = delay_ms
            
            # Update delay sum and average
            self.delay_sum     += delay_ms
            self.ping_count    += 1
            self.delay_average  = self.delay_sum / self.ping_count
        else:
            self.packet_loss_count += 1

    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Print the current statistics to the console.
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    def print_console_output ( self ):
        
        timestamp              = datetime.now ().strftime ( "%Y-%m-%d %H:%M:%S.%f" )[:-3]
        host_string            = f'"{self.host}"'
        packet_loss_percentage = ( self.packet_loss_count / ( self.ping_count + self.packet_loss_count ) ) * 100
        console_string         = f'{timestamp}    Ping: {host_string}    Packet Size: {self.packet_size} bytes    '

        if self.ping_count > 0:
            console_string += (
                f'Delay: {self.delay_sum / self.ping_count:.1f} ms    '
                f'Min: {self.delay_min:.1f} ms    '
                f'Max: {self.delay_max:.1f} ms    '
                f'Average: {self.delay_average:.1f} ms    '
            )
        console_string += f'Packets Sent: {self.ping_count}    Packets Lost: {self.packet_loss_count} ({packet_loss_percentage:.2f}%)'

        print ( console_string )

    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Get the current statistics as a CSV row.
    #    
    # Args:
    #   delay (float): The delay in seconds returned by the ping.
    #    
    # Returns:
    #   list: The current statistics as a list suitable for CSV writing.
    #---------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_csv_row ( self, delay ):
        
        timestamp              = datetime.now ().strftime ( "%Y-%m-%d %H:%M:%S.%f" )[:-3]
        packet_loss_percentage = ( self.packet_loss_count / ( self.ping_count + self.packet_loss_count ) ) * 100
        
        if delay is not None:

            delay_ms = delay * 1000  # Convert delay to milliseconds

            return [
                timestamp,
                self.host,
                self.packet_size,
                f'{delay_ms:.1f}',
                f'{self.delay_min:.1f}',
                f'{self.delay_max:.1f}',
                f'{self.delay_average:.1f}',
                self.ping_count,
                self.packet_loss_count,
                f'{packet_loss_percentage:.2f}',
                'TRUE'
            ]
        else:
            return [
                timestamp,
                self.host,
                self.packet_size,
                '-',
                '-',
                '-',
                '-',
                self.ping_count,
                self.packet_loss_count,
                f'{packet_loss_percentage:.2f}',
                'FALSE'
            ]
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Get the current statistics as a CSV row.
    #    
    # Args:
    #   arg_1 (type): Description of arg_1.
    #   arg_2 (type): Description of arg_2.
    #    
    # Returns:
    #   return_value: Description of return_value.
    #---------------------------------------------------------------------------------------------------------------------------------------------------------
