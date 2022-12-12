a=[1,2,3,4]
print(a.append(6))
#
b= {
    "name":"abc",
    "company":"xyz",
    "college":"ecfgg"
}
#b["marks"]
key="marks"
if key in b:
    print(b[key])
else:
    print("doesn't exist")

key="name"
print(b.get(key,"key doesn't exist"))

print(b.values())