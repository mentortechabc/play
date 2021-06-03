import sys

#print(sys.argv[1] + " " + "10:00-11:00 CEST")
#print(sys.argv[1] + " " + "11:00-12:00 CEST")
#print(sys.argv[1] + " " + "12:00-13:00 CEST")
#print(sys.argv[1] + " " + "13:00-14:00 CEST")
#print(sys.argv[1] + " " + "14:00-15:00 CEST")

data = """
    {input_data} 10:00-11:00 CEST
    {input_data} 11:00-12:00 CEST
    {input_data} 12:00-13:00 CEST
    {input_data} 13:00-14:00 CEST
    {input_data} 14:00-15:00 CEST
""".format(input_data = sys.argv[1])
print(data)
