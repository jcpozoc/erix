file=open("devices.txt","a")

while True:
    newItem = input("Enter a new device: ")
    if newItem == 'exit':
        print ("All Done")
        break
    else:
        file.write(newItem + "\n")
file.close()