import re
with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'/\* ============================================\n   THREE\.JS — 3D SCROLL STORY.*?\}\)\(\);\n', re.DOTALL)
new_content = pattern.sub('/* 3D SCROLL STORY JS REMOVED */\n', content)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("SUCCESS")
