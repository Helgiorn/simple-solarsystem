import untangle

obj = untangle.parse('sol.xml')

print (obj.root.child['name'])