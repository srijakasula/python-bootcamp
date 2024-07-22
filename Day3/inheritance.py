#INHERETENCE

class mobile:
    def power_button():
        print("power button is used for on/off")
    def call_operation():
        print("it is used for calling") 
    def text_operation():
        print("it is used for texting")       
class iphone(mobile):
    def air_drop():
        print("sending doc,pics")
mobj=iphone
mobj.call_operation()
      
