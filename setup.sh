#!/bin/bash

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check for Termux
if [[ -d "/data/data/com.termux" ]]; then
    echo -e "${GREEN}[✓] Termux detected${NC}"
else
    echo -e "${YELLOW}[!] Not in Termux environment${NC}"
fi

# Create virtual environment
echo -e "${YELLOW}[*] Setting up Python environment...${NC}"
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install colorama

# Make scripts executable
chmod +x main.py
chmod +x ua_generator.sh

echo -e "${GREEN}[✓] Setup Complete! 
Run Python version: python main.py
Run Bash version: ./ua_generator.sh${NC}"
