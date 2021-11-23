import os

def check_files(request):
   initial_dir = os.listdir("./")
   second_dir = os.listdir("./files")
   
   initial_dir = ' / '.join(initial_dir)
   second_dir = ' / '.join(second_dir)
   
   return f'{initial_dir} - {second_dir}'
