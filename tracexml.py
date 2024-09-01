# %%
import xml

# %%
import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\Ryzen\Downloads\dvdrental\py\actor\xl\worksheets\sheet1.xml')
print(tree)

# %%
root = tree.getroot()
# %%
print(root.attrib)
print(root.tag)
# %%
childlist=[]
for child in root:
    print((child.tag).replace("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}",""), child.attrib)
    childlist.append(child)
print(childlist)

# %%
for subchild in childlist:
    print((subchild.tag).replace("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}",""), subchild.attrib)
# %%
