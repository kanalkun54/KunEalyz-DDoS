import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install aiohttp")
    os.system("pip install asyncio")
    os.system("pip install colorama")
    os.system("pip install requests")
elif c == "1":
    os.system("pip3 install aiohttp")
    os.system("pip3 install asyncio")
    os.system("pip3 install requests")
    os.system("pip3 install colorama")
   
print("Done.")
