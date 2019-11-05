import os
import sys

class decimal_to_binary():

	def converter_decimal_to_binary(self,decimal):

		decimal_binary=decimal
		print ("\n#################################")
		print("DECIMAL TO BINARY: ",end="")
		return bin(decimal_binary)[2::] 
	
class binary_to_decimal():

	def converter_binary_to_decimal(self,binary):

		binary_to_decimal = binary
		decimal = 0

		for digit in binary:
			if digit == "0" or digit == "1": 
				decimal = decimal*2 + int(digit) 

			else:
				print("#################################")
				return "INVALID"
				break

		print ("\n#################################")
		print ("BINARY TO DECIMAL: ",end="")
		return decimal
		
class text_to_binary():

    def text_binary(self,text):

        mEncrytp = ''
        for letra in text :
            final = self.d_binary(ord(letra))
            mEncrytp = mEncrytp + str(final) + " "
        print("\n#################################")
        print("Text to BINARY: ",end="")
        return mEncrytp
 	
    def d_binary(self,digit):

        result = ''
        var = digit
        temp = 0
        i = 0
        while i < 8 :
            temp = var % 2 
            result = result + str(temp)
            if var==digit :
               var = digit//2
            else :
                var = var//2 #
            i = i + 1
       
        return result[::-1]

class binary_to_text() :

    def binary_text(self,binary):
        list_b = binary.split() 
        result = ''
        for i in range (len(list_b)) :
            result = result + chr(self.binary_d(int(list_b[i])))
        print("\n#################################")
        print("BINARY to Text: ",end="")
        return result
 
    def binary_d(self,binary):
        digit = 0
        i = 0
        for iterator in (str(binary)[::-1]) :

            if(int(iterator) == 1):

                digit = digit + 2 ** i

            i = i + 1
        return digit
  
d_b = decimal_to_binary()
b_d = binary_to_decimal()
t_b = text_to_binary()
b_t = binary_to_text()

#start Input
def menu():
	#start menu function
	print("##########")
	print("---Menu---\n")
	print("1) Decimal Number to Binary")
	print("2) Binary to Decimal Number")
	print("3) Text to Binary")
	print("4) Binary to Text")
	print("5)-Clear-")
	print("6)-Exit-\n")
	print("---Menu---")
	print("##########")
	try:
		opc =int(input("\nchoose a option: "))
		
		while 0<opc<7:

			if opc == 1:
				print("\nchose converter decimal to binary")
				print(d_b.converter_decimal_to_binary(int(input("\nenter the decimal number you want to convert: "))))
				print("#################################")
				opc = int(input("\nchoose a option again please: "))
			elif opc == 2:
				print("\nchose converter binary to decimal")
				print(b_d.converter_binary_to_decimal(input("\nenter the decimal number you want to convert: ")))
				print("#################################")
				opc = int(input("\nchoose a option again please: "))
			elif opc == 3:
				print("\nchose converter binary to decimal")
				print(t_b.text_binary(input("\nenter the binary you want to convert: ")))
				print("#################################")
				opc = int(input("\nchoose a option again please: "))
			elif opc == 4:
				print("\nchose converter binary to decimal")
				print(b_t.binary_text(input("\nenter the text you want to convert: ")))
				print("#################################")
				opc = int(input("\nchoose a option again please: "))
			elif opc == 5:
			 	os.system('cls')
			 	#os.system('clear') for linux
			 	menu()
			elif opc == 6:
				sys.exit()

		else:
			print("\n¡Invalid option!")
	except:

		return "EXIT"

menu()


