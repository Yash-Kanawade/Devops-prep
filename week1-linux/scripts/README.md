# week 1 - Linux scripts
## log_analyser.sh
Analyses application log files and generate a health summary report.
###Usage 
'''bash
./log_analyser.sh <logfile>
'''
## what it does 
- Validate input and checks files exists
- Reports total line count
- Breaks down entries by log level 
- Lists all error messages
- Prints health and unhealthy status
- Prints all the WARN messages including the count of WARN messgae
echo ""
##skills demonstrated
- Bash scripting : function , conditionals, loop , exit codes
- Text Processing : grep ,cut ,ec
- Input validation and defensive scripting (set -e , set -u)
echo ""
