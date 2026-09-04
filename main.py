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

fav_fruits = set(["Bananas","Avocados","Kiwis","Dragonfruit","Apples"]) #set

display(fav_fruits, target="div8")

days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #tuple

display(days_of_the_week, target="div9")

def adding_numbers(e):
    document.getElementById("output1").innerHTML = ""     # clears previous output
    num1 = float(document.getElementById('input1').value) # get 1st output
    num2 = float(document.getElementById('input2').value) # get 2nd output
    result_add = num1 + num2                                  # use operator to compute
    display(result_add, target = "output1")                   # display output in div

def subtracting_numbers(e):
    document.getElementById("output2").innerHTML = ""     # clears previous output
    num1 = float(document.getElementById('input1').value) # get 1st output
    num2 = float(document.getElementById('input2').value) # get 2nd output
    result_subtract = num1 - num2                         # use operator to compute
    display(result_subtract, target = "output2")          # display output in div

