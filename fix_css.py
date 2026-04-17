import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the double color issue and make it brighter and sharper
    content = re.sub(
        r'\.section-title\{text-shadow:.*?; color: #ffffff;(.*?)color:var\(--text\);\}',
        r'.section-title{\1color:#ffffff; text-shadow: 0 0 1px rgba(255,255,255,0.4), 0 0 12px rgba(56,189,248,0.7);}',
        content
    )
    content = re.sub(
        r'\.pcard-title\{text-shadow:.*?; color: #ffffff;(.*?)color:var\(--text\);\}',
        r'.pcard-title{\1color:#ffffff; text-shadow: 0 0 1px rgba(255,255,255,0.3), 0 0 10px rgba(56,189,248,0.6);}',
        content
    )
    content = re.sub(
        r'\.aaa-card h3\{text-shadow:.*?; color: #ffffff;(.*?)color:var\(--text\);\}',
        r'.aaa-card h3{\1color:#ffffff; text-shadow: 0 0 1px rgba(255,255,255,0.3), 0 0 10px rgba(56,189,248,0.6);}',
        content
    )
    content = re.sub(
        r'\.scard h4\{text-shadow:.*?; color: #ffffff;(.*?)color:var\(--text\);\}',
        r'.scard h4{\1color:#ffffff; text-shadow: 0 0 1px rgba(255,255,255,0.3), 0 0 10px rgba(56,189,248,0.6);}',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print('Fixed CSS double colors')
