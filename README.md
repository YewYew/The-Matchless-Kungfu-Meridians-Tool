#  The Matchless Kungfu Meridians Tool 
### [绝世好武功经络工具]

Tool for finding optimal meridian paths for inner skills in The Matchless Kungfu.
> https://store.steampowered.com/app/1696440/The_Matchless_Kungfu/
> 
> https://store.steamchina.com/app/1696440/_/

---

## Features:

* Automatically calculates meridian path(s) that provide the most skills.
* Customizable skill list and meridian count limit for calculations.
* Kinda fast calculation speed.

### To-do (Maybe):

* Account for multiple paths and "doubling up" on meridians.
* Account for current meridian types.
* Make the tool a web application.
    * Visual editor with pathfinding for meridian layout.
    * Skill Database of all inner skills in game.
* Convert/utilize concept for a workshop mod.

## Installation and Utilization:

1. Download and extract the repository (or just MeridiansTool.py).
2. Edit the script "MeridiansTool.py"
    * Follow the instructions within, which summarized are:
        * Edit the `skills` and `meridians_count` variables.
3. Save, then run the script with your preferred method.
4. Wait for it to finish.
5. Apply the results to your game... or don't!

### Understanding the output:

Output looks like the following:

```
Pattern Length: 18 / 20
Skills (6):
  Breathing Skill
  Art of Harmony
  Beastmaster
  Bionic Pentaform
  Art of Drunkness
  Golden Acupuncture
OTSOTSOSTOTTSOSTOT
```

*Pattern length* is how many meridians the path takes, and the maxmum available.

*Skills* is the list and count of inner techniques the path enables.

The letters at the end is the *meridian pattern* or *path*:
* **O** is a circle meridian.
* **S** is a square meridian.
* **T** is a triangle meridian.

## Notes:

The tool generates the path that contains the most skills, it may not be the most beneficial.
* Multiple paths are possible in-game, which can be better then a single long path.
* Paths can end at another's used meridian, triggering a bonus twice and saving room.
* The tool currently assumes you can freely change your meridian shapes.

You, as the tool user, need to determine if the results are truly optimal.

## Requirements:
1. [Python (3.12.4 or Latest, probably)](https://www.python.org/downloads/ "Python Homepage")

