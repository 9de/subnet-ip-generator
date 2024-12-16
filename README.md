# subnet-ip-generator

A Python utility for generating random IP addresses within specified subnets. Perfect for network testing, simulation scenarios, and educational purposes.

## Features

- Generate random IP addresses within any valid IPv4 subnet
- Input validation and robust error handling
- Command history tracking
- Automatic clipboard integration
- Cross-platform compatibility

## Installation

1. Clone the repository:
```bash
git clone https://github.com/9de/subnet-ip-generator.git
cd subnet-ip-generator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python subnettoIp.py
```

Available commands:
- Enter a subnet (e.g., `216.114.75.0/24`) to generate a random IP
- Type `history` to view previously generated IPs
- Type `clear` to clear the generation history
- Type `exit` to quit the program

Example:
```bash
Enter a subnet (e.g., 216.114.75.0/24): 192.168.1.0/24
Random IP from 192.168.1.0/24: 192.168.1.57
IP address copied to clipboard.
```

## Requirements

- Python 3.7+
- pyperclip
- ipaddress (included in Python standard library)

## Error Handling

The tool includes comprehensive error handling for:
- Invalid subnet formats
- Network/broadcast address exclusion
- Clipboard operation failures
- Keyboard interrupts

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using Python's ipaddress library
- Clipboard functionality provided by pyperclip
