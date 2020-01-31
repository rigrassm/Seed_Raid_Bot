#Start the bot with closed game and selection square over it
#Den Seed address: "peek 0xaddress 8" (address = 0x4298FAA0 + (0xden_id - 1) * 0x18))
#Event flag byte address = "peek 0xaddress 8" (address = (0x4298FAAB + (den_id - 1) * 0x18)) + 0xB)
#isEvent == 0/1 (search event raid seeds only)
#r.Ability == '1'/'2'/'H'
#r.Nature == 'NATURE'
#r.ShinyType = 'None'/'Star'/'Square'
#r.IVs == spread_name

from G8RNG import XOROSHIRO,Raid
import socket
import time
import binascii

def sendCommand(s, content):
    content += '\r\n' #important for the parser on the switch side
    s.sendall(content.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.7", 6000))

reset = 0
ivfilter = 1 #set 0 to disable filter
Maxresults = 5000
isEvent = 0
#add the spreads you need
V6 = [31,31,31,31,31,31]
A0 = [31,0,31,31,31,31]
S0 = [31,31,31,31,31,0]
S1 = [31,31,31,31,31,1]
S2 = [31,31,31,31,31,2]
S3 = [31,31,31,31,31,3]
S4 = [31,31,31,31,31,4]
S5 = [31,31,31,31,31,5]

time.sleep(2)
while True:
    sendCommand(s, "click A") #A on game
    print("A in game")
    time.sleep(0.2)
    sendCommand(s, "click A")
    time.sleep(1.5)
    sendCommand(s, "click A") #A on profile
    print("A in profile")
    time.sleep(0.2)
    sendCommand(s, "click A")
    time.sleep(16.5) 
    sendCommand(s, "click A") #A to skip anim
    print("skip anim")
    time.sleep(1)
    sendCommand(s, "click A")
    time.sleep(1)
    sendCommand(s, "click A")
    time.sleep(8)
    sendCommand(s, "click A") #A in den
    print("A in den")
    time.sleep(1)
    sendCommand(s, "click A")
    time.sleep(2.5)
    sendCommand(s, "click A") #A to throw piece
    print("throw piece in den")
    time.sleep(1.8)
    sendCommand(s, "click A") #A to save
    print("saving")
    time.sleep(1)
    sendCommand(s, "click HOME") #Home
    print("HOME clicked")
    time.sleep(2)
    
    sendCommand(s, "peek 0x4298fb9B 1") #event byte
    time.sleep(0.5)
    eventbyte = s.recv(3)
    #print(binascii.unhexlify(eventbyte[0:-1]))
    
    flag = int.from_bytes(binascii.unhexlify(eventbyte[0:-1]), "big") #flag event
    flag = (flag >> 1) & 1

    if flag:
        isEvent = 1
        print("Event")
    else:
        isEvent = 0
        print("No event")
    
    sendCommand(s, "peek 0x4298fb90 8") #get reversed seed from ram
    time.sleep(0.5)
    re_seed = s.recv(17)
    re_seed = (binascii.unhexlify(re_seed[0:-1])).hex()
    #print(re_seed)
    seed = int.from_bytes(binascii.unhexlify(re_seed), "little") #reverse the seed
    print("Seed", hex(seed))

    #spread searh
    j = 0
    found = 0
    while j < Maxresults: #and isEvent == 1:
        r = Raid(seed, flawlessiv = 5, HA = 1, RandomGender = 1)
        seed = XOROSHIRO(seed).next()
        if ivfilter:
            if r.ShinyType != 'None' and r.Ability == 1 and r.Nature == 'RELAXED': #and (r.IVs == S0 or r.IVs == S1 or r.IVs == S2
                                                                                         #or r.IVs == S3 or r.IVs == S4 or r.IVs == S5):
                print(j)
                r.print()
                found = 1
        else:
            r.print()
        j += 1

    if found:
        break
    else:
        reset = reset + 1
        print("Nothing found - resets:", reset)
        
    '''a = input('Continue? ')
    if a != "y":
        break'''

    time.sleep(0.5)
    sendCommand(s, "click X")
    time.sleep(2)
    sendCommand(s, "click A")
    time.sleep(3.5)