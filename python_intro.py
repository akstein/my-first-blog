print("Hello, Django girls!")
if 3 > 2:
	print("It works!")
if 5 > 2:
	print("5 is indeed greater than 2")
else:
	print("5 is not greater than 2")
name = "Adriana"
if name == "Jack":
	print("Hey Jack!")
elif name == "Adriana":
	print("Hey Adriana!")
else:
	print("Hey anonymous!")
volume = 87
if volume < 20:
	print("It is kind of quiet")
elif 20 <=volume < 40:
	print("It is nice for background music")
elif 40 <=volume < 60:
	print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
	print("Nice for parties")
elif 80 <= volume < 100:
	print("A bit loud!")
else:
	print("My ears are hurting! :(")
#Change the volume if it is too loud or too quiet
if volume < 20 or volume > 80:
	volume = 50
	print("That is better!")
def hi():
	print("Hi there!")
	print("How are you?")

hi()
def hi(name):
	if name == "Adriana":
		print("Hi Adriana")
	elif name == "Jack":
		print("Hi Jack")
	else:
		print("Hi anonymous!")

hi("Elsa")

def hi(name):
	print("Hi " + name + "!")

girls = ["Rachel", "Monica", "Phoebe", "Adriana", "You"]
for name in girls:
	hi(name)
	print("Next girl")
for i in range(1, 6):
	print(i)


