import sys
import re


OutPutpwmFileName = sys.argv[1]
allPwmFile = sys.argv[2]
selected_motifs_name = map(lambda x:x.strip(),open(sys.argv[3]).readlines())
pwmFile = open(OutPutpwmFileName, 'wb')				
pwmFile.write('MEME version 4.4\nALPHABET= ACGT\nstrands: + -\nBackground letter frequencies (from web form):\nA 0.25000 C 0.25000 G 0.25000 T 0.25000\n\n')				
				
				
#read the allPWM file and get the sol PWMs and write them to a file				
flag = 0				
with open(allPwmFile, 'rb') as handler:				
	# print "asd"			
	for line in handler:			
			
		line = line.strip()		
		# print "This is the line in allpwm",line	
		if re.search(r'MOTIF', line):		
			# print "asd"	
			split = line.split()	
			motifName  = split[1]
			# print	motifName		
			if motifName in selected_motifs_name:	
				# print "In :",motifName
				flag = 1
				pwmFile.write(line + '\n')
				continue
			else:	
				flag = 0
				
		if flag == 1:		
			pwmFile.write(line + '\n')	
#close the file				
pwmFile.close()				
