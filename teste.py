import usb.core

dev = usb.core.find(find_all=True)

for b in dev:
    print b.idProduct
