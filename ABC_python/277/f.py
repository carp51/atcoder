A = {1, 3, 4, 5, 8, 10, 12, 15}
B = {2, 3, 5, 6, 9, 11, 12, 15}
C = {1, 3, 6, 7, 10, 11, 13, 14, 15}

#(1)
three_cap = A & B & C

print(three_cap)

#(2)
AB_cap = A & B
BC_cap = B & C
CA_cap = C & A

print((AB_cap | BC_cap | CA_cap) - three_cap)

#(3)
three_cup = A | B | C

print(three_cup - (AB_cap | BC_cap | CA_cap))