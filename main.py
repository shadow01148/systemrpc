from pypresence import Presence
import time
import psutil

def rpc():
    if psutil.sensors_battery().percent is not None: 
        battery = psutil.sensors_battery().percent 

    RPC = Presence(123) # int
    if RPC is None:
        print("No Client ID provided. Look here:\n\nhttps://support-dev.discord.com/hc/en-us/articles/360028717192-Where-can-I-find-my-Application-Team-Server-ID-")
        return
    
    RPC.connect()
    while True:  
        cpu = round(psutil.cpu_percent(),1)
        mem = round(psutil.virtual_memory().percent,1)
        RPC.update(
            state=F"CPU: {str(cpu)}%, RAM: {str(mem)}%", 
            details=f"CPU Cores: {psutil.cpu_count()}, Battery percent: {battery}%", # to be fixed
            large_image="image_asset",
            small_image="small_image_asset", 
            large_text="RPC", # Text when hovering over large_image
            buttons=[{"label": "pypresence", "url": "https://github.com/qwertyquerty/pypresence"}]) # Maximum of 2 buttons   
        time.sleep(5) # you can remove this to go awol

rpc()
