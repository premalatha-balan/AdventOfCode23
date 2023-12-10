def readFile2Data():
  f=open("day7_input.txt", "r")
  hands_dict={}
  hands_dict = {(line.strip().split())[0]: [int((line.strip().split())[1])] for line in f}
  f.close
  return(hands_dict)

