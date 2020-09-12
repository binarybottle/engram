# Arno's Engram key layout

The [Engram layout](https://github.com/binarybottle/engram-layout) is an optimal keyboard layout for touch typing in English created by [Arno Klein](https://binarybottle.com),  with open source code.


                   Q  I  O  U        D  N  L  Y  Z  
                   P  H  E  A        T  S  R  C  X 
                   B  J  K  G        M  F  W  V

The Shift key accesses characters (top) that look similar to the numbers:

                   !  =  ?  +  $  @  ^  &  %  *
                   1  2  3  4  5  6  7  8  9  0

and accesses related but less common punctuation (top):

                `    \    ;    :    {    }    |    _
                '    "    ,    .    (    )    /    -

Swapping the Backspace and Caps lock keys completes the layout:


           ~        !  =  ?  +  $  @  ^  &  %  *  <  >
           #        1  2  3  4  5  6  7  8  9  0  [  ]     Caps

         Tab        Q  I  O  U  '  "  D  N  L  Y  Z  -     /
         Back       P  H  E  A  ,  .  T  S  R  C  X        Enter
         Shift      B  J  K  G  (  )  M  F  W  V           Shift

         Ctrl  Fn  Cmd  Alt     Space     Alt  Ctrl       Arrows

# Contents
1. [Rationale](#rationale)
2. [Comparison with other key layouts](#comparison)
3. [Factors used to compute the layout](#factors)
4. [Guiding criteria](#criteria)
5. [Summary of steps and results](#summary)

## Rationale <a name="rationale">

**Why?** <br>
In the future, I hope to include an engaging rationale for why I took on this challenge.
Suffice to say that I have battled repetitive strain injury since I worked
on an old DEC workstation at the MIT Media Lab while composing my thesis back in the mid-90s.
Ever since then I have used different key layouts (Dvorak, Colemak, my own, etc.),
and have primarily used Colemak for almost 10 years.  I find that they all place too much stress on tendons, with lateral extension of the index and little fingers,
and on uniform distribution of finger use, which has damaged my little fingers.
I have also experimented with a wide variety of human interface technologies
(voice dictation, one-handed keyboard, keyless keyboard, foot mouse, and ergonomic keyboards like the Kinesis Advantage. I recently got an Ergodox that I am looking forward to trying out with the Engram layout.

**"Engram"?** <br>
The name is a pun, referring both to "n-gram", letter permutations used to compute this layout, and "engram", or memory trace, the postulated change in neural tissue to account for the persistence of memory.

## Comparison with other key layouts <a name="comparison">

Despite the fact that the Engram layout was designed to reduce strain and discomfort, not to reduce finger travel from the home row, it scores higher than all other key layouts (Colemak, Dvorak, QWERTY, etc.) I've tested using the online Keyboard Layout Analyzer, for all of the examples of prose and tweet data I've tried, including the data sets below:

- [See the complete analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/x0WPtw3x)
of __Alice in Wonderland__ provided by the Keyboard Layout Analyzer 

- All __20,000 tweets__ from [Gender Classifier Data](https://www.kaggle.com/crowdflower/twitter-user-gender-classification) <br>
Added: November 15, 2015 by CrowdFlower

- The first __100,000 tweets__ from: [Sentiment140 dataset](https://data.world/data-society/twitter-user-data) training data <br>
Go, A., Bhayani, R. and Huang, L., 2009. <br>
Twitter sentiment classification using distant supervision. <br>
CS224N Project Report, Stanford, 1(2009), p.12.

According to the [Keyboard Layout Analyzer](http://patorjk.com/keyboard-layout-analyzer/):

    "The optimal layout score is based on a weighted calculation that factors in 
    the distance your fingers moved (33%), 
    how often you use particular fingers (33%),
    and how often you switch fingers and hands while typing (34%)."
    
## Factors used to compute the layout <a name="factors">
  - **N-gram letter frequencies** <br>
    
    [Peter Norvig's analysis](http://www.norvig.com/mayzner.html) of data from Google's book scanning project
  - **Flow factors** (transitions between ordered key pairs) <br>
    These factors are influenced by Dvorak's 11 criteria (1936) that can be summarized as follows:
      - Alternate between hands and balance finger loads.
      - Avoid using the same finger.
      - Avoid the upper and lower rows.
      - Avoid skipping over the home row ("hurdling").
      - Avoid tapping adjacent rows ("reaching") with (same or) adjacent fingers.
  - **Finger strengths** (peak keyboard reaction forces) <br>
      "Keyboard Reaction Force and Finger Flexor Electromyograms during Computer Keyboard Work", BJ Martin, TJ Armstrong, JA Foulke, S Natarajan, Human Factors,1996,38(4),654-664.
  - **Speed** (unordered interkey stroke times) <br>
      "Estimation of digraph costs for keyboard layout optimization", A Iseri, Ma Eksioglu, International Journal of Industrial Ergonomics, 48, 127-138, 2015. <br>
      _NOTE: Speed data were only used for exploration of early key layouts._

## Guiding criteria   <a name="criteria">

  1.  Assign 24 letters to keys that don't require lateral extension of index or little fingers.
  2.  Group letters for common command shortcut keys (F,C,Z,Y,X,V) close together.
  3.  Assign punctuation to keys that require lateral extension of index or little fingers.
  4.  Assign easier-to-remember characters to the shift-number keys.
  5.  Arrange letters so that more frequent bigrams are faster and easier to type.
  6.  Balance finger loads according to their relative strength.
  7.  Promote alternating between hands over typing with the same hand.
  8.  Promote little-to-index-finger roll-ins over index-to-little-finger roll_outs.
  9.  Avoid extending nearer, shorter fingers to upper rows.
  10. Avoid using the same finger.
  11. Avoid the upper and lower rows.
  12. Avoid skipping over the home row.
  
## Summary of steps and results  <a name="summary">

- Step 1: Optimize arrangement of the 12 most frequent letters across left and right sides
- Step 2: Arrange the most common command shortcut characters on the right side
- Step 3: Optimize arrangement of all remaining letters
- Step 4: Add punctuation marks and characters above similar-looking numbers
    
### 1. Optimize arrangement of the 12 most frequent letters across left and right sides

I selected 12 of the strongest key locations for the 12 most frequent letters in the English language (excluding C, which we group with other common command shortcut characters):

**E, T, A, O, I, N, S, R, H, L, D**, C, **U**, M, F, P, G, W, (Y), B, (V), K, (X), J, Q, (Z)

The 12 letters are split across left and right sides by an optimization algorithm, which is then used to optimize the arrangement of the 6 letters on each side.

The resulting arrangement led to all vowels on the left and the most common consonants on the right (except for H):

                   -  I  O  U        D  N  L  -  - 
                   -  H  E  A        T  S  R  -  -
                   -  -  -  -        -  -  -  -

#### **Details** <br>
I set an initial location for E and T, the most common letters, with E on the left side and T on the right side, to encourage a balance of typing across left and right hands, and to reduce the number of permutations to compute (3,628,800 for 10 letters). Each permutation corresponds to a unique arrangement of letters, and we score each arrangement by the average of the scores for all possible pair of letters (bigrams) in this arrangement. The score for each bigram is a product of the frequency of occurrence of that bigram and the factors Flow, Strength, and Speed: 

**Flow**: measure of ease of a finger transition from the first in a pair of letters to the second

Flow factors to _penalize_ difficult key transitions include:
    
- roll out from index to little finger
- either index or little finger on top row
- either middle or ring finger on bottom row
- index above middle, or little above ring 
- index above ring, or little above middle
- index above little, or little above index
- ring above middle
- use same finger twice
- at least one key not on home row
- one key on top row, the other on bottom row

**Strength**: measure of the average strength of the finger(s) used to type the two letters

Finger strengths are based on peak keyboard reaction forces (in newtons) from "Keyboard Reaction Force and Finger Flexor Electromyograms during Computer Keyboard Work", BJ Martin, TJ Armstrong, JA Foulke, S Natarajan, Human Factors,1996, 38(4), 654-664.

**Speed**: normalized interkey stroke times

These are left-right averaged versions derived from the study data below, to compensate for right-handedness of participants in the study:

"Estimation of digraph costs for keyboard layout optimization", 
A Iseri, Ma Eksioglu, International Journal of Industrial Ergonomics, 48, 127-138, 2015. 
    
### 2. Arrange the most common command shortcut characters on the right side
    
                   -  I  O  U        D  N  L  Y  Z
                   -  H  E  A        T  S  R  C  X 
                   -  -  -  -        -  -  -  V

  - Typing a command shortcut is usually done by holding the Command/Control key with the left little finger, potentially the weakest, while simultaneously stretching and tapping the shortcut letter with the same hand. By placing the command shortcut key on the far right side, this encourages one to type the Command/Control key with the left hand and the shortcut with the right hand.
  - Z is the least frequent letter and is placed in the worst position.
  - Undo (Z) & Redo (Y), and Cut (X) & Copy (C) pair well together. Y is to the left of Z and C to the left of X because they are more frequent letters.
  - Common bigrams with Y and C (LY, CT, NC, SC, CR) are easy to type.

### 3. Optimize arrangement of all remaining letters (as in Step 1)

E, T, A, O, I, N, S, R, H, L, D, C, U, **M, F, P, G, W**, (Y), **B**, (V), **K**, (X), **J, Q**, (Z)   

                   Q  I  O  U        D  N  L  Y  Z
                   P  H  E  A        T  S  R  C  X 
                   B  J  K  G        M  F  W  V

### 4. Add punctuation, and characters above the number keys

**Frequency of punctuation** 

These sources helped guided our arrangement:
    
  - "Punctuation Input on Touchscreen Keyboards: Analyzing Frequency of Use and Costs" <br>
    S Malik, L Findlater - College Park: The Human-Computer Interaction Lab. 2013 <br>
    https://www.cs.umd.edu/sites/default/files/scholarly_papers/Malik.pdf

  - "Frequencies for English Punctuation Marks" by Vivian Cook <br>
    http://www.viviancook.uk/Punctuation/PunctFigs.htm

  - "Computer Languages Character Frequency" <br>
    Xah Lee. Date: 2013-05-23. Last updated: 2020-06-29. <br>
    http://xahlee.info/comp/computer_language_char_distribution.html

Resulting in:

                   Q  I  O  U  '  "  D  N  L  Y  Z
                   P  H  E  A  ,  .  T  S  R  C  X 
                   B  J  K  G  (  )  M  F  W  V

Shift accesses similar-looking characters above the numbers:

                ~  !  =  ?  +  $  @  ^  &  %  *  [  ]
                #  1  2  3  4  5  6  7  8  9  0  <  >

Shift accesses less common, but similar-meaning punctuation:

                `    \    ;    :    {    }    |    _
                '    "    ,    .    (    )    /    -
             
**Rationale for shift-characters**

**#** &nbsp;&nbsp; The pound/hash represents numbers, and sits to the left of the number keys. <br>
**~** &nbsp;&nbsp; The tilde has several meanings, including "approximately equal to" <br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (here "similar-looking" to the numbers), and is in the standard location.

**'** &nbsp;&nbsp; Single quotation marks are used to quote text for 'emphasis', or to quote text within a quote. <br>
**`** &nbsp;&nbsp; One use of the backquote is to quote computer code. It is used in an analogous manner as a single quote <br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; in a quote, to quote code within code for command substitution (to replace a command with output).

**"** &nbsp;&nbsp; "Double quotation marks are used to quote direct speech?" <br>
**\** &nbsp;&nbsp; The backslash is an escape character used to quote special characters in regular expressions.

**,** &nbsp;&nbsp; The comma is used to separate text, for example in lists, or to provide a pause. <br>
**;** &nbsp;&nbsp; The semicolon provides a stronger separation or pause; it can be used in place <br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; of the comma to separate items in a list, especially if those items contain commas. <br>
   
**.** &nbsp;&nbsp; The period ends a sentence. <br>
**:** &nbsp;&nbsp; The colon similarly ends a statement but precedes something following: explanation, quotation, list, etc.

**|** &nbsp;&nbsp; The pipe connects commands in computer code. <br>
**/** &nbsp;&nbsp; The slash connects conjunctions/disjunctions/alternatives, or locations such as file paths or urls.

**-** &nbsp;&nbsp; The dash connects side-by-side words, or can surround a phrase for emphasis. <br>
**_** &nbsp;&nbsp; The underscore connects strings within variable or file names, or can _underline a phrase_ for emphasis.
