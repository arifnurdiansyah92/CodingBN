import xml.etree.ElementTree as ET

# Parse XML from a file
tree = ET.parse('./files/student_data.xml')
root = tree.getroot()

print(f"Root element: {root.tag}")
print(f"Root attributes: {root.attrib}")

# Parse XML from a string
xml_string = """<students>
  <student id="101">
    <name>John Doe</name>
    <course>Mathematics</course>
  </student>
  <student id="102">
    <name>Jane Smith</name>
    <course>Physics</course>
  </student>
</students>
"""

root_from_string = ET.fromstring(xml_string)
for child in root_from_string:
    student_id = child.get('id')
    name = child.find('name').text
    course = child.find('course').text
    print(f"Student ID: {student_id}, Name: {name}, Course: {course}")
