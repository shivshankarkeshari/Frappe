import json
a=open("./sample_data.json", "r").read()
a=json.loads(a)
import time


def movment(fromloc, toloc, pdt, qty):
	#if we know from where to where we have to move product
	if fromloc!="" and toloc!="":
		check=False
		for i in a:
			if a[i]["name"]==fromloc:
				check= True 
				if pdt in a[i]:
					if a[i][pdt]>=qty:
						a[i][pdt]=a[i][pdt]-qty
						s=False
						for j in a:
							if a[j]["name"]==toloc:
								if pdt in a[j]:
									a[j][pdt]=a[j][pdt]+qty
									print("Product has been moved")
									break
								else:
									a[j][pdt]=qty
									print("Product has been moved")
								s=True
						if s==False:
							a["loc{}".format(len(a)+1)]={"name": toloc, pdt: qty}
							print("Products has been moved into new location: " + toloc)
						break
					elif a[i][pdt]<=qty:
						print("Demands of {} are higher than present in {}".format(pdt, fromloc))
				else:
					print("Product not present at Origin location")
				break
		if check==False:
			print("Origin location doesn't exist")

	#If you want to move things out
	elif fromloc!="" and toloc=="":
		for i in a:
			if a[i]["name"]==fromloc:
				if a[i][pdt]>=qty:
					a[i][pdt]=a[i][pdt]-qty
				else:
					print("{} are in less amount than delevery quantity".format(pdt))
				break


	# If you want to move things into a location
	elif fromloc=="" and toloc!="":
		s=False
		for i in a:
			if a[i]["name"]==toloc:
				if pdt in a[i]:
					a[i][pdt]=a[i][pdt]+qty
				else:
					a[i][pdt]=qty
				s=True
				break


		if s==False:
			a["loc{}".format(len(a)+1)]={"name": toloc, pdt: qty}

	else:
		print("syntex error")





class Menu:

	def add_product(self):
		loci = input('Enter location name: ')
		product_name = input('Enter product name: ')
		product_quantity = int(input('Enter product quantity: '))
		movment("", loci, product_name, product_quantity)
		# print('Sucessfully added')

	def moving_pdt(self):
		fromloc = input('Enter From location: ')
		toloc = input('Enter location where to move: ')
		product_name = input('Enter product name: ')
		product_quantity = int(input('Enter product quantity: '))
		movment(fromloc, toloc, product_name, product_quantity)

	def mov_things_out(self):
		fromloc=input("Enter location: ")
		product_name = input('Enter product name: ')
		product_quantity = int(input('Enter product quantity: '))
		movment(fromloc, "", product_name, product_quantity)

	def add_loc_product(self):
		loci = input('Enter location name: ')
		for i in a:
			if a[i]["name"]==loci:
				print(a[i])
				break
		product_name = input('Enter product name: ')
		product_quantity = int(input('Enter product quantity: '))
		movment("", loci, product_name, product_quantity)
		# print('Sucessfully added')
	def show_all_products(self):
		loci = input('Enter location name: ')
		for i in a:
			if a[i]["name"]==loci:
				print(a[i])
				break

	def list_product_location(self):
		pdt= input('Enter product name: ')
		loci=[]
		for i in a:
			if pdt in a[i]:
				loci.append(a[i]["name"])
		print(*loci, sep = ", ")

	def see_all_data(self):
		print(a)

	def save_all_activity(self):
		with open("./sample_data.json", "w") as f:
			json.dump(a, f)
		Print("saved your all activity")





	




	def display(self):
		print('''
			Welcome to Product Manager
			============================
			     Enter    Function
			     -----    --------    
			     1 -------- Add new Product
			     2 -------- Move any product from one location to other
			     3 -------- Move out any Product from any specific location
			     4 -------- Increase existing product quantity
			     5 -------- See all Products at any Location
			     6 -------- See list of all location where any specific Product exist
			     7 -------- Display option
			     8 -------- Save all transaction  
			     9 -------- Close Program
			     10 ------- see all Location stats

			''')

	def run(self):

		
		self.display()

		while True:
			try:

				choice = int(input('Enter your choice: '))
				if choice == 1:
					self.add_product()
				elif choice == 2:
					self.moving_pdt()
				elif choice == 3:
					self.mov_things_out()
				elif choice == 4:
					self.add_loc_product()
				elif choice == 5:
					self.show_all_products()
				elif choice == 6:
					self.list_product_location()
				elif choice == 7:
					self.display()
				elif choice == 8:
					self.save_all_activity()
				elif choice == 9:
					print("Thanks for using this service")
					time.sleep(2)
					print("Ok Bye, Have a nice day :)")
					time.sleep(1)
					break
				elif choice == 10:
					self.see_all_data()
			except Exception as e:
				print('Please you must enter a right choice')

if __name__ == '__main__':
	Menu().run()

