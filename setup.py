import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install aiohttp")
    os.system("pip install asyncio")
    os.system("pip install aiohttp_socks")
    os.system("pip install colorama")
    os.system("pip install numpy")
elif c == "1":
    os.system("pip3 install aiohttp")
    os.system("pip3 install asyncio")
    os.system("pip3 install aiohttp_socks")
    os.system("pip3 install colorama")
    os.system("pip3 install numpy")
   
print("Done.")
