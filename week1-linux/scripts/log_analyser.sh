#!/bin/bash

set -e

#---------------------
#LOG ANALYSER 


log_info() {
    echo "[INFO] $1"
}

log_error() {
    echo "[ERROR] $1"
}

print_separator() {
    echo "--------------------------"
}


if [  -z "$1" ]
then 
    echo "Usage: ./log_analyzer.sh <log_file_name>"
    exit 1
fi


LOG_FILE=$1


if [  ! -f  "$LOG_FILE" ]
then
    echo "Log file does not exist"
    exit 1
fi

echo ""

echo "Analaysis of Log File has Began"
echo ""
print_separator
echo ""
echo "LOG ANALYSIS REPORT"
echo ""
echo "DATE : $(date '+%Y-%m-%d %H:%M:%S')"
echo ""
print_separator
echo ""
echo ""
echo "Total number of lines in log file is:$(wc -l "$LOG_FILE")"
echo ""
print_separator
echo ""

echo "ENTRIES BY LEVEL"
echo ""
cut -d' ' -f3 "$LOG_FILE" | sort | uniq -c | sort -rn

echo ""
print_separator
echo ""
echo "ERRORS INFO"
echo ""

if grep -q "ERROR" "$LOG_FILE"
then
    grep "ERROR" "$LOG_FILE"
    echo ""
    echo "Total number of errors : $(grep -c "ERROR" "$LOG_FILE")"
else
    echo "NO ERRORS OCCUR"
fi

echo ""
print_separator
echo ""
echo "WARNING INFO"
echo ""

if grep -q "WARN" "$LOG_FILE"
then
    grep "WARN" "$LOG_FILE"
    echo ""
    echo "Total warnings are : $(grep -c "WARN" "$LOG_FILE")"
else
    echo "No warnings"
fi

