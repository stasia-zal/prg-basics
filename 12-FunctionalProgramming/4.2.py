sp=[48,47,54,50,42,68,39,46]
print('Recorded values:',*sp)
print('Speed too high:',*list(filter(lambda x:x>50,sp)))