# get fake incubator data
from faker import Faker
from time import sleep
import random
import sqlite3
import os

'''
- heading format
  - Name, Contact, BirdType, NumberOfEggs, PricePerEgg($), TotalPrice($), DateAdded, HatchRate(%)

- price of each bird per egg
  - broiler $0.20
  - road runner $0.10
  - duck $0.50
  - geniue fowl $0.30
  - turkey $0.40
'''

# point to file location
os.chdir("/home/donald/Projects/Python36/Export to Excel")

# create faker obj
f = Faker()

# create db obj
print("[INFO] Connecting to database..")
db = sqlite3.connect("incubator.db")
cur = db.cursor()
print("[INFO] Connected to database. Ready!")
sleep(2)

def save_to_db(n, c, bt, noe, ppe, tp, da, hr):
    
    cur.execute("""INSERT INTO hatch(Name, Contact, BirdType, NumberOfEggs, PricePerEgg, TotalPrice, DateAdded, HatchRate) VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", (n, c, bt, noe, ppe, tp, da, hr))
    db.commit()
    print("[INFO] Data successfully saved to database")
        
def create_data():
    print("[INFO] Generating data..")
    
    bird_type = ["broiler", "road runner", "duck", "turkey", "geniue fowl"]
    broiler_p = 0.20
    runner_p = 0.10
    duck_p = 0.50
    fowl_p = 0.30
    turkey_p = 0.40
    
    name = f.name()
    phone = f.phone_number()
    added = str(f.date_this_year())
    eggs = random.randrange(9, 500)
    rate = random.randint(50, 90) + round(random.expovariate(0.5), 1)
    birdType = random.choice(bird_type)
    
    if birdType == "broiler":
        ppe = broiler_p
        tp = eggs * ppe
        
    elif birdType == "road runner":
        ppe = runner_p
        tp = eggs * ppe      
    
    elif birdType == "duck":
        ppe = duck_p
        tp = eggs * ppe 
        tp = round(tp, 2)
        
    elif birdType == "turkey":
        ppe = turkey_p
        tp = eggs * ppe   
        tp = round(tp, 2)
    
    elif birdType == "geniue fowl":
        ppe = fowl_p
        tp = eggs * ppe 
        tp = round(tp, 2)
    
    print("[INFO] Saving to database")
    save_to_db(name, phone, birdType, eggs, ppe, tp, added, rate)
    #data = (name, phone, birdType, eggs, ppe, tp, added, rate)
    #print("[INFO] Data: ", data)
    sleep(1)

# number of simuated data allowed
entries = 40
now_at = 0

while now_at < entries:
    print("[INFO] #%d Saving data entry" %now_at)
    create_data()
    now_at += 1
    sleep(5)
    
print("[INFO] Closing database connection..")
db.close()
print("[INFO] Done with incubator simulated data!")