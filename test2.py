import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('spam')
class veichle:

    def veichle_name(self):
        logger.info('Class1: doing something')
        name=input("enter name of veichle")
        return name
    def veichle_no(self):
         vno=input("enter veichle no")
         return vno

bike=veichle()
num=veichle()

print(bike.veichle_name())
print("veichle no is " ,num.veichle_no())

print("the new updated model of same bike is",bike.veichle_name())