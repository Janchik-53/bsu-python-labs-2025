# Напишите программу, которая проверяет, является ли строка анаграммой другой строки.
def main() :
   str1 = 'listen'
   str2 = 'SILEnT'
   if sorted(str1.lower()) == sorted(str2.lower()) :
      print("Анаграмма")

   else :
      print("Не анаграмма")

main()
    
    

