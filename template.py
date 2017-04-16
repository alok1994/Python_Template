from string import Template

def Main():
    cart = []
    cart.append(dict(item='cake',price=2,qty=1))
    cart.append(dict(item='Tea',price=10,qty=2))
    cart.append(dict(item='fish',price=32,qty=12))

    t = Template('$qty X $item = $price')
    total = 0
    print 'Cart'
    for data in cart :
        print t.substitute(data)
        total += data['price']
    print "Total=" +str(total)

if __name__ == '__main__':
                Main()
    

    
