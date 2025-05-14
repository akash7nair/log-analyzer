import re
from collections import defaultdict
from datetime import datetime

class LogAnalyzer:
    def __init__(self, log_path):
        self.log_path = log_path
        self.known_patterns = set()
        self.error_pattern = re.compile(r'ERROR|CRITICAL|FAILED', re.IGNORECASE)
        self.date_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    
    def _parse_log_line(self, line):
        date_match = self.date_pattern.search(line)
        if date_match:
            timestamp = datetime.strptime(date_match.group(), '%Y-%m-%d %H:%M:%S')
            message = line[date_match.end():].strip()
            return timestamp, message
        return None, None
    
    def analyze_timeframe(self, start_time, end_time):
        with open(self.log_path) as f:
            logs = [self._parse_log_line(line) for line in f]
        logs = [log for log in logs if log[0] and start_time <= log[0] <= end_time]
        
        return {
            'error_count': sum(1 for _, msg in logs if self.error_pattern.search(msg)),
            'unique_messages': len(set(msg for _, msg in logs)),
            'total_entries': len(logs)
        }