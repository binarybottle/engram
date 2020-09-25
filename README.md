# Arno's Engram key layout

The [Engram layout](https://github.com/binarybottle/engram-layout) is a keyboard layout optimized for comfortable touch typing in English created by [Arno Klein](https://binarybottle.com), with open source code to create other optimized key layouts.

               K  O  U  Y        W  M  D  B
               I  H  E  A        R  T  S  N
               V  Z  X  C        L  G  F  P

The Shift key accesses characters (top) that look similar to the numbers:

               !  =  ?  +  $  @  ^  &  %  *
               1  2  3  4  5  6  7  8  9  0

and accesses related but less common punctuation (top):

            `    \    ;    :    {    }    |    _
            '    "    ,    .    (    )    /    -

Swapping the Backspace and Caps lock keys completes the layout:

    ~        !  =  ?  +  $  @  ^  &  %  *  <  >
    #        1  2  3  4  5  6  7  8  9  0  [  ]     Caps

    Tab        K  O  U  Y  '  "  W  M  D  B  Q  -     /
    Back       I  H  E  A  ,  .  R  T  S  N  J        Enter
    Shift      V  Z  X  C  (  )  L  G  F  P           Shift

    Ctrl   Fn  Cmd  Alt    Space     Alt  Ctrl       Arrows    

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

## Comparison with other key layouts

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

"The optimal layout score is based on a weighted calculation that factors in the distance your fingers moved (33%), how often you use particular fingers (33%), and how often you switch fingers and hands while typing (34%)."

## Factors used to compute the layout <a name="factors">
  - **N-gram letter frequencies** <br>
    
    [Peter Norvig's analysis](http://www.norvig.com/mayzner.html) of data from Google's book scanning project
  - **Flow factors** (transitions between ordered key pairs) <br>
    These factors are influenced by Dvorak's 11 criteria (1936).
  - **Finger strengths** (peak keyboard reaction forces) <br>
      "Keyboard Reaction Force and Finger Flexor Electromyograms during Computer Keyboard Work", BJ Martin, TJ Armstrong, JA Foulke, S Natarajan, Human Factors,1996,38(4),654-664.
  - **Speed** (unordered interkey stroke times) <br>
      "Estimation of digraph costs for keyboard layout optimization", A Iseri, Ma Eksioglu, International Journal of Industrial Ergonomics, 48, 127-138, 2015. <br>
      _NOTE: Speed data were only used for exploration of early key layouts._
      
## Guiding criteria   <a name="criteria">

1.  Assign 24 letters to columns of keys that don't require lateral finger movement.
2.  Assign common punctuation to keys in the middle columns of the keyboard.
3.  Assign easier-to-remember characters to the shift-number keys.
4.  Group letters for common command shortcuts close together.
5.  Arrange letters so that more frequent bigrams are faster and easier to type.
6.  Balance finger loads according to their relative strength.
7.  Promote alternating between hands over uncomfortable transitions with the same hand.
8.  Promote little-to-index-finger roll-ins over index-to-little-finger roll_outs.
9.  Avoid stretching shorter fingers up and longer fingers down.
10. Avoid using the same finger.
11. Avoid the upper and lower rows.
12. Avoid skipping over the home row.

## Summary of steps and results  <a name="summary">

- Step 1: Arrange the most frequent letters based on comfort and bigram frequencies
- Step 2: Optimize assignment of the remaining (non-command character) letters
- Step 3: Add command shortcut characters
- Step 4: Arrange punctuation marks and characters in easy-to-remember places
    
### 1: Arrange the most frequent letters based on comfort and bigram frequencies

We will assign letters to the most comfortable keys within a layout of 24 finger-column keys. These columns require no lateral finger movements when touch typing (see below). The most comfortable keys include the left and right home rows (keys 5-8 and 17-20), the top-center keys that allow the longer middle and ring fingers to uncurl upwards (keys 2,3 and 14,15), as well as the shorter fingers to curl downwards (keys 9,12 and 21,24). We will reserve the bottom left row (keys 9-12) for common command shortcut letters (Z,X,C,V):

        Left:            Right:
     1  2  3  4       13 14 15 16  
     5  6  7  8       17 18 19 20  
    [9 10 11 12]      21 22 23 24

In prior experiments, all of the vowels clustered together on the left side, due in part to suboptimal consonant-vowel arrangements. We will therefore begin by assigning the five vowels to the most comfortable keys on the left. We will assign the letter E, the most frequent in the English language, to either of the strongest keys (7 and 8, the middle and index fingers on the home row). 

**E**, T, **A, O, I**, N, S, R, H, L, D, [C], **U**, M, F, P, G, W, Y, B, [V], K, [X], J, Q, [Z]
    
We will arrange the five vowels so that any top-frequency bigram (more than 1 billion instances in Peter Norvig's analysis of Google data) reads from left to right (ex: TH, not HT). Finally, we will allow the least frequent vowel, U, to be assigned to the less comfortable key 4 (index finger on the upper row). With the above constraints, we generate the following layouts:

     -  -  U  - 
     I  O  E  A      

     -  O  U  -
     I  -  E  A    

     -  -  -  U 
     I  O  E  A      

     -  -  O  U   
     -  I  E  A    

     -  -  O  U   
     I  -  E  A    

Next we examine all possible sequences of four letters from the seven most frequent consonants (T,N,S,R,H,L,D):

E, **T**, A, O, I, **N, S, R, H, L, D**, [C], U, M, F, P, G, W, Y, B, [V], K, [X], J, Q, [Z]

We select those sequences that contain top bigrams (more than 1 billion instances in Peter Norvig's analysis) in the list below:

**TH, ND, ST, NT, NS, TR, RS**, (RT), SH, LD, RD, LS, DS, LT, (TL), RL, HR, NL, (SL)
    
When reordered from right-to-left for ease of typing with the right hand (roll-in from little to index finger vs. roll-out from index to little finger), we have five consonant sequences: HTSN, HTDN, TSDN, RTSN, RTDN. The resulting five arrangements of five vowels on the left and five arrangements of four consonants on the right gives us 25 total arrangements, each with 11 unassigned keys:

    11  --U- IOEA ---- HTSN ----
    12  --U- IOEA ---- HTDN ----
    13  --U- IOEA ---- TSDN ----
    14  --U- IOEA ---- RTSN ----
    15  --U- IOEA ---- RTDN ----
    21  -OU- I-EA ---- HTSN ----
    21  -OU- I-EA ---- HTDN ----
    21  -OU- I-EA ---- TSDN ----
    21  -OU- I-EA ---- RTSN ----
    21  -OU- I-EA ---- RTDN ----
    31  ---U IOEA ---- HTSN ----
    31  ---U IOEA ---- HTDN ----
    31  ---U IOEA ---- TSDN ----
    31  ---U IOEA ---- RTSN ----
    31  ---U IOEA ---- RTDN ----
    41  --OU -IEA ---- HTSN ----
    41  --OU -IEA ---- HTDN ----
    41  --OU -IEA ---- TSDN ----
    41  --OU -IEA ---- RTSN ----
    41  --OU -IEA ---- RTDN ----
    51  --OU I-EA ---- HTSN ----
    51  --OU I-EA ---- HTDN ----
    51  --OU I-EA ---- TSDN ----
    51  --OU I-EA ---- RTSN ----
    51  --OU I-EA ---- RTDN ----

    
### 2: Optimize assignment of the remaining (non-command character) letters
    
    
We will assign the letters that are missing from each of the above layouts by scoring every possible arrangement of these letter-key assignments and selecting the top-scored arrangement (see below for details about scoring). Missing letters include those in bold below:

E, T, A, O, I, N, **S, R, H, L, D**, [C], U, **M, F, P, G, W, Y, B**, [V], **K**, [X], J, Q, [Z]
    
Finding all permutations of 13 letters is too computationally intensive, so we will assign the two least frequent letters, Q and J, to the hardest-to-reach keys lying outside the 24-key columns, to the upper right. We will also assign two of the remaining least frequent letters (W,B) to the hard-to-reach top-corner keys on the right (13,16, leaving nine letters to permute and arrange):
    
     1  2  3  4       [W] 14 15 [B] [Q]
     5  6  7  8        17 18 19 20  [J]
     9 10 11 12        21 22 23 24
    
    
#### **Scoring details**
    
The optimization algorithm finds every permutation of a given set of letters ( for 9 letters), maps these letter permutations to a set of keys, and ranks these letter-key mappings according to a score reflecting ease of typing key pairs and frequency of letter pairs (bigrams). The score is the average of the scores for all possible bigrams in this arrangement. The score for each bigram is a product of the frequency of occurrence of that bigram and the factors Flow, Strength, and Speed: 

**Flow**: measure of ease of a finger transition from the first in a pair of letters to the second

Flow factors to _penalize_ difficult key transitions include:
    
- roll out from index to little finger
- index or little finger on top row
- middle or ring finger on bottom row
- index above middle, or little above ring 
- index above ring, or little above middle
- ring above middle
- use same finger twice for a non-repeating letter
- at least one key not on home row
- one key on top row, the other on bottom row

**Strength**: measure of the average strength of the finger(s) used to type the two letters

Finger strengths are based on peak keyboard reaction forces (in newtons) from "Keyboard Reaction Force and Finger Flexor Electromyograms during Computer Keyboard Work", BJ Martin, TJ Armstrong, JA Foulke, S Natarajan, Human Factors,1996, 38(4), 654-664.

**Speed**: normalized interkey stroke times

These are left-right averaged versions derived from the study data below, to compensate for right-handedness of participants in the study (we used this data for early experimentation):

"Estimation of digraph costs for keyboard layout optimization", 
A Iseri, Ma Eksioglu, International Journal of Industrial Ergonomics, 48, 127-138, 2015. 
    

### 3: Add command shortcut characters

We then complete the letter layout by arranging the common command characters (Z,X,C,V) on the left and the remaining least frequent letters Q and J on the far right:

          K  O  U  Y        W  M  D  B
          I  H  E  A        R  T  S  N
          -  -  -  -        L  G  F  P    

### 4. Arrange punctuation marks and characters in easy-to-remember places

    
**Frequency of punctuation** 

These sources helped guide our arrangement:
    
  - "Punctuation Input on Touchscreen Keyboards: Analyzing Frequency of Use and Costs" <br>
    S Malik, L Findlater - College Park: The Human-Computer Interaction Lab. 2013 <br>
    https://www.cs.umd.edu/sites/default/files/scholarly_papers/Malik.pdf

  - "Frequencies for English Punctuation Marks" by Vivian Cook <br>
    http://www.viviancook.uk/Punctuation/PunctFigs.htm

  - "Computer Languages Character Frequency" <br>
    Xah Lee. Date: 2013-05-23. Last updated: 2020-06-29. <br>
    http://xahlee.info/comp/computer_language_char_distribution.html

Resulting in:

          K  O  U  Y        W  M  D  B
          I  H  E  A        R  T  S  N
          V  Z  X  C        L  G  F  P

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
