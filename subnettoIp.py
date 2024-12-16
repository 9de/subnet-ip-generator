#!/usr/bin/env python3
"""
IP Address Generator

A tool for generating random IP addresses within specified subnets.
Includes input validation, error handling, and clipboard integration.
"""

import ipaddress
import random
import pyperclip
from typing import Optional, List, Union, Tuple
import re


class SubnetError(Exception):
    """Custom exception for subnet-related errors."""
    pass


class IPGenerator:
    """Handles generation of random IP addresses within specified subnets."""
    
    def __init__(self):
        self.history: List[Tuple[str, str]] = []  # Store (subnet, generated_ip) pairs
    
    @staticmethod
    def validate_subnet(subnet: str) -> bool:
        """
        Validate subnet notation format before parsing.
        
        Args:
            subnet: String representation of an IP subnet
            
        Returns:
            bool: True if the subnet notation is valid
        """
        subnet_pattern = r'^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$'
        return bool(re.match(subnet_pattern, subnet))
    
    def generate_random_ip(self, subnet: str) -> str:
        """
        Generate a random IP address within the specified subnet.
        
        Args:
            subnet: String representation of an IP subnet (e.g., '192.168.1.0/24')
            
        Returns:
            str: A random IP address within the subnet
            
        Raises:
            SubnetError: If the subnet is invalid or contains no usable hosts
        """
        if not self.validate_subnet(subnet):
            raise SubnetError("Invalid subnet format. Use notation like '192.168.1.0/24'")
            
        try:
            network = ipaddress.IPv4Network(subnet, strict=False)
            ip_range = list(network.hosts())
            
            if not ip_range:
                raise SubnetError(f"No usable hosts in subnet {subnet}")
                
            random_ip = str(random.choice(ip_range))
            self.history.append((subnet, random_ip))
            return random_ip
            
        except ValueError as e:
            raise SubnetError(f"Invalid subnet: {str(e)}")
    
    def get_history(self) -> List[Tuple[str, str]]:
        """Return the history of generated IPs."""
        return self.history
    
    def clear_history(self) -> None:
        """Clear the generation history."""
        self.history.clear()


def copy_to_clipboard(text: str) -> bool:
    """
    Safely copy text to clipboard.
    
    Args:
        text: String to copy to clipboard
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        pyperclip.copy(text)
        return True
    except Exception:
        return False


def main() -> None:
    """Main program loop."""
    generator = IPGenerator()
    
    print("Random IP Address Generator")
    print("Enter 'exit' to quit, 'history' to view previous generations")
    print("'clear' to clear history\n")
    
    while True:
        try:
            user_input = input("\nEnter a subnet (e.g., 104.17.112.0/20): ").strip().lower()
            
            if user_input == 'exit':
                print("\nExiting program. Goodbye!")
                break
                
            elif user_input == 'history':
                history = generator.get_history()
                if history:
                    print("\nGeneration History:")
                    for subnet, ip in history:
                        print(f"Subnet: {subnet} → IP: {ip}")
                else:
                    print("\nNo generation history available.")
                continue
                
            elif user_input == 'clear':
                generator.clear_history()
                print("\nHistory cleared.")
                continue
            
            random_ip = generator.generate_random_ip(user_input)
            print(f"\nRandom IP from {user_input}: {random_ip}")
            
            if copy_to_clipboard(random_ip):
                print("IP address copied to clipboard.")
            else:
                print("Warning: Could not copy to clipboard.")
                
        except SubnetError as e:
            print(f"\nError: {str(e)}")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\nUnexpected error: {str(e)}")


if __name__ == "__main__":
    main()