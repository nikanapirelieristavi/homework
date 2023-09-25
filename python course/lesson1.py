from turtle import*
#vaketebt saxls
#tavidan vaketebt kvadrats
#funqcia "forward" it shegvidzlia horizontaluri xazi davxazot da frchxilebshi ra ufro didi ricxvia mit ufro didi xazi gamodis
#funqcia "left" it vwert frcxhilebshi im ricxvs ramdeni gradusitac gvinda rom miemartos is xazi

width(7)
begin_fill()
color("red")

forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)

forward(40)
left(90)

end_fill()

color("brown")

begin_fill()
forward(35)
right(90)
forward(20)
right(90)
forward(35)

end_fill()
penup()
goto(100, 100)

color("purple")

begin_fill()
right(135)
pendown()
forward(70)
left(90)
forward(70)
left(135)
forward(100)

end_fill()
penup()

goto(15, 50)

pendown()

width(4)
color("black")

begin_fill()

forward(20)
left(90)

forward(35)
left(90)

forward(20)
left(90)
forward(35)

color("cyan")

end_fill()

penup()

goto(85, 50)

pendown()

color("black")

begin_fill()

left(180)

forward(35)
left(90)

forward(20)
left(90)

forward(35)
left(90)

forward(20)

color("cyan")
end_fill()

penup()

exitonclick()



print("hello world")


#pliusi ar iwereba  brwyalebshi

#es aris komentari

#int-integer it aginishneba ricxvi

#xstr-string it aginishneba brwyalebshi moqceuli nebismieri ram da mat ewodebtad simboloebi

#strings sheudzlebelia miematos integeri

print(" nika aris " + "15" + " wlis")

print(5 + int("5"))