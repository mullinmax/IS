import sys

	
# features = [sys.argv[1]]

# fimo_file = "/users/PHS0293/ohu0404/project/Brugia/FC4/L3_L3D6/L3_L3D6/L3_L3D6_Motif_Scanning/L3_L3D6_fore_Fimo/fimo.txt"
# fimo_file = "/users/PHS0293/ohu0404/project/Brugia/FC4/L3_L3D9/L3_L3D9/L3_L3D9_Motif_Scanning/L3_L3D9_fore_Fimo/fimo.txt"
fimo_file = sys.argv[1]
label = fimo_file.split(".")[0]
my_dict = {}

flag = True
with open(fimo_file) as f:
	for line in f:
		if flag:
			flag = False
			continue
		line = line.strip().split()
		motif = line[0]
		# if not motif in features:
		# 	continue
		seq = line[1]
		if not my_dict.has_key(seq):
			my_dict[seq] = {}
		if not my_dict[seq].has_key(motif):
			my_dict[seq][motif] = []
		start = line[2]
		end = line[3]
		strand = line[4]
		p_value = line[6]
		score = float(line[5])
		
		if strand == "+":
			my_dict[seq][motif].append([start,end,"D",score])
		if strand == "-":
			my_dict[seq][motif].append([start,end,"R",score])
out = open(label + "_feature_map.tsv","wb")

for key1 in my_dict:
	for key2 in my_dict[key1]:
		for item in my_dict[key1][key2]:
			strand = item[2]
			start = item[0]
			end = item[1]
			outline = [key1,"site",key2,strand,start,end]
			print >>out,"\t".join(outline)