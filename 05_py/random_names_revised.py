# Justin Zou, Mark Zhu, Han Zhang (Team MJH)
# SoftDev
# K05 -- Python Random Name Generator
# 2021-09-26

import random

pd1 = ["Owen Yaggy", "Haotian Gan", "Ishraq Mahid","Ivan Lam","Michelle Lo"
        "Christopher Liu","Ivan Mijacika","Lucas Lee","Josephine Lee","Rayat Roy",
        "Emma Buller","William Chen","Rachel Xiao","Andrew Juang","Yuqing Wu"
        "Renggeng Zheng","Annabel Zhang","Alejandro Alonso","Deven Maheshwari",
        "Oscar Wang","Tami Takada","Yusuf Elsharawy","Ella Krechmer","Tomas Acuna",
        "Tina Nguyen","Theo Fahey","Sadid Ethun"]

pd2 = ["Patrick Ging","Wenhao Dong","Raymond Yeung","Kevin Cao","Michael Borczuk",
        "Alif Abdullah","Justin Zou","Andy Lin","Shadman Rakib","David Chong",
        "Daniel Sooknanan","Cameron Nelson","Austin Ngan","Yaying Liang Li"
        ,"Eric Guo","Noakai Aronesty","Roshani Shrestha","Yoonah Chang",
        "Qina Liu","Han Zhang","Joshua Kloepfer"]

def getName():
    if random.randint(0,1)==0:
        print(random.choice(pd1))
    else:
        print(random.choice(pd2))