# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "18196402"))
    API_HASH = getenv("API_HASH", "a184b91d39fc85265e232e7c323fac45")
    BOT_TOKEN = getenv("BOT_TOKEN","0")
    FSUB = getenv("FSUB", "Adult_Unity")
    CHID = int(getenv("CHID", "-1001942609289"))
    SUDO = list(map(int, getenv("SUDO", "5911422304").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://naibansari987:Yuuichi@cluster0.wp2wkfb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
