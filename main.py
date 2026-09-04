from pyscript import document, display
display(target="div1")

name = "Name: Francis Ezekiel Fernandez"#string

display(name, target="div2")

age = "Age: 14"#integer

display(age, target="div3")

height14 = "Height: 157.48 cm"#float

display(height14, target="div4")

countries_list = ["Japan", "Malaysia", "Germany", "Korea"]#list

display(countries_list, target="div5")

student_type = "false"#boolean

display(student_type, target="div6")

aboutme ={
        "Favorite Color": "Purple",
        "Car Brand": "Honda",
        "Shoe Size": "8.5 US Mens",
        "Best Friend": "Ary" ,
}#dict

display(aboutme, target="div7")

fav_fruits = set(['Bananas','Avocados','Kiwis','Dragonfruit','Apples']) #set

display(fav_fruits, target="div8")

days_of_the_week = tuple(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) #tuple

display(days_of_the_week, target="div9")