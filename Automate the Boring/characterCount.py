import pprint
message = 'With Nagatos death, Tobi, disguised as Madara Uchiha (one of Konohas founding fathers), announces that he wants to capture all nine Tailed Beasts to cast an illusion powerful enough to control all humanity and achieve world peace. The leaders of the five ninja villages refuse to help him and instead join forces to confront his faction and allies. That decision results in a Fourth Shinobi World War between the combined armies of the Five Great Countries (known as the Allied Shinobi Forces) and Akatsukis forces of zombie-like ninjas. The Five Kage try to keep Naruto, unaware of the war, in a secret island turtle near Kumogakure (Hidden Cloud Village), but Naruto finds out and escapes from the island with Killer Bee, the host of the Eight-Tails. At that time, Naruto—along with the help of Killer Bee—gains control of his Tailed Beast and the two of them head for the battlefield.'
count = {}

for character in message: 
    count.setdefault(character, 0) 
    count[character] = count[character] + 1
    
pprint.pprint(count)