#import pyfiglet module 
import pyfiglet 
  
result = pyfiglet.figlet_format("Coded by miles")
print(result)
from pafy import new 
url = input("enter your video link here: ")
video = new(url)
mlzdl = video.getbest()
mlzdl.download()
#
#
#
#
print("the video successfully downloaded")
