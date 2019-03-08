acl = int(input("What is the IPv4 ACL number?"))

if acl >=1 and acl <=99:
    print("This is a standard IPv4 ACL.")
elif acl >=100 and acl<=199:
    print("This is a extanded IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")
