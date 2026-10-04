 Python System Monitor

A self-developed system monitor built with Python that tracks essential system resources in real time and displays them directly in the terminal.

The project was created to gain practical experience with Python, system monitoring, and processing system data.

 Features

- CPU Monitoring: Displays current CPU usage and the number of CPU cores.
- RAM Monitoring: Tracks memory usage and displays used and total memory.
- Disk Monitoring: Shows storage usage of the main drive.
- Network Monitoring: Tracks the total amount of data sent and received.
- Battery Monitoring: Displays the current battery level when a battery is detected.
- System Uptime: Calculates how long the system has been running.
- Process Analysis: Identifies the three processes with the highest memory usage.
- Real-Time Updates: Regularly refreshes system information.
- Cross-Platform Support: Supports different drive paths and terminal commands for Windows and other operating systems.

Technologies

- Python 3
- psutil – Retrieves system information and process data.
- OS – Detects the operating system and manages terminal commands.
- Datetime and Time – Handle timestamps and system uptime.

Installation

1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

2. Navigate to the project directory

```bash
cd YOUR-REPOSITORY
```

3. Install dependencies

```bash
python -m pip install psutil
```

4. Run the program

```bash
python sys_monitor.py
```
Example Output


SYSTEM MONITOR
Time:         14:32:10
Uptime:       5 hrs 42 min

CPU:          [###-------] 32% (8 cores)
RAM:          [#####-----] 54% (8.6 of 16.0 GB)
Disk:         [######----] 61% (305.0 of 500.0 GB)
Battery:      [########--] 82%

Network:
  received:   1250 MB
  sent:       340 MB

RAM-intensive processes:
  firefox                  12.4%
  Code                      8.7%
  python                    3.2%



Usage

Once started, the monitor runs automatically.

- System information is refreshed regularly.
- The terminal display is cleared and updated with each refresh.
- Press `Ctrl + C` to safely stop the program
-
- What I Learned

- Working with external Python libraries
- Retrieving and processing system information
- Structuring code with custom functions
- Using loops and conditional statements
- Handling exceptions and keyboard interrupts
- Sorting and analyzing process data
- Understanding basic cross-platform programming

Future Improvements

- Display real-time network speeds in MB/s
- Support monitoring multiple drives
- Add more advanced process information
- Implement a graphical user interface (GUI)
- Store and analyze historical system data



Project: Python System Monitor  
Language: Python  
Library: psutil  
