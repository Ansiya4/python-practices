class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def pri(self):
        print(self.msg)

try:
    t=str(input('Enter'))
    Accident(t)
    if t=='crash':
        raise Accident('CRAAAAASH')
except Accident as error:
    error.pri()
else:
    A=Accident(t)
    A.pri()
