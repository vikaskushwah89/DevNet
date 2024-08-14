# Import modules
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
import json
import yaml
from helper import *

# Main function
if __name__ == "__main__":
    #########################################
    #              Procedure 1              #
    #########################################
    # Add print statement here
    print("DevNet")

    #########################################
    #              Procedure 2              #
    #########################################
    print('##################')
    print('###### YAML ######')
    print('##################')

    user_yaml = {}
    # Open the user.yaml file as read only
    with open("DevAsc/user.yaml", 'r') as file:
        # Load the stream using safe_load
        user_yaml = yaml.safe_load(file)
        # Print the object type
        print("Type of user_yaml variable: " + type(user_yaml).__name__)
        print('----------------------')
        # Iterate over the keys of the user_yaml and print them
        print('Keys in user_yaml:')
        for key, value in user_yaml.items():
            print(key)
        print('----------------------')

    # Create a new instance of class User
    user = User()
    # Assign values from the user_yaml to the object user
    user.id = user_yaml['id']
    user.first_name = user_yaml['first_name']
    user.last_name = user_yaml['last_name']
    user.birth_date = user_yaml['birth_date']
    user.address = user_yaml['address']
    user.score = user_yaml['score']
    # Print the user object
    print('User object:')
    print(user)

    #########################################
    #              Procedure 3              #
    #########################################
    print('##################')
    print('###### JSON ######')
    print('##################')

    # Create JSON structure from the user object
    user_json = json.dumps(user, default = serializeUser)
    # Print the created JSON structure
    print('Print user_json:')
    print(user_json)
    print('----------------------')

    # Create JSON structure with indents and sorted keys
    print('JSON with indents and sorted keys')
    user_json = json.dumps(user, default=serializeUser, indent=4, sort_keys=True)
    print(user_json)
    #########################################
    #              Procedure 4              #
    #########################################
    print('######################')
    print('# XML - Element Tree #')
    print('######################')
    
    # Parse the user.xml file
    with open('DevAsc/user.xml', 'r') as xml_file:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        # Print the tags
        print("Tags in the XML:")
        for element in root:
            print(element.tag) 
        print('----------------------')    

        # Accessing element value
        print('Accessing element value')
        addresses = root.findall('address')
        print('----------------------')

        # Print elements from the tag name 'address'
        print('Addresses:')
        for address in addresses:
            for i in address:
                print(i.tag + ' : ' + i.text)

        print('----------------------')

        # Print the entire structure with printNodes
        print('The structure:')
        for k in root.iter():
            print(k.tag + ' : ' + k.text)

    # Parsing XML files with MiniDOM 
    print('######################')
    print('### XML - MiniDOM ####')
    print('######################')

    # Parse the user.xml file
    dom = MD.parse('DevAsc/user.xml')
    # Print the tags
    print('Tags in the XML:')
    for node in dom.childNodes:
        print(node.childNodes)
    
    # Accessing element value
    print('Accessing element value')
    idElements = dom.getElementsByTagName('id')
    print(idElements)
    elementId = idElements.item(0)
    print(elementId.childNodes)
    idValue = elementId.firstChild.data
    print(idValue)

    # Print elements from the DOM with tag name 'address'
    print("--------------------------")
    print('Addresses:')
    for node in dom.getElementsByTagName('address'):
        printNodes(node.childNodes)

    # Print the entire structure with printNodes
    print('The structure:')
    for node in dom.childNodes:
        printNodes(node.childNodes)
    
    #########################################
    #              Procedure 5              #
    #########################################
    print('######################')
    print('#   Use Namespaces   #')
    print('######################')

    # Parse the user.xml file
    itemTree = ET.parse('DevAsc/item.xml')
    # Get the root element
    root = itemTree.getroot()
    # Define namespaces 
    namespaces = {'a':'https://www.example.com/network', 'b':'https://www.example.com/furniture'}
    # Set table as the root element 
    elementsInNSa = root.findall('a:table', namespaces)
    elementsInNSb = root.findall('b:table', namespaces)
    # Elements in NS a
    print('Elements in NS a:')   
    for e in elementsInNSa:
        for i in e.iter():   
            print(i.tag + ':' + i.text)
    print('----------------------')

    # Elements in NS b
    print('Elements in NS b:')
    for element in list(elementsInNSb[0]):
        print(element.tag + ':' + element.text)