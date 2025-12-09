#!/bin/bash

# Script to start all agent servers
# Usage: ./start_servers.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="$SCRIPT_DIR/logs"
PID_FILE="$SCRIPT_DIR/.server_pids"

# Create logs directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "Shutting down all servers..."
    if [ -f "$PID_FILE" ]; then
        while read pid; do
            if kill -0 "$pid" 2>/dev/null; then
                echo "Stopping process $pid..."
                kill "$pid" 2>/dev/null
            fi
        done < "$PID_FILE"
        rm -f "$PID_FILE"
    fi
    echo "All servers stopped."
    exit 0
}

# Trap signals to cleanup
trap cleanup SIGINT SIGTERM

# Start parser server (port 8001)
echo "Starting Parser Agent Server on port 8001..."
cd "$SCRIPT_DIR"
python3 parser_server.py > "$LOG_DIR/parser.log" 2>&1 &
PARSER_PID=$!
echo "$PARSER_PID" >> "$PID_FILE"
echo "  ✓ Parser server started (PID: $PARSER_PID)"

# Wait a moment for server to initialize
sleep 2

# Start analyzer server (port 8002)
echo "Starting Analyzer Agent Server on port 8002..."
python3 analyzer_server.py > "$LOG_DIR/analyzer.log" 2>&1 &
ANALYZER_PID=$!
echo "$ANALYZER_PID" >> "$PID_FILE"
echo "  ✓ Analyzer server started (PID: $ANALYZER_PID)"

# Wait a moment for server to initialize
sleep 2

# Start advisor server (port 8003)
echo "Starting Advisor Agent Server on port 8003..."
python3 advisor_server.py > "$LOG_DIR/advisor.log" 2>&1 &
ADVISOR_PID=$!
echo "$ADVISOR_PID" >> "$PID_FILE"
echo "  ✓ Advisor server started (PID: $ADVISOR_PID)"

# Wait a moment for server to initialize
sleep 2

echo ""
echo "=" | tr -d '\n' | head -c 60
echo ""
echo "All agent servers are running!"
echo ""
echo "Server Status:"
echo "  • Parser Server:   http://127.0.0.1:8001 (PID: $PARSER_PID)"
echo "  • Analyzer Server: http://127.0.0.1:8002 (PID: $ANALYZER_PID)"
echo "  • Advisor Server:  http://127.0.0.1:8003 (PID: $ADVISOR_PID)"
echo ""
echo "Logs are being written to: $LOG_DIR/"
echo ""
echo "Press Ctrl+C to stop all servers"
echo "=" | tr -d '\n' | head -c 60
echo ""

# Wait for all background processes
wait

