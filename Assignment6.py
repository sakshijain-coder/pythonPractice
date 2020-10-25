while(1):
    name=input("enter name:")
    if (name.isalpha() and name.isprintable() and len(name)>5):
        break;
print("name is:",name)
