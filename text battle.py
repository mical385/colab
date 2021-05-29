import random as r
import time as t

enemy = []
spawn_start_rate = 20
spawn_end_rate = 60
lvl = 0
weapon_dmg = 0
dmg_reduction = 0
health = 100
coins = 0
global fighting


def help_menu():
    return ("""
    Help menu
    Options:
    fight:go into fight mode with any spawned enemy,but if there are two enemy spawned,you will fight the weakest
    help:shows this menu
    ystat:shows your stats(not in fight mode)
    inventory:shows what items you have
    estats:shows what kind of enemy they are and their health (in fight mode)
    run:Escapes fight mode,but there is a 1/5 chance that the enemy might drag you back.
        If that happens,you will lose a turn and the enemy will attack. 
    use:You can use a item that is bought from the shop menu.Typing the word alone will not work
        you can use in in battle ode,but it will let you lose your turn
    shop:Enters shop mode(not in battle mode)
        The shop sells you healing,one time damage increase and upgrades.

    -------------------------------------------------------------------
    The chances of the various types of enemies spawning are down below.
    --------------------------------------------------------------------
    Common enemy: 11/30 chance of spawning,loot:1-5 coins,HP:25
    Uncommon enemy: 9/30 chance of spawning,loot:5-13,HP:45
    Rare enemy: 6/30 chance of spawning,loot:13-25,HP:90
    Godly enemy: 3/30 chance of spawning,loot:25-50,HP:150
    Legendary enemy: 1/30 chance of spawning,loot:50-150,HP:300
    Every 20-60 seconds,a enemy will spawn based on the above spawn rates.
    there must be no other enemies for it to spawn
    ----------------------------------------------
    There will also be a chance that the enemy will miss,depending on the exhaustion
    You have a 1/8 chance of performing a critical hit,which will deal 20% more damage.
    """)


def spawn():
    while True:
        if len(enemy) == 0:
            t.sleep(r.randint(spawn_start_rate, spawn_end_rate))
            chance = r.randint(1, 30)
            if chance in range(1, 12):
                return "A Common enemy had spawned!"
            if chance in range(12, 22):
                return "A Common enemy had spawned!"
            if chance in range(22, 29):
                return "A Common enemy had spawned!"
            if chance in range(29, 33):
                return "A Common enemy had spawned!"
            if chance in range(33, 35):
                return "A Common enemy had spawned!"


def fight():
    global fighting
    if len(enemy) == 0:
        return "You drew your weapon and got ready to attack,but no one came."
    elif len(enemy) != 0:
        fighting = 1
        return "You drew your weapon and get ready for a battle with a", enemy[0], "enemy!"


print("Combat game v1.")
t.sleep(1)
print("You will spawn with a weapon with 1-5 damage")
t.sleep(1)
print("Type in help for help")
