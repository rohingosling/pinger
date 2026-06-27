#-----------------------------------------------------------------------------------------------------------------------
# Module:  pinger.py
# Project: Pinger
# Author:  Rohin Gosling
#
# Description:
#
#   Core ping engine for Pinger. Defines the Pinger class, which sends ICMP echo requests via ping3 and maintains
#   running statistics (minimum, maximum, and average delay, and packet loss), formatting them for the console and for
#   CSV output.
#-----------------------------------------------------------------------------------------------------------------------

import time
from ping3    import ping
from datetime import datetime


#-----------------------------------------------------------------------------------------------------------------------
# Class: Pinger
#
# Description:
#
#   Performs ping operations and maintains running ping statistics: minimum, maximum, sum, and average round-trip delay,
#   the number of successful pings, and the number of lost packets.
#
# Attributes:
#
#   host              : The host to ping.
#   packet_size       : The size of the ping packet in bytes.
#   delay_min         : The minimum round-trip delay seen, in milliseconds.
#   delay_max         : The maximum round-trip delay seen, in milliseconds.
#   delay_sum         : The running sum of successful delays, in milliseconds.
#   ping_count        : The number of successful pings.
#   packet_loss_count : The number of failed pings.
#   ping_interval     : The delay between pings, in seconds.
#   delay_average     : The running average delay, in milliseconds.
#-----------------------------------------------------------------------------------------------------------------------

class Pinger:

    #-------------------------------------------------------------------------------------------------------------------
    # Function: __init__
    #
    # Description:
    #
    #   Store the target host and packet size and initialise the statistics counters.
    #
    # Arguments:
    #
    #   host        : The host to ping.
    #   packet_size : The size of the ping packet in bytes.
    #
    # Returns:
    #
    #   None.
    #-------------------------------------------------------------------------------------------------------------------

    def __init__ ( self, host, packet_size ):

        # Store the target host and packet size and initialise the statistics counters.

        self.host        = host
        self.packet_size = packet_size

        self.delay_min         = float ( 'inf' )
        self.delay_max         = 0
        self.delay_sum         = 0
        self.ping_count        = 0
        self.packet_loss_count = 0
        self.ping_interval     = 1
        self.delay_average     = 0

    #-------------------------------------------------------------------------------------------------------------------
    # Function: ping_once
    #
    # Description:
    #
    #   Send a single ICMP echo request to the host.
    #
    # Arguments:
    #
    #   None.
    #
    # Returns:
    #
    #   The round-trip delay in seconds if successful, None otherwise.
    #-------------------------------------------------------------------------------------------------------------------

    def ping_once ( self ):

        # Send a single ICMP echo to the host and return the round-trip delay.

        return ping ( self.host, size = self.packet_size )

    #-------------------------------------------------------------------------------------------------------------------
    # Function: update_statistics
    #
    # Description:
    #
    #   Update the running statistics from a single ping result. A successful delay updates the minimum, maximum, sum,
    #   and average; a failure (None) increments the packet-loss count.
    #
    # Arguments:
    #
    #   delay : The delay in seconds returned by the ping, or None on failure.
    #
    # Returns:
    #
    #   None.
    #-------------------------------------------------------------------------------------------------------------------

    def update_statistics ( self, delay ):

        # Update the running statistics from a single ping result.

        if delay is not None:
            delay_ms = delay * 1000  # Convert delay to milliseconds

            # Update min delay

            if delay_ms < self.delay_min:
                self.delay_min = delay_ms

            # Update max delay

            if delay_ms > self.delay_max:
                self.delay_max = delay_ms

            # Update delay sum and average

            self.delay_sum += delay_ms
            self.ping_count += 1
            self.delay_average = self.delay_sum / self.ping_count
        else:
            self.packet_loss_count += 1

    #-------------------------------------------------------------------------------------------------------------------
    # Function: print_console_output
    #
    # Description:
    #
    #   Build and print the current statistics line to the console: timestamp, host, packet size, delay, minimum,
    #   maximum, and average delay, packets sent, and packets lost with the loss percentage.
    #
    # Arguments:
    #
    #   None.
    #
    # Returns:
    #
    #   None.
    #-------------------------------------------------------------------------------------------------------------------

    def print_console_output ( self ):

        # Build and print the current statistics line for the console.

        timestamp              = datetime.now ().strftime ( "%Y-%m-%d %H:%M:%S.%f" ) [ : -3 ]
        host_string            = f'"{self.host}"'
        packet_loss_percentage = ( self.packet_loss_count / ( self.ping_count + self.packet_loss_count ) ) * 100
        console_string         = f'{timestamp}    Ping: {host_string}    Packet Size: {self.packet_size} bytes    '

        # Append the delay statistics (shown only after at least one successful ping) and the packet totals.

        if self.ping_count > 0:
            console_string += (
                f'Delay: {self.delay_sum / self.ping_count:.1f} ms    '
                f'Min: {self.delay_min:.1f} ms    '
                f'Max: {self.delay_max:.1f} ms    '
                f'Average: {self.delay_average:.1f} ms    '
            )
        console_string += f'Packets Sent: {self.ping_count}    Packets Lost: {self.packet_loss_count} ({packet_loss_percentage:.2f}%)'

        print ( console_string )

    #-------------------------------------------------------------------------------------------------------------------
    # Function: get_csv_row
    #
    # Description:
    #
    #   Build the current statistics as a CSV row. A successful ping records the delay and statistics; a failed ping uses
    #   "-" placeholders. The final column is the success flag ("TRUE" / "FALSE").
    #
    # Arguments:
    #
    #   delay : The delay in seconds returned by the ping, or None on failure.
    #
    # Returns:
    #
    #   The current statistics as a list suitable for CSV writing.
    #-------------------------------------------------------------------------------------------------------------------

    def get_csv_row ( self, delay ):

        # Build the current statistics as a CSV row, using "-" placeholders when the ping failed.

        timestamp              = datetime.now ().strftime ( "%Y-%m-%d %H:%M:%S.%f" ) [ : -3 ]
        packet_loss_percentage = ( self.packet_loss_count / ( self.ping_count + self.packet_loss_count ) ) * 100

        # Build the row according to whether the ping succeeded or failed.

        if delay is not None:

            delay_ms = delay * 1000  # Convert delay to milliseconds

            # Return the row for a successful ping.

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

            # Return the row for a failed ping.

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
