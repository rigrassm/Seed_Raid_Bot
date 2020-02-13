# Seed_Raid_Bot
 A useful python script which softresets Pokémon SwSh Raids. It will read Den Seed from Switch RAM and search the spread you're looking for!
 
# Warning
 I won't be liable if your Switch get damaged or banned. Use at your own risk.
 
 # Features
* Sofreset for a good Den Seed (perfect IVs, shiny at low frame, etc.)
* Softreset for event raids
* Softreset for rare beam raids
 
# Requirements
* CFW
* Internet Connection
* sys-botbase(https://github.com/olliz0r/sys-botbase)
* ldn_mitm(https://github.com/spacemeowx2/ldn_mitm)

# Usage
To check Den id, use CaptureSight
1) Install the latest release of [Python](https://www.python.org/downloads/)
2) Connect your Switch to Interet
3) Start sys-botbase and ldn_mitm
4) Go to System Settings, check your Switch IP and write it in the script
5) Set game text speed to normal
6) Save in front of an empty Den (get its watts before saving if they're avaiable). You must have at least one Wishing Piece in your bag
7) Modify script filters research according to what is written below
8) Start the script with game closed and selection square over it

# Always Remember!
Sometimes button inputs of your joycons won't work. This because the fake controller isn't detached from your Switch. 
So, everytime you want to stop the bot, always press CTRL+C and follow the instructions. The bot will detach the fake controller and buttons will work correctly. 

# Research Filters (Need to be edited!)
* r.ShinyType == 'None'/'Star'/'Square' (!= 'None' for both square/star)
* r.Nature == 'NATURE'
* r.Ability == 1/2/'H'
* r.IVs == spread_name (spread_name = [x,x,x,x,x,x])

# Credits:
* spacemeowx2 for his livesafer sys-module. It avoids Switch to disconnect from wifi once game is opened
* olliz0r for his amazing sys-module
* wwwwwwzx for [G8RNG](https://github.com/wwwwwwzx/raidtool) code
* Admiral-Fish for cleaning G8RNG code
* zaksabeast for [CaptureSight](https://github.com/zaksabeast/CaptureSight/) (all addresses/checks are taken from there)
