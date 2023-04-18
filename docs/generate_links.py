import re
import yaml

# Open the input file
with open('index.md', 'r') as f:
    content = f.read()

# Find all lines starting with "#" symbol
data = []
pattern = re.compile(r'^#\s+(\w+.+)$', re.MULTILINE)
matches = pattern.findall(content)
for name in matches:
    link = re.sub(r'\W+', '-', name) # Replace non-alphanumeric characters with "-"
    data.append({'name': name, 'link': "#" + link.lower().strip("-")})

# Write the list to a YAML file
with open('_data/links.yml', 'w') as f:
    yaml.dump(data, f)
