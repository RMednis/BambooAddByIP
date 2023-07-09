# Your BambuStudio system's IP Address
TARGET_IP = "127.0.0.1"

# Your Printer's IP
PRINTER_IP = "10.1.1.6"

# The USN (Unique Serial Number) of your printer
# You can see this in the printer's menu
PRINTER_USN = "000000000000000"

# Set this to your model.
# X1 Carbon - "3DPrinter-X1-Carbon"
# X1        - "3DPrinter-X1"
# P1P       - "C11"
PRINTER_DEV_MODEL = "C11"

# Device name... What to show the printer as in the UI
PRINTER_DEV_NAME = "SuperCoolPrinter"

# Run BambuStudio before sending magic packet?
RUN_BSTUDIO = True

# BambuStudio path
BSTUDIO_PATH = "../bambu-studio.exe"

# Time to wait between packets (Seconds)
WAIT_TIME = 5

# !! May want to not change these !!
# Reported Signal Strength (Changes indicator on BambuStudio)
PRINTER_DEV_SIGNAL = "-44"
# Is the printer in LAN Mode ?
PRINTER_DEV_CONNECT = "lan"
# Does the printer have a Cloud User account bound? "free" - none
PRINTER_DEV_BIND = "free"
