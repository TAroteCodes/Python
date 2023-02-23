#set is unorderd,homogenius,mutable
#no duplicates are allowded
S={10,20,30,40,50,50,'A'}
print(S)
print(len(S))
print(50 in S)
S.add(100)
print(S)
S.pop()
print(S)
S.pop()
print(S)
S.remove(100)
print(S)
T={55,57,20,40,45,15}
A={50,20,40,35}
Z=T.union(A)
print(Z)
B=T.symmetric_difference(A)
print(B)
C={55,57,45}
print(T.issuperset(C))
C.discard(57)
print(C)
