def menu():
	Food_Items = ['Rice', 'Paneer','Daa_Makhni','klkl','ggdd','djkdjk']
	Price = [150,180,220,100,120]
	for i in range(len(Food_Items)):

		if i < len(Price):

		    print(Food_Items[i],Price[i])

		else:
			print(Food_Items[i],"no Price")    
		
		
menu()