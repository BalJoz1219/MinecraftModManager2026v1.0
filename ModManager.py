import json
import shutil
import turtle as t
import json
import os
i = 0

print()
scr = t.Screen()
scr.setup(1500,700)
scr.tracer(0)

new_pack_active = False  # Flag to prevent multiple New Pack prompts
selected_mod = None  # Currently selected mod for pack actions

# Load existing mods from file if it exists, otherwise create empty list
if os.path.exists("mods.json"):
    with open("mods.json", "r") as file:
        asd = json.load(file)
else:
    asd = {
        "Mods": [],
        "Packs": {},
        "Bonds": {}
    }
if os.path.exists("PathToModFolder.txt"):
    with open("PathToModFolder.txt", "r") as file:
        PathToModFolder = file.read().strip()
else:
    PathToModFolder = ""
t.hideturtle()
scr.title("Minecraft Mod Manager 2026")
t.penup()
t.goto(-450,300)
t.pencolor("black")
t.pendown()
t.write("All mods")
t.penup()
t.goto(400, 300)
t.pendown()
t.forward(80)
t.right(90)
t.forward(30)
t.right(90)
t.forward(80)
t.right(90)
t.forward(30)
t.penup()
t.back(25)
t.right(90)
t.forward(15)
t.pendown()
t.write("New Mod")
t.penup()
t.penup()
t.goto(160, 300)
t.pendown()
t.forward(200)
t.right(90)
t.forward(30)
t.right(90)
t.forward(200)
t.right(90)
t.forward(30)
t.penup()
t.back(25)
t.right(90)
t.forward(15)
t.pendown()
t.write("Change Mod Folder Path")
t.penup()
t.penup()
t.goto(-40, 300)
t.pendown()
t.forward(80)
t.right(90)
t.forward(30)
t.right(90)
t.forward(80)
t.right(90)
t.forward(30)
t.penup()
t.back(25)
t.right(90)
t.forward(15)
t.pendown()
t.write("All Packs")
t.penup()
t.penup()
t.goto(60, 300)
t.pendown()
t.forward(80)
t.right(90)
t.forward(30)
t.right(90)
t.forward(80)
t.right(90)
t.forward(30)
t.penup()
t.back(25)
t.right(90)
t.forward(15)
t.pendown()
t.write("New Pack")
t.penup()
t.penup()
t.goto(160, 300)
t.pendown()
t.forward(200)
t.right(90)
t.forward(30)
t.right(90)
t.forward(200)
t.right(90)
t.forward(30)
t.penup()
t.back(25)
t.right(90)
t.forward(15)
t.pendown()
t.write("Change Mod Folder Path")
t.penup()
t.penup()
t.penup()
t.setheading(0)
t.goto(-550, -310)
t.pendown()
t.forward(80)
t.right(90)
t.forward(30)
t.right(90)
t.forward(80)
t.right(90)
t.forward(30)
t.penup()
t.back(25)
t.right(90)
t.forward(15)
t.pendown()
t.write("Delete Pack")
t.penup()
t.penup()
t.setheading(0)
t.goto(-360, -310)
t.pendown()
t.forward(80)
t.right(90)
t.forward(30)
t.right(90)
t.forward(80)
t.right(90)
t.forward(30)
t.penup()
t.back(25)
t.right(90)
t.forward(15)
t.pendown()
t.write("Choose Pack")
t.penup()
t.forward(80)
t.right(90)
t.forward(30)
t.right(90)
t.forward(80)
t.right(90)
t.forward(30)
t.penup()
t.back(25)
t.right(90)
t.forward(15)
t.pendown()
t.write("New Pack")
t.penup()
t.goto(-450,248)
t.pendown()
t.penup()
t.setheading(0)
t.goto(-260, -310)
t.pendown()
t.forward(80)
t.right(90)
t.forward(30)
t.right(90)
t.forward(80)
t.right(90)
t.forward(30)
t.penup()
t.back(25)
t.right(90)
t.forward(7)
t.pendown()
t.write("Unchoose Pack")
t.penup()
t.penup()
t.setheading(0)
t.goto(-460, -310)
t.pendown()
t.forward(80)
t.right(90)
t.forward(30)
t.right(90)
t.forward(80)
t.right(90)
t.forward(30)
t.penup()
t.back(25)
t.right(90)
t.forward(15)
t.pendown()
t.write("Delete mod")
t.penup()
def ChangeModFolderClick(x,y):
    if x > 159 and x < 361 and y >269 and y < 301:
        global asd  
        global PathToModFolder         
        PathToModFolder = scr.textinput("Path", "Path to the Mods folder:")
        PathToModFolder = PathToModFolder[1:-1]
        with open("PathToModFolder.txt", "w+") as file:
            file.write(PathToModFolder)
        if os.path.exists("mods.json"):
            with open("mods.json", "r") as file:
                asd = json.load(file)
        else:
            asd = {
                "Mods": [],
                "Packs": {},
                "Bonds": {}
            }

def NewPackClick(x,y):
    global new_pack_active
    if not new_pack_active and 60 <= x <= 140 and 269 <= y <= 301:
        new_pack_active = True
        newPack = scr.textinput("Pack", "Name of the new pack:")
        if newPack:
            addedMod = scr.textinput("Pack", f"Mod's path you want to add to {newPack}:")
            addedMod = addedMod[1:-1]
            if addedMod:
                if newPack not in asd["Packs"]:
                    asd["Packs"][newPack] = []
                if addedMod not in asd["Packs"][newPack]:
                    asd["Packs"][newPack].append(addedMod)
                    with open("mods.json","w+") as file:
                        json.dump(asd, file)
        new_pack_active = False

def delete_mod_click(x,y):
    global selected_mod
    if -460 <= x <= -360 and -350 <= y <= -280:
        mod_to_delete = scr.textinput("Mod deleting", "Path to the mod you want to delete: ")
        mod_to_delete = mod_to_delete[1:-1]
        if not mod_to_delete:
            return
        removed = False
        if mod_to_delete in asd.get("Mods", []):
            asd["Mods"].remove(mod_to_delete)
            removed = True
        for pack_mods in asd.get("Packs", {}).values():
            while mod_to_delete in pack_mods:
                pack_mods.remove(mod_to_delete)
                removed = True
        if "Bonds" in asd:
            if mod_to_delete in asd["Bonds"]:
                del asd["Bonds"][mod_to_delete]
                removed = True
            for bond_list in asd["Bonds"].values():
                while mod_to_delete in bond_list:
                    bond_list.remove(mod_to_delete)
                    removed = True
        if selected_mod == mod_to_delete:
            selected_mod = None
        if removed:
            with open("mods.json", "w+") as file:
                json.dump(asd, file)
            draw_mods()
            draw_packs()
        try:
            if os.path.exists(mod_to_delete):
                os.remove(mod_to_delete)
        except Exception as e:
            print(f"Failed to delete file: {e}")

def ChoosePackClick(x, y):
    if -360 <= x <= -280 and -350 <= y <= -300:
        packToChoose = scr.textinput("Choose Pack", "Name of the pack to choose:")
        for i in range(len(asd["Packs"][packToChoose])):
            source = asd["Packs"][packToChoose][i]
            destination = PathToModFolder
            shutil.copy(source, destination)
            i += 1


def get_bonded_group(mod_name):
    """Return a set of mods bonded together with mod_name, including itself."""
    if "Bonds" not in asd:
        return {mod_name}
    bonded = {mod_name}
    stack = [mod_name]
    while stack:
        current = stack.pop()
        for partner in asd.get("Bonds", {}).get(current, []):
            if partner not in bonded:
                bonded.add(partner)
                stack.append(partner)
    return bonded


def add_bond(mod_a, mod_b):
    if "Bonds" not in asd:
        asd["Bonds"] = {}
    asd["Bonds"].setdefault(mod_a, [])
    asd["Bonds"].setdefault(mod_b, [])
    if mod_b not in asd["Bonds"][mod_a]:
        asd["Bonds"][mod_a].append(mod_b)
    if mod_a not in asd["Bonds"][mod_b]:
        asd["Bonds"][mod_b].append(mod_a)


xx = -480
yy = 300
i = 0
mod_positions = []  # Track positions of clickable mods

def draw_mods():
    """Draw all mods in the list"""
    global yy, mod_positions
    mod_positions = []  # Reset positions
    t.setheading(0)
    # Clear the mods area
    t.penup()
    t.goto(-480, 290)
    t.pencolor("white")
    t.fillcolor("white")
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(300)
        t.right(90)
        t.forward(500)
        t.right(90)
    t.end_fill()
    
    # Redraw mods
    yy = 300
    t.penup()
    t.goto(-480, yy-15)
    t.setheading(0)
    t.pencolor("black")
    if len(asd["Mods"]) > 0:
        for i in range(len(asd["Mods"])):
            t.penup()
            t.goto(-480, yy-15)
            t.pendown()
            t.write(asd["Mods"][i])
            # Store mod position for click detection
            mod_positions.append({
                "name": asd["Mods"][i],
                "x": -480,
                "y": yy-15
            })
            yy -= 15
    t.update()

def ModClick(x, y):
    """Check if a mod was clicked"""
    global selected_mod
    for mod in mod_positions:
        # Calculate text width (approximate: 8 pixels per character)
        text_width = len(mod["name"]) * 8
        # Check if click is within the mod text bounds (adjusted hitbox)
        if mod["x"] <= x <= mod["x"] + text_width and mod["y"] - 5 <= y <= mod["y"] + 5:
            selected_mod = mod["name"]
            t.penup()
            t.goto(0,350)
            t.pendown()
            t.pendown()
            t.forward(80)
            t.right(90)
            t.forward(30)
            t.right(90)
            t.forward(80)
            t.right(90)
            t.forward(30)
            t.penup()
            t.back(25)
            t.right(90)
            t.forward(15)
            t.pendown()
            t.write("Add to a pack")
            t.penup()
            t.goto(100,350)
            t.pendown()
            t.pendown()
            t.forward(80)
            t.right(90)
            t.forward(30)
            t.right(90)
            t.forward(80)
            t.right(90)
            t.forward(30)
            t.penup()
            t.back(25)
            t.right(90)
            t.forward(15)
            t.pendown()
            t.write("Bond")
            t.penup()
            t.goto(200,350)
            t.pendown()
            t.pendown()
            t.forward(120)
            t.right(90)
            t.forward(30)
            t.right(90)
            t.forward(120)
            t.right(90)
            t.forward(30)
            t.penup()
            t.back(25)
            t.right(90)
            t.forward(15)
            t.pendown()
            t.write("Remove from pack")
            t.penup()
            t.goto(340,350)
            t.pendown()
            t.pendown()
            t.forward(80)
            t.right(90)
            t.forward(30)
            t.right(90)
            t.forward(80)
            t.right(90)
            t.forward(30)
            t.penup()
            t.back(25)
            t.right(90)
            t.forward(15)
            t.pendown()
            t.write("Close")
            t.penup()

            return

def NewModClick(x,y):
    global asd
    if x > 390 and x < 481 and y >269 and y < 301:
        newMod = scr.textinput("Mod", "Path to the mod:")
        newMod = newMod[1:-1]
        if newMod and newMod not in asd["Mods"]:
            asd["Mods"].append(newMod)
            with open("mods.json","w+") as file:
                json.dump(asd, file)
            draw_mods()  # Redraw the list after adding
def CloseClick(x,y):
    if 340 <= x <= 420 and 320 <= y <= 350:
        t.penup()
        t.goto(0,350)
        t.setheading(0)
        t.pendown()
        t.pencolor("white")
        t.fillcolor("white")
        t.begin_fill()
        for _ in range(2):
            t.forward(600)
            t.right(90)
            t.forward(30)
            t.right(90)
        t.end_fill()
        draw_mods()  # Restore mod list after closing overlay
def put_in_pack_click(x, y):
    global selected_mod
    if 0 <= x <= 80 and 320 <= y <= 350:
        if selected_mod:
            mods_to_add = sorted(get_bonded_group(selected_mod))
        else:
            modToAdd = scr.textinput("Pack", "Which mod do you want to add to a pack?")
            modToAdd = modToAdd[1:-1]
            mods_to_add = [modToAdd] if modToAdd in asd["Mods"] else []
        if not mods_to_add:
            return
        packToAdd = scr.textinput("Pack", "Name of the pack to add to:")
        if packToAdd:
            if packToAdd not in asd["Packs"]:
                asd["Packs"][packToAdd] = []
            for mod_name in mods_to_add:
                if mod_name not in asd["Packs"][packToAdd]:
                    asd["Packs"][packToAdd].append(mod_name)
            with open("mods.json","w+") as file:
                json.dump(asd, file)
            draw_packs()  # Update packs display after adding

def DeletePackClick(x, y):
    if -140 <= x <= -60 and 269 <= y <= 301:
        packToDelete = scr.textinput("Delete Pack", "Name of the pack to delete:")
        if packToDelete in asd.get("Packs", {}):
            del asd["Packs"][packToDelete]
            with open("mods.json", "w+") as file:
                json.dump(asd, file)
            draw_packs()
        else:
            print(f"Pack '{packToDelete}' not found")
    elif -550 <= x <= -470 and -350 <= y <= -300:
        packToDelete = scr.textinput("Delete Pack", "Name of the pack to delete:")
        if packToDelete in asd.get("Packs", {}):
            del asd["Packs"][packToDelete]
            with open("mods.json", "w+") as file:
                json.dump(asd, file)
            draw_packs()
        else:
            print(f"Pack '{packToDelete}' not found")

def RemoveFromPackClick(x, y):
    if 199 <= x <= 280 and 320 <= y <= 350:
        if selected_mod:
            mods_to_remove = sorted(get_bonded_group(selected_mod))
        else:
            modToRemove = scr.textinput("Pack", "Which mod do you want to remove from a pack?")
            modToRemove = modToRemove[1:-1]
            mods_to_remove = [modToRemove] if modToRemove in asd["Mods"] else []
        if not mods_to_remove:
            return
        packToRemove = scr.textinput("Pack", "Name of the pack to remove from:")
        if packToRemove in asd["Packs"]:
            for mod_name in mods_to_remove:
                if mod_name in asd["Packs"][packToRemove]:
                    asd["Packs"][packToRemove].remove(mod_name)
            with open("mods.json","w+") as file:
                json.dump(asd, file)
            draw_packs()  # Update packs display after removing
def bond_click(x, y):
    if 100 <= x <= 180 and 320 <= y <= 350:
        modToBond = scr.textinput("Bond", "Which is the first mod do you want to bond?")
        modToBond2 = scr.textinput("Bond", "Which is the second mod do you want to bond?")
        modToBond = modToBond[1:-1]
        modToBond2 = modToBond2[1:-1]
        if modToBond in asd["Mods"] and modToBond2 in asd["Mods"]:
            add_bond(modToBond, modToBond2)
            with open("mods.json","w+") as file:
                json.dump(asd, file)
            draw_packs()
            print(f"Bonded {modToBond} and {modToBond2}")
        else:
            print("Both mods must exist before bonding")

def draw_packs():
    """Draw all packs on-screen in the right area."""
    t.setheading(0)
    # Clear the packs area on the right side
    t.penup()
    t.goto(0, 250)
    t.pencolor("white")
    t.fillcolor("white")
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(320)
        t.right(90)
        t.forward(380)
        t.right(90)
    t.end_fill()
    
    # Draw packs list
    t.penup()
    t.goto(10, 250)
    t.setheading(0)
    t.pencolor("black")
    if "Packs" not in asd or len(asd["Packs"]) == 0:
        t.write("No packs available")
        t.update()
        return
    line = 0
    for pack_name, mods in asd["Packs"].items():
        t.penup()
        t.goto(10, 250 - line * 20)
        t.pendown()
        t.write(f"{pack_name}:")
        line += 1
        for mod_name in mods:
            t.penup()
            t.goto(30, 250 - line * 20)
            t.pendown()
            t.write(f"- {mod_name}")
            line += 1
        line += 1  # Extra blank line after each pack
    t.update()

def unchoose_pack_click(x,y):
    if x > -260 and x < -180 and y > -350 and y < -300:
        packToUnchoose = scr.textinput("Unchoose Pack", "Name of the pack to unchoose:")
        for i in range(len(asd["Packs"][packToUnchoose])):
            ht = os.path.split(asd["Packs"][packToUnchoose][i])
            ht[1]
            source = fr"{PathToModFolder}\{ht[1]}"
            os.remove(source)
def draw_used_packs():
    """Draw only packs that contain mods."""
    t.penup()
    t.goto(0, -150)
    t.pencolor("white")
    t.fillcolor("white")
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(320)
        t.right(90)
        t.forward(380)
        t.right(90)
    t.end_fill()
    
    t.penup()
    t.goto(10, -150)
    t.pencolor("black")
    used_packs = {k: v for k, v in asd.get("Packs", {}).items() if len(v) > 0}
    if not used_packs:
        t.write("No used packs available")
        t.update()
        return
    line = 0
    for pack_name, mods in used_packs.items():
        t.penup()
        t.goto(10, -150 - line * 20)
        t.pendown()
        t.write(f"{pack_name}:")
        line += 1
        for mod_name in mods:
            t.penup()
            t.goto(30, -150 - line * 20)
            t.pendown()
            t.write(f"- {mod_name}")
            line += 1
        line += 1  # Extra blank line after each pack
    t.update()


def all_packs_click(x, y):
    # Bottom-left All Packs button
    if -450 <= x <= -370 and -310 <= y <= -280:
        draw_packs()
    # Top-left All Packs button
    if -40 <= x <= 40 and 269 <= y <= 301:
        draw_packs()


def ScreenClick(x, y):
    ChangeModFolderClick(x, y)
    NewPackClick(x, y)
    all_packs_click(x, y)
    ChoosePackClick(x, y)
    DeletePackClick(x, y)
    NewModClick(x, y)
    ModClick(x, y)
    CloseClick(x, y)
    put_in_pack_click(x, y)
    RemoveFromPackClick(x, y)
    bond_click(x, y)
    unchoose_pack_click(x,y)
    delete_mod_click(x,y)

# Register a single click dispatcher so every button and area works
# (Turtle only supports one onscreenclick handler at a time)
# Also draw mods once initially.

draw_mods()
t.onscreenclick(ScreenClick, 1)
t.listen()

# Draw initial mods list
# draw_mods()  # already called above

t.done()
