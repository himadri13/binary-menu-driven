import pickle as p
while True:
	print("WELCOME TO")
	print("FOOTBALL SCORECARD")
	print("1.insert records to bin file")
	print("2.display records")
	print("3.search record")
	print("4.delete record")
	print("5.update record")
	print("6.exit")
	ch=int(input("enter choice"))
	if ch==1:
		fl=open("football.dat",'ab')
		while True:
		    n=int(input("enter id"))
		    nm=input("enter name")
		    g=int(input("goals scored"))
		    dt={'id':n,'name':nm,'goals':g}
		    p.dump(dt,fl)
		    ch1=int(input('Another record (1-yes,2-no)'))
		    if ch1==2:
		    	break
		    	fl.close()
	if ch==2:
		fl=open('football.dat','rb')
		print ("{:<12} {:<12} {:<12}".format('ID', 'NAME', 'GOALS'))
		while True:
			try:
				dt=p.load(fl)
				print ("{:<14} {:<13} {:<10}".format(dt['id'],dt['name'] , dt['goals']))
			except EOFError:
				break
				fl.close()
	if ch==3:
		flag=False
		fl=open('football.dat','rb')
		checkid=int(input('Enter id number to be searched'))
		while True:
			try:
				rec=p.load(fl)
				if checkid==rec['id']:
					print('Record found')
					print('name = ',rec['name'])
					print('goals = ',rec['goals'])
					flag=True
			except EOFError:
				break
		if flag==False:
				print('Record not found')
				fl.close()
	if ch==4:
		import time as t
		flag=False
		lst=[]
		fl=open('football.dat','rb')
		checkroll=int(input('Enter id number to be deleted '))
		while True:
			try:
				rec=p.load(fl)
				if checkroll==rec['id']:
					print('Record found')
					print('Name = ',rec['name'])
					print('goals = ',rec['goals'])
					print('Deleting.......')
					t.sleep(5)
					print('Done')
					flag=True
				else:
					lst.append(rec)
			except EOFError:
				break
		fl.close()
		if flag==False:
			print('Record not found')
		else:
			fl=open('football.dat','wb')
			for l in lst:
				p.dump(l,fl)
		fl.close()
	if ch==5:
		flag=False
		reclist=[]
		fl=open('football.dat','rb')
		checkid=int(input('Enter id number to be updated '))
		while True:
			try:
				rec=p.load(fl)
				reclist.append(rec)
			except EOFError:
				break
		fl.close()
		for i in reclist:
			if i['id']==checkid:
				print('Record found')
				print('Name = ',rec['name'])
				print('Marks = ',rec['goals'])
				newname=input('Enter new name to be updated')
				newgoals=int(input('Enter new goals to be updated'))
				i['name']=newname
				i['goals']=newgoals
		print('Updating.......')
		import time as t
		t.sleep(3)
		print('Done')
		fl=open('football.dat','wb')
		for l in reclist:
			p.dump(l,fl)
		fl.close()
	if ch==6:
		break
	 
			
			
			
			
				
		
				

			
 
		    
		    
    
     	
              

		

	
	