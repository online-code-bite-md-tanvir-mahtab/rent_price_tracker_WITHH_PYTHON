from traceback import print_exception
from get_info_price import HomePrice
from fill_the_form import FormFill



def hendle_the_call(link,price,add):
    for i in range(len(price)):
        # creating the instance of the class
        file = FormFill()
        file.find_the_form_fill(add[i],price[i],link[i])
        print("filling is completed")



if __name__ == '__main__':
    data = HomePrice()
    link = data.get_the_link_data()
    # print(link)
    price = data.get_the_price_data()
    # print(price)
    add = data.get_the_address()
    # print(add)
    hendle_the_call(link,price,add)



