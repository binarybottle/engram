# Arno's Engram keyboard layouts
Engram is a family of keyboard layouts optimized for comfortable and efficient touch typing in different languages created by [Arno Klein](https://arnoklein.info).
You can use the [open-source software](https://github.com/binarybottle/optimize-layouts) to create new key layouts optimized for different languages.

An article is currently under review that describes the Engram approach to optimizing keyboard layouts, based on language-dependent n-gram frequencies and language-independent typing preferences, using multi-objective optimization informed by crowdsourced typing data. Letters are optimally arranged according to ergonomics factors that promote reduction of lateral finger movements and more efficient typing of high-frequency letter pairs. The most common punctuation marks are logically grouped together in the middle columns and numbers are paired with mathematical and logic symbols.

Currently, there are Engram keyboard layouts for typing in:

  - English ([Engram-en](engram-en/)) 
  - Spanish ([Engram-es](engram-es/)) 

<!-- You can install the Engram-en layout on [Windows, macOS, and Linux](https://keyman.com/keyboards/engram_en)
or [try it out online](https://keymanweb.com/#en,Keyboard_engram).-->

### Engram-en layout for English

**"Ergonomic" orthonormal keyboard**
![Orthonormal keyboard](engram-en/Fig1_engram_layout_46keys_orth.jpg)

**Staggered/diagonal keyboard**
![Staggered keyboard](engram-en/Fig2_engram_layout_46keys_diag.jpg)

         [{ 1| 2= 3~ 4+  5<  6>  7^ 8& 9% 0* ]} /\
            bB yY oO uU  '(  ")  dD nN gG vV qQ #$ @`
            hH iI aA eE  ,;  .:  tT rR sS cC zZ 
            kK jJ xX wW  -_  ?!  mM lL fF pP
            
----------------

# Contents
1. [Why new key layouts?](#why-new)
2. [Why me?](#why-me)
3. [Why "Engram"?](#why-engram)
4. [Acknowledgments](#acknowledgments)

## Why new layouts? <a name="why-new">
Since the invention of the computer, researchers, engineers, artists, and designers have invented and refined many ways to facilitate human interaction with the computer, such as manipulation of peripheral devices, motion and gesture tracking, voice commands, speech-to-text, and even brain-computer interfaces. Through it all the humble keyboard remains the principal human-computer interface, dominated in form by the conventional, flat, diagonal array of keys that come with computers, laptops, and accessed virtually on mobile device screens. These conventional keyboards are not optimized to accommodate the ergodynamics of the human hand or upper body. Less conventional physical keyboard designs reposition the keys or are shaped in ways intended to reduce the strain of repetitive typing. For example, some keyboards are split into left- and right-hand sides and angled to reduce bending of the wrists, are rounded to conform to the shape of the hand, position high-access keys in the middle for easy reach by the thumbs, and arrange keys into perpendicular rows and columns to reduce diagonal finger movements. Some also permit a choice of key switches, whose force–displacement characteristics can impact strain and fatigue. The Kinesis Advantage and the Ergodox are two examples of commercial keyboard designs that also permit remapping of characters to individual keys, and therefore enable completely customizable keyboard layouts. 

Since the vast majority of people simply use the keyboard bundled with their computer or physically integrated into their laptop, adopting a better keyboard layout has the greatest potential to significantly improve comfort and reduce strain for the greatest number of people who do touch typing. And to counter the resigned statement “It’s too difficult for people to switch keyboard layouts,” it is important to recognize: (1) there are hundreds of millions of people for whom it would not be a switch, including every new generation, (2) many languages do not yet have a well-established keyboard layout, and (3) people who suffer or do not wish to suffer repetitive strain injuries from typing but need to type have vested interest in improving the ergonomics in their lives. Free and open-source software such as Keyman (keyman.com) make it easy to switch the arrangement of characters on a given computer keyboard to over 2,000 different languages.

Developing an optimal keyboard layout for a given language is another challenge altogether. There are over four hundred septillion, or four hundred trillion trillion (26! = 403,291,461,126,605,635,584,000,000, or 4.03 E+26) possible ways to arrange a sequence of 26 letters, an NP-complete problem that is currently computationally intractable to optimize. Attempts to solve the “keyboard arrangement problem” have been ongoing, with more recent contenders applying simulated annealing, ant colony optimization, Cyber Swarm, and genetic algorithms. 

## Why me? <a name="why-me">
Suffice to say I love solving problems and I have battled repetitive strain injury. I have used different key layouts (Qwerty, Dvorak, Colemak, etc.), each for years, before designing my own. None satisfied me, and none seemed to be firmly grounded in scientific research with data from real typists. So I took this on as a research challenge.

## Why "Engram"? <a name="why-engram">
The name is a pun, referring both to "n-gram", letter permutations and their frequencies that are used to compute Engram layouts, and "engram", or memory trace, the postulated change in neural tissue to account for the persistence of memory, as a nod to my attempt to make these layouts easy to remember.

## Acknowledgments <a name="acknowledgments">
The Engram layouts are the culmination of years of effort devoted to studying and optimizing keyboard layouts, so there are plenty of people and resources I wish to acknowledge. I would like to thank all of the people who have been so supportive over the years. To my family, friends, colleagues, and online participants and discussants for supporting this endeavor, whether by funding the GoFundMe campaign, volunteering as online participants for this study, or by engaging in helpful discussions. To Jack Grinband and Ian Douglas in particular for their helpful discussions. The Spanish version would not have been possible were it not for Ian Douglas cleaning up the Leipzig Spanish corpus and computing Spanish character and bigram frequencies. To those who have tried out earlier versions of my keyboard layouts and to those who have expressed interest in seeing Engram applied to different languages in the future. To the Keyman community who have helped to make distribution of the Engram (and thousands of other) layouts very convenient. I would also like to express my gratitude to all of my predecessors who have made valiant efforts to improve our relationship with computers by advancing the ergonomics of keyboard designs and keyboard layouts.

I must also express my appreciation to that damned DEC workstation at the MIT Media Lab that introduced me to repetitive strain injury 30 years ago, which has prompted me over the years to experiment with voice dictation, one-handed and keyless keyboards, foot pedals, foot mouse, and various ortholinear ergonomic keyboards like the Kinesis Advantage and Ergodox.