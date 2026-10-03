import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('server.py', 'r', encoding='utf-8') as fp:
    lines = fp.readlines()

print(f"Total lines in server.py: {len(lines)}")
# Check error handlers and potential unhandled exceptions
for i, line in enumerate(lines):
    if 'SELECT ' in line or 'INSERT INTO ' in line or 'UPDATE ' in line or 'DELETE FROM ' in line:
        # Check if inside try-except
        pass
    if 'int(' in line or 'float(' in line:
        # Check if parsing without try/except
        if any(k in line for k in ['payload.get', 'self._json.get', 'params.get', 'query.get']):
            # see context
            ctx = "".join(lines[max(0, i-3):min(len(lines), i+3)])
            if 'try:' not in ctx:
                print(f"[POTENTIAL BUG] server.py:{i+1} parses int/float without try-except:\n  {line.strip()}")
