def build_graph():
    with open('Roads.xml', 'r') as roadsFile:
        xml = roadsFile.read()
        print(xml)
