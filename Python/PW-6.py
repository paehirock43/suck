from Shoe import Shoes
repeat = "Y"
while repeat.upper()=="Y":
    id=input("Enter Id: ")
    while True:
        brand=input("Enter Brand[1=Puma, 2=Reebok, 3=Converse,4=Adidas,5=Nike]: ")
        if brand == '1' or brand == '2' or brand == '3' or brand == '4' or brand == '5':
            break
        else:
            print("Invalid Data Please Try Again")
    while brand=='1':
        model=input("Enter Model[1=Batman Suede, 2=Basket Classic, 3=Pokemon Rider,4=Minecraft]: ")
        if model == '1' or model == '2' or model == '3' or model == '4':
            break
        else:
            print("Invalid Data Please Try Again")
            continue
    while brand=='2':
        model=input("Enter Model[1=Turbo Restyle, 2=Zig Kinetica, 3=GL 1000,4=Flexagon Force]: ")
        if model == '1' or model == '2' or model == '3' or model == '4':
            break
        else:
            print("Invalid Data Please Try Again")
            continue
    while brand=='3':
        model=input("Enter Model[1=Chuck Taylo All Star, 2=Jack Purcell, 3=Star Life Clean,4=Point Star,5=Star in Black Youth]: ")
        if model == '1' or model == '2' or model == '3' or model == '4' or model == '5':
            break
        else:
            print("Invalid Data Please Try Again")
            continue
    while brand=='4':
        model=input("Enter Model[1=Neo, 2=Stan Smith Lux, 3=Forum Low,4=Run Falcon]: ")
        if model == '1' or model == '2' or model == '3' or model == '4':
            break
        else:
            print("Invalid Data Please Try Again")
            continue
    while brand=='5':
        model=input("Enter Model[1=Air Force, 2=Air Max, 3=Retro GTS,4=Free Run]: ")
        if model == '1' or model == '2' or model == '3' or model == '4' :
            break
        else:
            print("Invalid Data Please Try Again")
            continue
    result=Shoes(id,brand,model)
    print("Id: ",result.getId())
    print("Brand: ",result.getBrand())
    print("Model: ",result.getModel())
    print("Price: ",result.getPrice())
    print("Discount: ",result.getDiscount())
    print("Net: ",result.getNet())
    repeat = input("Do you want to continue? (Y/N): ")

