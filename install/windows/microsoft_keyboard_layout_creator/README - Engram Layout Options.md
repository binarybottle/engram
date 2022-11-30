# Engram Keyboard Layout Options for Windows

- by Abigail Read (@AbbyRead), June 2022

The available options contained in this zip file should, to the best of my knowledge, work on any Windows OS.  
## Why not use the Keyman version instead?

Keyman is great, but it necessitates an additional app running in the background (namely, Keyman) for it to work.  This means if your computer runs an update or has a hiccup that causes it not to run at start-up you will have to open it up yourself manually before you can go back to using the layout.  Kind of annoying.

Additionally, and more importantly, Keyman seems to use some sort of higher level software trickery to do what it does.  This means certain programs may not respond correctly to the layout.  To get slightly technical as to why, when a program is designed within a framework meant to reach as many platforms as possible (Windows, Mac, Linux, etc.) it will often have things coded in a low-level way that acts as similarly as possible across multiple environments.  Often the simplest route is the one with the least OS-specific best practices in mind.  So when you have two programs functioning half right, where the Venn diagram overlaps is where it fails to deliver.  

So we end up back where we started, needing something that functions well on the operating system it was designed for.  That's where these native ports come in.  These were designed in Microsoft's own official app for doing so: Microsoft Keyboard Layout Creator, and the .klc files included here are the project files from that program.  So, if you want to play around with them and make your own flavor, have at it.  If you wish to publish that flavor though, have a look at the (very permissive) license here first: https://github.com/binarybottle/engram/blob/master/LICENSE

## Two versions?  What's the difference?

Inside the zip file, you will see two different folders: engram2b and engram2c.  Most people will just want to go with engram2b, as that remains faithful to the Engram 2.0 layout.

The other version is one Abby cooked up that rectifies (in a way) one very rare use case compatibility problem.  On testing out the engram2b layout, my good friend Abby (the creator of this readme and port; I'm just going to talk in third-person) tried out DOSBox.  Even with the layout correctly functioning as a Windows-compatible layout, was not recognised by DOSBox, presumably because it references hardware keys as opposed to whatever the operating system says a key is supposed to be.  While this is bothersome for us, DOSBox at least has a key remapper program built-in and accessible during play.  Where it falls short though is in assuming no one would ever want to reassign characters across different keys for when the shift key is or isn't held.  So there is unfortunately NO KNOWN WAY for DOSBox to be made compatible with this layout short of going into the app's source code and doing it yourself.  Abby's solution: Engram 2.C (for compatibility).  This keeps most of the feel of the original intent, without splitting and reassigning the characters on any of the keys.  So, keycap shape permitting, with the 2.C layout you could actually rearrange the real hardware keys yourself to get yourself an official unofficial Engram Keyboard, cheap as free!

## So why 2b?  Why not just call it 2 if it's the same layout as 2.0?

Well, Abby goofed on her first attempt, bless her heart.  Ignoring all the validation warnings from the program, she spat out what we we'll now refer to as 2a, uploading it as fast as she could in order to get that sweet, sweet "I contributed to something" feel.  In creating that version though she made some hasty assumptions as to what the operating system would do with its standard hotkeys.  Turns out, Windows maintains the physical layout for things like cut, copy, paste WITHOUT needing to force it in the layout program (as she had tried to do with 2a).  Forcing it (needlessly) by assigning just a BUNCH of exceptions for when Ctrl or Alt are pressed actually led to a buuuuuuuuuunch of compatibility hiccups.  Hence why we do not speak of 2a.  Only 2b (and maybe c).

## Installation

When you decide on a layout or why-not-both it, you will need to run the setup.exe that will be found inside either folder.  All this does is pick the appropriate .msi file for the processor your computer has and run it.  If your computer doesn't trust it, try making it trust it.  Tell him it'll be okay, just run it.  should take like a millisecond to install, and you can thank your computer for bearing with you.

## Okay, where is it?

On Windows 10:
You should first try restarting your computer.  Then go into Start --> Settings --> Time & Language --> Language (on the side pane).  Scroll down to Preferred Languages, and you'll see English (I'm assuming).  Click that, and then click Options.  Scroll down to Keyboards and click Add a keyboard.  Scroll through until you find one or more that start with "Engram 2.0".  If you find one that just says Engram, don't click that; that's the Keyman version.  I mean you can, but at this point, why you still bothering with that, huh?  If you installed both, they may both show up as the exact same name.  Abby don't know how to fix that.  She put the name in the files right, but all she sees is twins on the OS.  They still work like the two different versions though, b and c.  Might just have to play around on notepad to determine which is which.  Sorry.  :shrug:

## But MAAAAAAAHM!  I'm still having compatibility issues wif my favorite program!!

Jeez, kid, get off my back.  Haven't I done enough for you?  Back in my day, we just had ONE layout, and it was QWERTY!  If you want compatibility so bad why don't you go out and get a job!  Earn your own compatibility for Christ's sake.

But srsly this time.  Autohotkey is amazing, and you should try figuring it out if you never want to have to use QWERTY again and maybe become a god in the process.  Abby couldn't pull it off, but she's a hopeless goober.  Don't be like Abby.  Fail until you fail better.  Fail upwards.  Fake it until you make it more... more better.  Being bad at something is the first step toward being kinda good at something.  A cartoon for teeny child babies told me that one.  I really like that cartoon.

## There any good places to practice this?

A lot of places really.  No need to buy Mavis Beacon anymore.  All that paid stuff is waaaaaaay outdated at this point anyways.

List of suggestions (in raw link form because Abigail is a lazy piece of work):
https://monkeytype.com/
https://btype.io/
https://eatkin.itch.io/a-relaxing-typing-game
https://www.tipp10.com/en/
https://klavaro.sourceforge.io/en/index.html
https://www.gnu.org/savannah-checkouts/gnu/gtypist/gtypist.html

## Who can I thank for all this?

Well, binarybottle mostly.  He's the brains behind Engram 2.0, and Abby just copied his notes, made a port, a spinoff, and this weird readme that you definitely read all of just now.  :wink:
https://github.com/binarybottle
https://github.com/AbbyRead

### Cheers!  And happy typing!
