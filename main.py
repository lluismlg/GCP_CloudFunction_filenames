import os

def checkFiles(request):
   initial_dir = os.listdir("./")
   second_dir = os.listdir("./files/sites/default/files/special_topics/cn/")
   
   initial_dir = ' / '.join(initial_dir)
   second_dir = ' / '.join(second_dir)
   
   result = ' /n '.join(second_dir)
   
   return result
