d={"Eno":123,"Ename":"abc"}
print(d)
print(d["Eno"])
print(d.get("Ename"))
d["Ename"]="xyz"
print(d)
d["Age"]=18
print(d)
d.pop("Eno")
print(d)
d.popitem()
print(d)
d.clear()
print(d)

