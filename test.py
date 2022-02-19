import requests as ReQues_t

LisT = ReQues_t.get("https://google.com").text

abc = []
for i in LisT:
  print(i)
  abc.append(i)
  if abc.count(i) > 1:
    abc.remove(i)
    print("dupe: {}".format(i))
    
