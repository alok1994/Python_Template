from string import Template

class MyTemplate(Template):
    delimiter = '#'
    
def Main():
        cart = []
        cart.append(dict(item='Cake', price = 10, qty = 2))
        cart.append(dict(item='Coke', price = 2, qty = 1))
        cart.append(dict(item='Fish', price = 32, qty = 3))

        t = MyTemplate('#qty X #item = #price ')
        total = 0
        print 'Cart:'
        for data in cart:
            print t.substitute(data)
            total += data['price']
        print 'Toatal', str(total)

if __name__ == '__main__':
    Main()
