
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *
engine = create_engine('sqlite:///Games.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
session.query(Category).delete()
session.query(Game).delete()
session.query(User).delete()

# create a dummy user

User1 = User(name="Nehad Alnahari", email="nauniversity22@gmail.com",
             picture="""https://cdn0.iconfinder.com/data/icons/urban-avatar-flat/128/01_woman_girl_avatar_user_people_profession_contact-512.png""")
session.add(User1)
session.commit()

# "Action" category
category1 = Category(name="Action", user_id = 1)

session.add(category1)
session.commit()


# "Platform" category
category2 = Category(name="Platform", user_id = 1)

session.add(category2)
session.commit()

# "Action Adventure" category
category3 = Category(name="Action Adventure", user_id = 1)

session.add(category3)
session.commit()

# "Open world" category
category4 = Category(name="Open world", user_id = 1)
session.add(category4)
session.commit()

# "RPG" category
category5 = Category(name="RPG", user_id = 1)
session.add(category5)
session.commit()

# "Fantasy" category
category6 = Category(name="Fantasy", user_id = 1)
session.add(category6)
session.commit()

# "Fighting" category
category7 = Category(name="Fighting", user_id = 1)
session.add(category7)
session.commit()

# "Sport" category
category8 = Category(name="Sport", user_id = 1)
session.add(category8)
session.commit()

# "Shooting" category
category9 = Category(name="Shooting", user_id = 1)
session.add(category9)
session.commit()

# "Horror" category
category10 = Category(name="Horror", user_id = 1)
session.add(category10)
session.commit()

game1 = Game(
    name =   "Mortal Kombat X"  ,
    description = """Mortal Kombat X  s gameplay consists of two players, or one player and the CPU, fighting against each other with their selected character, using a large, varied array of character specific attacks. 
                 The game contains several modes, such as a story mode, which takes place twenty five years after the previous Mortal Kombat game, several   Tower   modes, which feature dynamically changing challenges, numerous online modes, and the   Krypt  , a mode played in a first person perspective where players explore the areas unlocking a variety of in game items.""",
    picture = """https://en.wikipedia.org/wiki/Mortal_Kombat_X#/media/File:Mortal_Kombat_X_Cover_Art.png""",
    platform = """iOS
                Microsoft Windows
                PlayStation 4
                Xbox One
                Android""",
    developer = "NetherRealm Studios"  ,
    publisher =   "Warner Bros. Interactive Entertainment"  ,
    producer = """Hans P. Lo 
                               Adam Urba""",
    director = "Ed Boon" ,
    category = category1,
    user_id = 1
    )
session.add(game1)
session.commit()

game2 = Game(
    name =   "Shadow of the Tomb Raider"  ,
    description = """Set shortly after the events of Rise of the Tomb Raider, its story follows Lara Croft as she ventures through Mesoamerica and South America to the legendary city Paititi, battling the paramilitary organization Trinity and racing to stop a Mayan apocalypse she has unleashed. 
                     Lara must traverse the environment and combat enemies with firearms and stealth as she explores semi open hubs. 
                     In these hubs she can raid challenge tombs to unlock new rewards, complete side missions, and scavenge for resources which can be used to craft useful materials.""",
    picture = """https://upload.wikimedia.org/wikipedia/en/1/11/Shadow_of_the_Tomb_Raider_cover.png""",
    platform = """Microsoft Windows
                  PlayStation 4
                  Xbox One
                  macOS
                  Linux""",
    developer = "Eidos Montreal",
    publisher = "Square Enix"  ,
    producer = """Mario Chabtini
                  Fleur Marty""",
    director = "Daniel Chayer"  ,
    category = category1,
    user_id = 1
    )
session.add(game2)
session.commit()

game3 = Game(
    name =   "Rayman Legends"  ,
    description = """The game carries on the style of gameplay from Rayman Origins in which up to four players (depending on the format) simultaneously make their way through various levels. 
                     Lums can be collected by touching them, defeating enemies, or freeing captured Teensies. 
                     Collecting Teensies unlocks new worlds, which can be played in any order once they are available. 
                     Along with Rayman, Globox, and the Teensies returning as playable characters, players can now control new female character Barbara and her sisters, once they are rescued from certain stages.""",
    picture = """https://ubistatic19 a.akamaihd.net/ubicomstatic/en us/global/game info/rl_naked_boxshot_tablet_138238.jpg""",
    platform = """Microsoft Windows
                  Nintendo Switch
                  PlayStation 3
                  PlayStation 4
                  PlayStation Vita
                  Wii U
                  Xbox 360
                  Xbox One""",
    developer = "Ubisoft Montpellier"  ,
    publisher = "Ubisoft"  ,
    producer = """Abdelhak Elguess
                  Pierre Arnaud Lamberta""",
    director = "Michel Ancel"  ,
    category = category2,
    user_id = 1
    )
session.add(game3)
session.commit()

game4 = Game(
    name =   "Super Mario Odyssey"  ,
    description = """Super Mario Odyssey is a platform game in which players control Mario as he travels across many different worlds, known as "Kingdoms", on the Odyssey, a hat shaped ship, to rescue Princess Peach from Bowser, who plans to forcibly marry her. 
                     The Kingdoms in the game return to the exploration based level design featured in Super Mario 64. 
                     Each Kingdom has Mario searching for and clearing various objectives in order to obtain items known as Power Moons, which can power up the Odyssey and grant access to new Kingdoms. 
                     Checkpoint flags littered throughout each Kingdom allow Mario to instantly warp to them once activated. 
                     Certain levels feature areas called "flat" zones, where Mario is placed in a 2D side scrolling environment similar to his appearance in the original Super Mario Bros.""",
    picture = """https://cdn3.dualshockers.com/wp content/uploads/2017/08/super mario boxart.jpg""",
    platform = "Nintendo Switch"  ,
    developer = "Nintendo EPD"  ,
    publisher = "Nintendo"  ,
    producer = """Yoshiaki Koizumi
                  Koichi Hayashida""",
    director = "Kenta Motokura"  ,
    category = category2,
    user_id = 1
    )
session.add(game4)
session.commit()

game5 = Game(
    name = "Crash Bandicoot N. Sane Trilogy"  ,
    description = """Crash Bandicoot N. Sane Trilogy is a collection of remasters of the first three games in the Crash Bandicoot series; Crash Bandicoot, Cortex Strikes Back and Warped. 
                     Each game features Crash Bandicoot traversing various levels in order to stop Doctor Neo Cortex from taking over the world. 
                     Like in the original games, Crash uses spinning and jumping techniques to defeat enemies, smash crates, and collect items such as Wumpa Fruits, extra lives and protective Aku Aku masks. """,
    picture = """https://file cdn.scdkey.com/product/20181125173718_scdk.jpg""",
    platform = """PlayStation 4
                  Microsoft Windows
                  Nintendo Switch
                  Xbox One""",
    developer = "Vicarious Visions"  ,
    publisher = "Activision|"  ,
    producer = """Kara Massie""",
    director = "Dan Tanguay"  ,
    category = category2,
    user_id = 1
    )
session.add(game5)
session.commit()

game6 = Game(
    name =  "God of War"  ,
    description = """God of War is a third person action adventure video game. 
                     It features an over the shoulder free camera, a departure from the previous installments, which featured a fixed cinematic camera (with the exception of 2007  s two dimensional side scroller Betrayal). 
                     Cinematographically, the game is presented in a continuous shot, with no camera cuts or loading screens. 
                     Although the previous main installment, Ascension (2013), introduced multiplayer to the series, this installment is single player only.
                     The game is open, but it is not open world. 
                     Due to its openness, players can fast travel to different locations. 
                     Swimming, an ability in previous games, was cut, and players instead use a boat to traverse bodies of water.
                     Unlike previous games, which allowed players to freely jump whenever needed, jumping can now only be done at designated areas, such as at a rockface or ledge. 
                     Throughout the game, players battle Norse mythological foes, such as dark elves, wulvers, draugrs, as well as Gullveig and the revenants, beings warped by seior magic, among many others.""",
    picture = """http://chichicity.ir/wp content/uploads/2018/05/god of war.jpg""",
    platform = """PlayStation 4""",
    developer = "SIE Santa Monica Studio",
    publisher = "Sony Interactive Entertainment",
    producer = """Elizabeth Dahm Wang
                               Sean Llewellyn
                               Chad Cox
                               Eric Fong""",
    director = "Cory Barlog",
    category = category3,
    user_id = 1
    )
session.add(game6)
session.commit()

game7 = Game(
    name =   "Red Dead Redemption 2"  ,
    description = """Red Dead Redemption 2 is a Western themed action adventure game. 
                     Played from a first or third person perspective, the game is set in
                     an open world environment featuring a fictionalized version of the Western U.S. 
                     The game features both single player and online multiplayer components.
                     The player controls outlaw Arthur Morgan, member of the Van Der Linde gang, 
                     as he completes numerous missions linear scenarios with set objectives in order to progress through the story. 
                     Outside of missions, the player may freely roam its interactive world. 
                     Unlike in the previous game, the player is granted the ability to swim. 
                     The player may engage into combat with enemies using melee attacks, firearms, or explosives. 
                     The combat has been refined from the previous game, and notable new mechanics consist 
                     of dual wielding and the ability to use a bow, which can project sharp or explosive arrows.
                     The player may also witness or take part in random events encountered from exploring the game world. 
                     These include public executions, crimes committed by other people, ambushes, pleas 
                     for assistance, ride by shootings, and dangerous animal attacks.""",
    picture = """https://cdn3.dualshockers.com/wp content/uploads/2017/08/super mario boxart.jpg""",
    platform = """PlayStation 4
                  Xbox One""",
    developer = "Rockstar Studios",
    publisher = "Rockstar Games",
    producer = """Rob Nelson""",
    category = category3,
    user_id = 1
    )
session.add(game7)
session.commit()

game8 = Game(
    name =   "The Legend of Zelda: Breath of the Wild"  , 
    description = """Breath of the Wild is an action adventure game set in an open world environment where players are tasked with exploring the kingdom of Hyrule while controlling Link. 
                     In terms of structure, Breath of the Wild encourages nonlinear gameplay, which is illustrated by the game  s lack of defined entrances or exits to areas, scant instruction given to the player, and encouragement to explore freely. 
                     Breath of the Wild introduces a consistent physics engine to the Zelda series, letting players approach problems in different ways rather than trying to find a single solution. 
                     The game also integrates a "chemistry engine" that defines the physical properties of most objects and governs how they interact with the player and one another. 
                     For example, players may take advantage of the game  s dynamic weather by throwing metal objects at enemies during thunderstorms to attract a lightning strike. 
                     However, the level of realism offered in the "chemistry engine" also means that players will equally attract an unavoidable fatal lightning strike if wearing any metal during thunderstorms.""",
    picture = """https://www.zelda.com/breath of the wild/assets/img/media/wallpaper 1 thumb.jpg""",
    platform = """Nintendo Switch
                  Wii U""",
    developer =   "Nintendo EPD"  ,
    publisher =   "Nintendo"  ,
    producer = """Eiji Aonuma""",
    director =   "Hidemaro Fujibayashi"  ,
    category = category4,
    user_id = 1
    )
session.add(game8)
session.commit()

game9 = Game(
    name =   "Grand Theft Auto V"  ,
    description = """Grand Theft Auto V is an action adventure game played from either a third person or first person perspective. 
                     Players complete missionslinear scenarios with set objectivesto progress through the story. 
                     Outside of the missions, players may freely roam the open world. Composed of the San Andreas open countryside area, including the fictional Blaine County, and the fictional city of Los Santos, the world is much larger in area than earlier entries in the series. 
                     It may be fully explored after the game  s beginning without restriction, although story progress unlocks more gameplay content.
                     Players use melee attacks, firearms and explosives to fight enemies, and may run, jump, swim or use vehicles to navigate the world. 
                     To accommodate the map  s size, the game introduces vehicle types absent in its predecessor Grand Theft Auto IV, such as fixed wing aircraft. 
                     In combat, auto aim and a cover system may be used as assistance against enemies. 
                     Should players take damage, their health meter will gradually regenerate to its halfway point. 
                     Players respawn at hospitals when their health depletes. 
                     If players commit crimes, law enforcement agencies may respond as indicated by a "wanted" meter in the head up display (HUD). 
                     Stars displayed on the meter indicate the current wanted level (for example, at the maximum five star level, police helicopters and SWAT teams swarm to lethally dispatch players). 
                     Law enforcement officers will search for players who leave the wanted vicinity. 
                     The meter enters a cool down mode and eventually recedes when players are hidden from the officers   line of sight that displays on the mini map.""",
    picture = """https://i5.walmartimages.com/asr/4928a977 3712 4a8b be65 9a4443a10277_1.513d3f2dd19e0361ae992518a938e48f.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF""",
    platform = """PlayStation 3
                  Xbox 360
                  PlayStation 4
                  Xbox One
                  Microsoft Windows""",
    developer =   "Rockstar North"  ,
    publisher =   "Rockstar Games"  ,
    producer = """Leslie Benzies
                  Imran Sarwar""",
    category = category4,
    user_id = 1
    )
session.add(game9)
session.commit()

game3 = Game(
    name =   "Shadow of the Tomb Raider"  ,
    description = """Set shortly after the events of Rise of the Tomb Raider, its story follows Lara Croft as she ventures through Mesoamerica and South America to the legendary city Paititi, battling the paramilitary organization Trinity and racing to stop a Mayan apocalypse she has unleashed. 
                     Lara must traverse the environment and combat enemies with firearms and stealth as she explores semi open hubs. 
                     In these hubs she can raid challenge tombs to unlock new rewards, complete side missions, and scavenge for resources which can be used to craft useful materials.""",
    picture = """https://upload.wikimedia.org/wikipedia/en/1/11/Shadow_of_the_Tomb_Raider_cover.png""",
    platform = """Microsoft Windows
                  PlayStation 4
                  Xbox One
                  macOS
                  Linux""",
    developer = "Eidos Montreal",
    publisher = "Square Enix"  ,
    producer = """Mario Chabtini
                  Fleur Marty""",
    director = "Daniel Chayer"  ,
    category = category1,
    user_id = 1
    )
session.add(game3)
session.commit()

game10 = Game(
    name =   "Minecraft"  ,
    description = """Minecraft is a 3D sandbox game that has no specific goals to accomplish, allowing players a large amount of freedom in choosing how to play the game. 
                     However, there is an achievement system. 
                     Gameplay is in the first person perspective by default, but players have the option for third person perspective. 
                     The game world is composed of rough 3D objectsmainly cubes and fluids, and commonly called "blocks"representing various materials, such as dirt, stone, ores, tree trunks, water, and lava. 
                     The core gameplay revolves around picking up and placing these objects. 
                     These blocks are arranged in a 3D grid, while players can move freely around the world. 
                     Players can "mine" blocks and then place them elsewhere, enabling them to build things.
                     The game world is virtually infinite and procedurally generated as players explore it, using a map seed that is obtained from the system clock at the time of world creation (or manually specified by the player).""",
    picture = """https://d1u5p3l4wpay3k.cloudfront.net/minecraft_gamepedia/thumb/7/7d/Xbox_One_Edition_Cover.png/200px Xbox_One_Edition_Cover.png?version=bafc50056306ffe143b8d8118423b9cb""",
    platform = """Microsoft Windows
                  macOS
                  Linux
                  PlayStation 
                  XBOX 360
                  PlayStation 4
                  Xbox One""",
    developer =   "Mojang"  ,
    publisher = """Mojang
                   Microsoft Studios
                   Sony Computer Entertainment""",
    category = category4,
    user_id = 1
    )
session.add(game10)
session.commit()

game11 = Game(
    name =   "One Piece Pirate Warriors 3"  ,
    description = """The gameplay is similar to the first two installments. 
                     A new feature is the Kizuna Rush, which summons another character alongside the player in battle to perform a combination attack. 
                     Up to four players can be summoned at once this way, with the finishing attacks becoming more powerful as more characters join.
                     During battle, one of the NPC support characters (known as Crew in the game) may become a Hero, which causes the Kizuna Gauge of the support character who is a hero to fill up more easily. 
                     Maxing out this support character  s Kizuna Level and filling their Kizuna Gauge, will unleash their Hero Power. 
                     Each character (Playable & Support) have their own Hero Powers which produce different effects, such as causing a barrage (such as Fujitora causing a barrage of meteors, Sakazuki unleashing a barrage magma, or Garp throwing a barrage of Cannonballs) that deals out damage to every enemy on a stage, restoring health of allied units (Chopper & Sanji  s hero power), reducing the enemy units attack power by intimidating them (Zoro and Luffy  s Hero Power), or inspiring allied units increasing their combat effectiveness and attack strength. 
                     However tough enemies can also unleash their Hero Power which causes a stunned Gauge to appear over their head and when the gauge reaches 0 the enemy will be stunned causing their Hero Power to end.""",
    picture = """https://gpstatic.com/acache/28/55/2/de/packshot b1def6b3386af6e23df2491a9c35a345.jpg""",
    platform = """	PlayStation 3
                    PlayStation 4
                    PlayStation Vita
                    Microsoft Windows
                    Nintendo Switch""",
        developer =   "Omega Force"  ,
        publisher =   "Bandai Namco Entertainment"  ,
        producer = """Koji Nakajima Hisashi Koinuma""",
        category = category5,
        user_id = 1
    )
session.add(game11)
session.commit()

game12 = Game(
    name =   "Final Fantasy XV"  , 
    description = """Final Fantasy XV is an open world action role playing game where players take control of main protagonist Noctis Lucis Caelum during his journey across the world of Eos. 
                     While accompanied by his three companions Gladiolus, Ignis and Prompto, Noctis is the only character directly controlled by the player: he can navigate through simple movement, jump over small obstacles, sprint for a limited time, and perform context based actions such as taking cover behind objects. 
                     The kingdom of Lucis is a large connected landmass that can be explored on foot, by using the party  s car "Regalia", or chocobos, recurring galliform birds in the Final Fantasy series. 
                     Both the Regalia and chosen Chocobos can be customised by the player, and Chocobos can join in battles if their connection to the characters is strong enough. 
                     While Chocobos are controlled manually, the Regalia can be either manually or automatically controlled. 
                     The party can also fast travel to areas unlocked on the world map. 
                     The Regalia must be refueled periodically at petrol stations. 
                     In towns the party can visit, there are inns and hotels where they can stay, shops where items and equipment can be purchased with the in game currency gil, and local tipsters, non playable characters (NPCs) who provide information on quests, from main story missions to side quests. 
                     Side quests are also available from individual NPCs found in towns. 
                     During some story sequences, dialogue choices appear for Noctis, with the selected option altering the response from NPCs.""",
    picture = """https://images na.ssl images amazon.com/images/I/91PRcTd QNL._SX425_.jpg""",
    platform = """PlayStation 4
                  Xbox One
                  Microsoft Windows""",
    developer =   "Square Enix Business Division 2"  ,
    publisher =   "Square Enix"  ,
    producer = """Shinji Hashimoto""",
    director =   "Hajime Tabata"  ,
    category = category6,
    user_id = 1
    )
session.add(game12)
session.commit()

game13 = Game(
    name =   "Pokemon: Lets Go and  Lets Go Eevee  ",
    description = """Pokemon: Lets Go, Pikachu   and Lets Go, Eevee   are set in the Kanto region and include the original 151 Pokemon creatures in addition to their respective Mega Evolved forms from Pokemon X and Y & Omega Ruby and Alpha Sapphire, and their Alolan Forms from Sun and Moon.
                     Lets Go, Pikachu   and Lets Go, Eevee  feature common elements of the main series, such as battling non player character Pokemon Trainers and Gym Leaders with caught Pokemon creatures. 
                     However, instead of battling them like the traditional battle system of other major Pokemon role playing games (RPGs), the catching of Pokemon creatures uses a different mechanic that is based on the mobile spin off game Pokemon Go where players throw Poke Balls at a wild Pokemon by using the motion controls of the Joy Con controller. 
                     The action can also be performed with a button press when the Joy Con controllers are docked to the console in hand held mode, but this still requires using the motion controls to aim. 
                     If a player uses the motion controls, the catching of Pokemon is based on the player  s timing rather than accuracy. 
                     Although it is possible to miss a throw, the ball is almost guaranteed to hit the Pokemon.""",
    picture = """https://www.gameaxis.com/wp-content/uploads/2018/11/pokemon-lets-go_1536566637980.jpg""",
    platform = """Nintendo Switch""",
    developer =   "Game Freak"  ,
    publisher = """The Pokemon Company
                   Nintendo""",
    producer = """Shigeru Ohmori
                  Hitoshi Yamagami
                  Akira Kinashi""",
    director =   "unichi Masuda"  ,
    category = category6,
    user_id = 1
    )
session.add(game13)
session.commit()

game14 = Game(
    name =  "Street Fighter V"  , 
                 description = """Street Fighter V carries on the 2D fighting gameplay of its predecessors, in which two fighters use a variety of attacks and special abilities to knock out their opponent. 
                                The game features the EX gauge introduced in Street Fighter III, which builds as the player lands attacks and can be used to either power up special moves or perform super combos known as Critical Arts, although the Focus Attacks from the previous game have been removed. 
                                New to this game is the "V Gauge", which builds as the player receives attacks and adds three new techniques: V Skills, V Reversals, and V Triggers. 
                                V Skills are special attacks unique to each fighter; for example, Ryu can parry an attack while M. Bison can reflect projectiles, some of which build V Gauge when successfully performed. 
                                V Reversals allow players to use a section of the V Gauge to perform a counter move whilst being attacked. 
                                Finally, V Triggers use the entire V Gauge to allow the player to perform a unique ability, such as a temporary damage boost for Ryu  s energy balls or added hits to Chun Li  s attacks. 
                                Additionally, the Stun Meter, which has been present since Street Fighter III, is made visible under the health bars in this game. 
                                The Stun Meter increases when receiving consecutive attacks and will cause the player to become stunned if filled; thus, it encourages players to play offensively when the opponent  s Meter is close to full. 
                                The game also features an interactive arena, showcasing special animations when a player is defeated at the edge of the arena.""",
                 picture = """http://www.gamers.at/wp-content/uploads/2016/01/street-fighter-5-alle-kampfer-move-isten-charakter-werte.jpg""",
                 platform = """PlayStation 4
                               Microsoft Windows
                               Arcade""",
                 developer = """Capcom
                                Dimps""",
                 publisher =   "Capcom"  ,
                 producer = """Yoshinori Ono""",
                 director =   "Takayuki Nakayama" ,
                 category= category7,
                 user_id = 1
    )
session.add(game14)
session.commit()

game14 = Game(
    name =  "Street Fighter V"  , 
                 description = """Street Fighter V carries on the 2D fighting gameplay of its predecessors, in which two fighters use a variety of attacks and special abilities to knock out their opponent. 
                                The game features the EX gauge introduced in Street Fighter III, which builds as the player lands attacks and can be used to either power up special moves or perform super combos known as Critical Arts, although the Focus Attacks from the previous game have been removed. 
                                New to this game is the "V Gauge", which builds as the player receives attacks and adds three new techniques: V Skills, V Reversals, and V Triggers. 
                                V Skills are special attacks unique to each fighter; for example, Ryu can parry an attack while M. Bison can reflect projectiles, some of which build V Gauge when successfully performed. 
                                V Reversals allow players to use a section of the V Gauge to perform a counter move whilst being attacked. 
                                Finally, V Triggers use the entire V Gauge to allow the player to perform a unique ability, such as a temporary damage boost for Ryu  s energy balls or added hits to Chun Li  s attacks. 
                                Additionally, the Stun Meter, which has been present since Street Fighter III, is made visible under the health bars in this game. 
                                The Stun Meter increases when receiving consecutive attacks and will cause the player to become stunned if filled; thus, it encourages players to play offensively when the opponent  s Meter is close to full. 
                                The game also features an interactive arena, showcasing special animations when a player is defeated at the edge of the arena.""",
                 picture = """http://www.gamers.at/wp-content/uploads/2016/01/street-fighter-5-alle-kampfer-move-isten-charakter-werte.jpg""",
                 platform = """PlayStation 4
                               Microsoft Windows
                               Arcade""",
                 developer = """Capcom
                                Dimps""",
                 publisher =   "Capcom"  ,
                 producer = """Yoshinori Ono""",
                 director =   "Takayuki Nakayama" ,
                 category= category7,
                 user_id = 1
    )
session.add(game14)
session.commit()

game15 = Game(
    name =  "Tekken 7"  ,
                 description = """Tekken 7 focuses on 1v1 battles. 
                                  Two mechanisms are introduced in the game. 
                                  The first, Rage Art, allows the player to execute critical attacks that deal roughly 30 percent damage depending on the character once their health bar is critical, in exchange for inactivating the normal attack power increase. 
                                  The second, Power Crush, lets the player continue their attacks even while being hit by the enemy, although they would still receive the damage dealt by the enemy  s attacks. 
                                  The mechanic also works for absorbing high and mid attacks. 
                                  The bound system, which staggers a character to increase opportunity for additional hits, is replaced by Screw Attack, which makes the enemy spin sideways when they are hit airborne, allowing the player to inflict additional hits after they reach the ground. 
                                  Unlike bound, however, Screw Attack cannot be used to do wall combos. 
                                  With a new display system, the game  s multiplayer allows players to choose which side of the screen to play on. 
                                  Movement has undergone some changes and is similar to the movement mechanics found in Tekken Revolution, most notably when characters walk backwards.""",
                 picture = """https://i1.wp.com/www.kodkey.com/wp content/uploads/2018/08/teken7.jpg?ssl=1""",
                 platform = """Arcade
                               Microsoft Windows
                               PlayStation 4
                               Xbox One""",
                 developer =   "Bandai Namco Studios"  ,
                 publisher =   "Bandai Namco Entertainment"  ,
                 producer = """Motohiro Okubo""",
                 director = """Katsuhiro Harada
                               Yuichi Yonemori
                               Kouhei Ikeda""",
                 category_id = 7,
                 user_id = 1
    )
session.add(game15)
session.commit()

game16 = Game(
    name =  "Naruto Shippuden: Ultimate Ninja Storm 4"  ,
                 description = """Ultimate Ninja Storm 4 features gameplay akin to that of previous games in the series, in which players battle each other in 3D arenas. 
                                  A returning feature which was omitted since the original Ultimate Ninja Storm is the ability to Wall Run. 
                                  Players will be able to dynamically take to battle to the sides of the arenas, and battle on the walls of each stage. 
                                  A major change to the feature is the ability to have one character be on the wall, while the other stays on the field. 
                                  Originally the second player was automatically moved to the wall, to keep the battle flowing and the system in check. 
                                  The option to select one of three different fighting types has been removed, which was introduced in Naruto Shippuden: Ultimate Ninja Storm Revolution, restoring the previous system of Ultimate Jutsu and Awakenings seen in the rest of the series. 
                                  Another new feature is the ability to swap characters during battle, similar to games like Marvel vs. Capcom 3. 
                                  Awakenings and ultimate jutsus from previous games also return, and can now be shared between the switchable characters, meaning players can build up their meter with one character, switch to the other and use said abilities with the other character. 
                                  However, the characters will now all share the same life bar. 
                                  Also new to the franchise is the ability to break weapons and armor, both in free battle and boss battles. 
                                  To support this, they have added the ability to create elemental damage; For example, fire can burn away clothing. 
                                  Players can, however, get rid of the fire by moving around quickly throughout the area or by getting hit with water attacks.""",
                 picture = """https://images eds ssl.xboxlive.com/image?url=8Oaj9Ryq1G1_p3lLnXlsaZgGzAie6Mnu24_PawYuDYIoH77pJ.X5Z.MqQPibUVTcegOkVb21TDTzcq5gnihG6VlWWI7EHdms767cI7A8IT8qu.OLHcv4D7OAXwA55k9jQhIMB8CH1dqlQvZW1PVrtDvW0zgq9kfklZn6u71hgbWnfpRHFC6rThtIMrMxlGWD4aAH117btbnh.uD7pLxsezIBr_.FaGbIV5.EBWwUVOU &h=1080&w=1920&format=jpg""",
                 platform = """Microsoft Windows
                               PlayStation 4
                               Xbox One""",
                 developer =   "CyberConnect2"  ,
                 publisher = """Bandai Namco Entertainment""",
                 producer = """Yuki Nishikawa""",
                 director = """Yohei Ishibashi""",
                 category_id = 7,
                 user_id = 1
    )
session.add(game16)
session.commit()

game17 = Game(
    name = "FIFA 19"  , 
                 description = """Gameplay changes on FIFA 19 include the new Active Touch System an overhaul of player control, timed finishing  where the kick button may be pressed a second time to determine the exact moment the ball is actually kicked, 50/50 battles a system for determining how likely a player will win loose balls, and Dynamic Tactics which allows players to configure strategies, and switch between them in real time during a match.
                                  FIFA 19 introduces the UEFA Champions League, UEFA Europa League and UEFA Super Cup competitions to the game, after their licences with Konami  s Pro Evolution Soccer expired. 
                                  The game will have support for promotion and relegation between the Champions League and Europa League. 
                                  Martin Tyler and Alan Smith return as regular commentators with Derek Rae and Lee Dixon as Champions League commentators. 
                                  Geoff Shreeves also returns as the touchline reporter as well as Alan McInally providing updates from around the league. 
                                  New graphics and stadiums have been implemented.""",
                 picture = """https://pbs.twimg.com/media/Dp SYoVWoAAaxAa.jpg""",
                 platform = """Microsoft Windows
                               PlayStation 3
                               PlayStation 4
                               Xbox 360
                               Xbox One
                               Nintendo Switch""",
                 developer = """EA Vancouver
                                EA Romania""",
                 publisher =   "EA Sports"  ,
                 category = category8,
                 user_id = 1
    )
session.add(game17)
session.commit()

game18 = Game(
    name =  "NBA 2k19"  ,
                 description = """NBA 2K19 is a basketball simulation video game developed by Visual Concepts and published by 2K Sports, based on the National Basketball Association (NBA). 
                                  It is the 20th installment in the NBA 2K franchise and the successor to NBA 2K19. """,
                 picture = """http://cdn.techmagz.ir/2018/10/f69cb2b5 62e4 4aca add3 601b7884b5e7.jpeg""",
                 platform = """Microsoft Windows
                               Xbox One
                               PlayStation 4
                               Nintendo Switch
                               Android
                               iOS""",
                 developer =   "Visual Concepts"  ,
                 publisher =   "2K Sports"  ,
                 category = category8,
                 user_id = 1
    )
session.add(game18)
session.commit()

game19 = Game(
    name = "Call of Duty: Black Ops 4"  , 
                 description = """Call of Duty: Black Ops 4 is a multiplayer first person shooter video game. 
                                  Unlike previous titles in the Call of Duty series, Black Ops 4 is the first entry to not feature a traditional single player campaign, and contains only Multiplayer, Zombies and a new battle royale mode called Blackout.
                                  Multiplayer: Black Ops 4  s multiplayer features the return of Specialists, unique soldier characters with special abilities and traits. 
                                  At launch, the game features a total of ten Specialists, six of which (Ruin, Prophet, Battery, Seraph, Nomad, Firebreak) are returning characters from Black Ops III, while the other four (Recon, Ajax, Torque, Crash) are new additions. 
                                  Unlike Black Ops III, the game allows only one unique Specialist per team, in order to emphasize the role of each character. 
                                  Following launch, more Specialists are added to the roster, with unique weaponry and equipment.
                                  Zombies: Zombies returns as the cooperative multiplayer mode for Black Ops 4. 
                                  The game mode features a wider range of customization, allowing for more personalized play styles. 
                                  Mechanics of the game can be customized via "Custom Mutations", which include over 100 variables, such as overall difficulty, zombie speed, health, damage, and more.
                                  Blackout: Black Ops 4 features a battle royale game mode called Blackout which will serve as a stand in for the campaign mode. 
                                  While utilizing the traditional Black Ops combat style, the mode includes the largest map featured in a Call of Duty title. 
                                  Players compete against each other through locations appeared in previous Black Ops games. 
                                  This mode will also feature land, sea, and air vehicles for players to use.""",
                 picture = """https://s3.dexerto.com/thumbnails/_thumbnailLarge/when does black ops 4 and blackout release.jpg""",
                 platform = """Microsoft Windows
                               PlayStation 4
                               Xbox One""",
                 developer = """Treyarch""",
                 publisher =   "Activision"  ,
                 director =   "Jason Blundell"  ,
                 category = category9,
                 user_id = 1
    )
session.add(game19)
session.commit()

game20 = Game(
    name =  "Battlefield V"  ,
                 description = """Battlefield V will focus extensively on party based features and mechanics, scarcity of resources, and removing "abstractions" from game mechanics to increase realism. 
                                  There will be an expanded focus on player customization through the new Company system, where players will be able to create multiple characters with various cosmetic and weapon options. 
                                  Cosmetic items, and currency used to purchase others, will be earned by completing in game objectives.
                                  The game will feature several new multiplayer modes, including the "continuous" campaign mode "Tides of War", "Firestorm", and "Grand Operations". 
                                  The Grand Operations mode is an expansion of the "Operations" mode introduced in Battlefield 1, which focuses on matches taking place across multiple stages to simulate a campaign from the war. 
                                  In Grand Operations, each round will have specific objectives, and performance in each stage will influence the next. 
                                  Games will culminate with a "Final Stand", with players using only a primary weapon with limited ammo, and no respawns. 
                                  Similarly to Battlefield 1, the game will feature a collection of single player "war stories" based on aspects of World War II. 
                                  The game also features a cooperative mode not seen since Battlefield 3 called "Combined Arms", where four players can undertake missions together and features dynamic missions and objectives so missions cannot be played the same way each time. 
                                  Combined Arms is scheduled to be released after launch. 
                                  The Battle Royale mode will be built around the franchise  s "core pillars of destruction, team play, and vehicles".""",
                 picture = """https://vignette.wikia.nocookie.net/battlefield/images/3/3c/Battlefield_V_Cover_Art.jpg/revision/latest?cb=20180524142938""",
                 platform = """Microsoft Windows
                               PlayStation 4
                               Xbox One""",
                 developer =   "EA DICE"  ,
                 publisher =   "Electronic Arts"  ,
                 producer = """Aleksander Grondal
                               Andreas Morell
                               David Sirland
                               Lars Gustavsson
                               Ryan McArthur""",
                 category = category9,
                 user_id = 1
    )
session.add(game20)
session.commit()

game21 = Game(
    name =  'Fortnite'  ,
                 description = """Currently, Fortnite is distributed as three different game modes, using the same engine and has similar graphics, art assets, and game mechanics.
                                  Fortnite: Save the World is designed as player versus environment game, with four players cooperating towards a common objective on various missions. 
                                  The game is set after a fluke storm appears across Earth, causing 98 percent of the population to disappear, and the survivors to be attacked by zombie like "husks". 
                                  The players take the role of commanders of home base shelters, collecting resources, saving survivors, and defending equipment that help to either collect data on the storm or to push back the storm. 
                                  From missions, players are awarded a number of in game items, which include hero characters, weapon and trap schematics, and survivors, all of which can be leveled up through gained experience to improve their attributes.
                                  Fortnite Battle Royale is a player versus player battle royale game for up to 100 players, allowing one to play alone, in a duo, or in a squad (usually consisting of three or four players). 
                                  Weaponless players airdrop from a "Battle Bus" that crosses the game  s map. 
                                  When they land, they must scavenge for weapons, items, and resources while trying to stay alive and attack other players, eliminating them. 
                                  Over the course of a round, the safe area of the map shrinks down in size due to an incoming storm; players outside that safe area take damage and can be eliminated if they fail to quickly evacuate. 
                                  This forces remaining players into tighter spaces and encourages player encounters. 
                                  The last player, duo, or squad remaining is the winner.
                                  Fortnite Creative is a sandbox game mode where players are given complete freedom to create anything they want on an island, such as battle arenas, race courses, platforming challenges and more. 
                                  Epic Games plans to review some of the most popular creations from Creative and rotate these into the Battle Royale map in an area called "The Block".""",
                 picture = """https://i.gadgets360cdn.com/large/fortnite_keyart_1505235339110.jpg""",
                 platform = """Windows, macOS
                               Nintendo Switch
                               PlayStation 4
                               Xbox One
                               iOS
                               Android""",
                 developer =   "Epic Games"  ,
                 publisher = """Epic Games""",
                 category = category9,
                 user_id = 1
    )
session.add(game21)
session.commit()

game22 = Game(
    name =  "PlayerUnknown  s Battlegrounds",
                 description = """Battlegrounds is a player versus player shooter game in which up to one hundred players fight in a battle royale, a type of large scale last man standing deathmatch where players fight to remain the last alive. 
                                  Players can choose to enter the match solo, duo, or with a small team of up to four people. 
                                  The last person or team alive wins the match.
                                  Each match starts with players parachuting from a plane onto one of the four maps. 
                                  The plane  s flight path across the map varies with each round, requiring players to quickly determine the best time to eject and parachute to the ground. 
                                  Players start with no gear beyond customized clothing selections which do not affect gameplay. 
                                  Once they land, players can search buildings, ghost towns and other sites to find weapons, vehicles, armor, and other equipment. 
                                  These items are procedurally distributed throughout the map at the start of a match, with certain high risk zones typically having better equipment. 
                                  Killed players can be looted to acquire their gear as well. 
                                  Players can opt to play either from the first person or third person perspective, each having their own advantages and disadvantages in combat and situational awareness; though server specific settings can be used to force all players into one perspective to eliminate some advantages.
                                  Every few minutes, the playable area of the map begins to shrink down towards a random location, with any player caught outside the safe area taking damage incrementally, and eventually being eliminated if the safe zone is not entered in time; in game, the players see the boundary as a shimmering blue wall that contracts over time. 
                                  This results in a more confined map, in turn increasing the chances of encounters. 
                                  During the course of the match, random regions of the map are highlighted in red and bombed, posing a threat to players who remain in that area. 
                                  In both cases, players are warned a few minutes before these events, giving them time to relocate to safety. 
                                  At random, a plane will fly over various parts of the playable map and drop a loot package, containing items which are typically unobtainable during normal gameplay. 
                                  These packages emit highly visible red smoke, drawing interested players near it and creating further confrontations.
                                  At the completion of each round, players gain in game currency based on their performance. 
                                  The currency is used to purchase crates which contain cosmetic items for character or weapon customization.""",
                 picture = """https://steamcdn a.akamaihd.net/steam/apps/578080/header.jpg?t=1545084399""",
                 platform = """Windows, macOS
                               Nintendo Switch
                               PlayStation 4
                               Xbox One
                               iOS
                               Android""",
                 developer =   "PUBG Corporation"  ,
                 publisher = """PUBG Corporation (Windows, PlayStation 4)
                                Microsoft Studios (Xbox One)
                                Tencent Games (mobile)""",
                 producer = """Chang han Kim""",
                 director = """Brendan Greene""",
                 category = category9,
                 user_id = 1
    )
session.add(game22)
session.commit()

game23 = Game(
    name =   "Resident Evil 7: Biohazard"  , 
                 description = """The player controls Ethan Winters from a first person perspective as he searches the Baker house for his missing wife. 
                                  Although Ethan is a civilian with few combat skills, he is able to arm himself with a variety of different weapons including handguns, shotguns, flamethrowers, explosives and chainsaws against the Baker family and a humanoid form of fungus known as the "Molded". 
                                  He can also block attacks to reduce damage. 
                                  Various sections of the game are spent being pursued by members of the Baker family, who if engaged in combat, can only be temporarily incapacitated. 
                                  However, these encounters are avoidable by means of stealth, or running away.
                                  Unlike Resident Evil 5 and Resident Evil 6, the gameplay emphasizes horror and exploration over action.""",
                 picture = """https://i.ytimg.com/vi/5iszUCmLyW4/maxresdefault.jpg""",
                 platform = """Microsoft Windows
                               PlayStation 4
                               Xbox One
                               Nintendo Switch""",
                 developer = """Capcom""",
                 publisher =   "Capcom"  ,
                 producer = """Masachika Kawata
                               Tsuyoshi Kanda""",
                 director =   "Koshi Nakanishi"  ,
                 category = category10,
                 user_id = 1
    )
session.add(game23)
session.commit()

game24 = Game(
    name =  "Outlast"  ,
                 description = """In Outlast, the player assumes the role of investigative journalist Miles Upshur, as he navigates a dilapidated psychiatric hospital overrun by homicidal patients. 
                                  The game is played from a first person perspective and features some stealth gameplay mechanics. 
                                  The player can walk, run, crouch, jump, climb ladders and vault over objects. 
                                  Unlike most games however, the player doesn  t have a visible health bar on the screen and is unable to attack enemies. 
                                  The player must instead rely on stealth tactics such as hiding in lockers, sneaking past enemies, staying in the shadows and hiding behind or under things in order to survive. 
                                  Alternatively, the player can attempt to outrun their pursuer. 
                                  If the player dies, the game will reset to the most recent checkpoint.
                                  Most of the hospital is unlit, and the only way for the player to see while in the dark is through the lens of a camcorder equipped with night vision. 
                                  Using the night vision mode will slowly consume batteries, forcing the player to scavenge for additional batteries found throughout the building. 
                                  Outlast makes heavy use of traditional jump scares and audio cues, which alert the player if an enemy has seen them. 
                                  If the player records specific events with their camcorder, Miles will write a note about it, providing further insight into his thoughts. 
                                  Documents can be collected, which offer backstory and other supplementary information about the hospital.""",
                 picture = """https://cdn02.nintendo europe.com/media/images/10_share_images/games_15/nintendo_switch_download_software_1/H2x1_NSwitchDS_OutlastBundleOfTerror_image1600w.jpg""",
                 platform = """Microsoft Windows
                               PlayStation 4
                               Xbox One
                               Linux
                               OS X
                               Nintendo Switch""",
                 developer =   "Red Barrels" ,
                 publisher =   "Red Barrels" ,
                 category = category10,
                 user_id = 1
    )
session.add(game24)
session.commit()









