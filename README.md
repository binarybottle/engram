# Arno's Engram key layout

Engram is a key layout optimized for comfortable and efficient touch typing in English 
created by [Arno Klein](https://binarybottle.com), 
with [open source code](https://github.com/binarybottle/engram) to create other optimized key layouts.
You can install the Engram layout on [Windows, macOS, and Linux](https://keyman.com/keyboards/engram)
or [try it out online](https://keymanweb.com/#en,Keyboard_engram).

Letters are optimally arranged according to ergonomic factors that promote reduction of lateral finger movements and more efficient typing of high-frequency letter pairs: 

             Y  O  U  X            W  D  C  V  Q 
             I  H  E  A            R  T  S  N  Z      
             P  K  J  G            L  B  F  M             

The most common punctuation marks are logically grouped together in the middle columns (accessed directly and by the Shift key) and numbers are paired with mathematical and logic symbols (accessed by the Shift Key):

          {  |  =  ~  +    <   >    ^  &  %  *  }  \
          [  1  2  3  4    5   6    7  8  9  0  ]  /

             Y  O  U  X   '(   ")   W  D  C  V  Q  #$  @
             I  H  E  A   ,;   .:   R  T  S  N  Z      
             P  K  J  G   -_   ?!   L  B  F  M             

See below for a full description and comparisons with other key layouts.

<!--
### Default layer
![Default layer](https://github.com/binarybottle/engram/blob/master/assets/engram-base-layer.png?raw=true)
### Shift layer
![Shift layer](https://github.com/binarybottle/engram/blob/master/assets/engram-shift-layer.png?raw=true)
-->

### Default layer (ergonomic keyboard)
![Ergonomic keyboard default layer](https://github.com/binarybottle/engram/blob/master/assets/engram-base-layer-ergodox.png?raw=true)
### Shift layer (ergonomic keyboard)
![Ergonomic keyboard Shift layer](https://github.com/binarybottle/engram/blob/master/assets/engram-shift-layer-ergodox.png?raw=true)
[Ergonomic keyboard images care of [Ergodox](https://configure.ergodox-ez.com/ergodox-ez/layouts/APXBR/latest/0).]

(c) 2021 Arno Klein, MIT license

--------------------------------

# Contents
1. [Why a new key layout?](#why)
2. [How does Engram compare with other key layouts?](#scores)
3. [Factors used to compute the Engram layout](#factors)
4. [Guiding criteria](#criteria)
5. [Summary of steps and results](#summary)

## Why a new key layout? <a name="why">

**Personal history** <br>
In the future, I hope to include an engaging rationale for why I took on this challenge.
Suffice to say I love solving problems, and I have battled repetitive strain injury 
ever since I worked on an old DEC workstation at the MIT Media Lab while composing 
my thesis back in the 1990s.
I have experimented with a wide variety of human interface technologies over the years --
voice dictation, one-handed keyboard, keyless keyboard, foot mouse, and ergonomic keyboards 
like the Kinesis Advantage and Ergodox keyboards with different key switches.
While these technologies can significantly improve comfort and reduce strain, 
an optimized key layout can only help when typing on ergonomic or standard keyboards. 

I have used different key layouts (Qwerty, Dvorak, Colemak, etc.)
for communications and for writing and programming projects,
and have primarily relied on Colemak for the last 10 years. 
**I find that most to all of these key layouts:**

- Demand too much strain on tendons
    - *strenuous lateral extension of the index and little fingers*
- Ignore the ergonomics of the human hand
    - *different finger strengths*
    - *different finger lengths*
    - *natural roundedness of the hand*
    - *home row easier than upper row for shorter fingers*
    - *home row easier than lower row for longer fingers*
    - *ease of little-to-index finger rolls vs. reverse*
- Over-emphasize alternation between hands and under-emphasize same-hand, different-finger transitions
    - *same-row, adjacent finger transitions are easy and comfortable*
    - *little-to-index finger rolls are easy and comfortable*

While I used ergonomic principles outlined below and the accompanying code to help generate the Engram layout,
I also relied on massive bigram frequency data for the English language. 
if one were to follow the procedure below and use a different set of bigram frequencies for another language or text corpus,
they could create a variant of the Engram layout, say "Engram-French", better suited to the French language.
    
**Why "Engram"?** <br>
The name is a pun, referring both to "n-gram", letter permutations and their frequencies that are used to compute the Engram layout, and "engram", or memory trace, the postulated change in neural tissue to account for the persistence of memory, as a nod to my attempt to make this layout easy to remember.

## How does Engram compare with other key layouts? <a name="scores">

Despite the fact that the Engram layout was designed to reduce strain and discomfort, not specifically to increase speed or reduce finger travel from the home row, it scores higher than all other key layouts (Colemak, Dvorak, QWERTY, etc.) for some large, representative, publicly available data (all text sources are listed below and available on [GitHub](https://github.com/binarybottle/text_data)). Below are tables of different prominent key layouts scored using the Engram Scoring Model (detailed below), and generated by the online [Keyboard Layout Analyzer](http://patorjk.com/keyboard-layout-analyzer/) (KLA):

> The optimal layout score is based on a weighted calculation that factors in the distance your fingers moved (33%), how often you use particular fingers (33%), and how often you switch fingers and hands while typing (34%).
 
#### Engram Scoring Model scores for existing layouts based on publicly available text data
    
| Layout | Google bigrams | Alice in Wonderland | Romeo Juliet | Bhaghavad Gita | Memento screenplay | 100K tweets | 20K tweets | MASC tweets | MASC spoken | COCA blogs | Google website | Sofware languages |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Engram | 0.02497 | 0.01941 | 0.02095 | 0.01935 | 0.02592 | 0.03297 | 0.02976 | 0.02789 | 0.01835 | 0.02481 | 0.04379 | 0.02735 |
| Halmak | 0.02465 | 0.01924 | 0.02078 | 0.01915 | 0.02579 | 0.03282 | 0.02951 | 0.02765 | 0.01826 | 0.02455 | 0.04342 | 0.02705 |
| Norman | 0.02416 | 0.01899 | 0.02044 | 0.01892 | 0.02538 | 0.03224 | 0.02892 | 0.02709 | 0.01798 | 0.02409 | 0.04201 | 0.02653 |
| Workman | 0.02445 | 0.01906 | 0.02058 | 0.01897 | 0.02557 | 0.03251 | 0.02924 | 0.02742 | 0.01804 | 0.02431 | 0.04277 | 0.02687 |
| QGMLWB | 0.02324 | 0.01830 | 0.01969 | 0.01812 | 0.02445 | 0.03116 | 0.02811 | 0.02601 | 0.01738 | 0.02320 | 0.04094 | 0.02545 |
| Colemak Mod-DH | 0.02421 | 0.01876 | 0.02034 | 0.01881 | 0.02519 | 0.03213 | 0.02876 | 0.02713 | 0.01783 | 0.02407 | 0.04216 | 0.02674 |
| Colemak | 0.02431 | 0.01881 | 0.02044 | 0.01884 | 0.02530 | 0.03229 | 0.02888 | 0.02724 | 0.01790 | 0.02418 | 0.04221 | 0.02703 |
| ASSET | 0.02371 | 0.01831 | 0.01996 | 0.01828 | 0.02484 | 0.03170 | 0.02836 | 0.02676 | 0.01743 | 0.02365 | 0.04188 | 0.02652 |
| Capewell | 0.02383 | 0.01860 | 0.02013 | 0.01858 | 0.02489 | 0.03177 | 0.02844 | 0.02670 | 0.01768 | 0.02374 | 0.04141 | 0.02620 |
| Dvorak | 0.02363 | 0.01847 | 0.02002 | 0.01834 | 0.02473 | 0.03148 | 0.02831 | 0.02640 | 0.01760 | 0.02355 | 0.04101 | 0.02596 |
| QWERTY | 0.02133 | 0.01684 | 0.01812 | 0.01669 | 0.02242 | 0.02879 | 0.02580 | 0.02404 | 0.01581 | 0.02133 | 0.03793 | 0.02401 |

#### Keyboard Layout Analyzer scores for existing layouts based on publicly available text data
    
| Layout | Alice in Wonderland | Romeo Juliet | Bhaghavad Gita | Memento screenplay | 100K tweets | 20K tweets | MASC tweets | MASC spoken | COCA blogs | Google website | Software languages |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Engram | 67.20 | 57.66 | 57.82 | 54.85 | 60.52 | 55.87 | 56.99 | 61.15 | 66.94 | 34.26 | 45.58 |
| Halmak | 66.25 | 57.02 | 57.45 | 55.03 | 60.86 | 55.53 | 57.13 | 62.32 | 67.29 | 30.41 | 47.60 |
| Norman | 62.76 | 53.21 | 53.44 | 52.33 | 57.43 | 53.24 | 53.90 | 59.97 | 62.80 | 28.29 | 46.01 |
| Workman | 64.78 | 56.67 | 56.97 | 54.29 | 59.98 | 55.81 | 56.25 | 61.34 | 65.27 | 29.28 | 47.76 | 
| QGMLWB | 65.45 | 55.67 | 55.57 | 54.07 | 60.51 | 56.05 | 56.90 | 62.23 | 66.26 | 33.05 | 45.72 | 
| Colemak Mod-DH | 65.74 | 56.05 | 57.52 | 54.91 | 60.75 | 54.94 | 57.15 | 61.29 | 67.12 | 31.85 | 48.50 | 
| Colemak | 65.83 | 56.12 | 57.63 | 54.94 | 60.67 | 54.97 | 57.04 | 61.36 | 67.14 | 31.48 | 48.65 | 
| ASSET | 64.60 | 54.63 | 56.09 | 53.84 | 58.66 | 54.72 | 55.35 | 60.81 | 64.71 | 33.05 | 47.52 | 
| Capewell | 63.40 | 55.67 | 56.56 | 53.45 | 59.27 | 52.84 | 55.28 | 59.80 | 64.29 | 28.27 | 45.62 | 
| Dvorak | 65.86 | 58.18 | 57.29 | 55.09 | 60.93 | 55.56 | 56.59 | 62.75 | 66.64 | 28.85 | 45.55 | 
| QWERTY | 53.06 | 43.74 | 44.92 | 44.25 | 48.28 | 44.99 | 44.59 | 51.79 | 52.31 | 24.28 | 39.89 | 

---
    
| Text source | Information |
| --- | --- |
| "Alice in Wonderland" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/mN0CTbZ3) of Alice in Wonderland (Ch.1), a standard text used for comparing layouts |
| "Romeo and Juliet" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/FVBfzMB5) of [Romeo and Juliet](https://www.fulltextarchive.com/page/Romeo-and-Juliet1/) |
| "Bhaghavad Gita" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/w4xFG5HG) of [Bhaghavad Gita](https://www.gutenberg.org/files/2388/2388-h/2388-h.htm) |
| "Memento screenplay" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/WblX3l9d) of the screenplay for [Memento](https://www.dailyscript.com/scripts/memento.html) |
| "100K tweets" | 100,000 tweets from: [Sentiment140 dataset](https://data.world/data-society/twitter-user-data) training data |
| "20K tweets" | 20,000 tweets from [Gender Classifier Data](https://www.kaggle.com/crowdflower/twitter-user-gender-classification) |
| "MASC tweets" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/fv3Cj2zQ) of [MASC](http://www.anc.org/data/masc/corpus/) tweets (cleaned of html markup) |
| "MASC spoken" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/CvHXTg7n) of [MASC](http://www.anc.org/data/masc/corpus/) spoken transcripts (phone and face-to-face: 25,783 words) |
| "COCA blogs" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/fv3Cj2zQ) of [Corpus of Contemporary American English](https://www.english-corpora.org/coca/) [blog samples](https://www.corpusdata.org/) |
| "Google website" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/CtwvHjM5) of the [Google home page](https://google.com) (accessed 10/20/2020) |
| "Software languages" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/szdpfS3K) of the "Tower of Hanoi" (programming languages A-Z from [Rosetta Code](https://rosettacode.org/wiki/Towers_of_Hanoi)) |

| Layout | Year | Website |
| --- | --- | --- |
| Engram | 2021 | https://engram.dev |
| [Halmak 2.2](https://keyboard-design.com/letterlayout.html?layout=halmak-2-2.en.ansi) | 2016 | https://github.com/MadRabbit/halmak |
| [Norman](https://keyboard-design.com/letterlayout.html?layout=norman.en.ansi) | 2013 | https://normanlayout.info/ |
| [Workman](https://keyboard-design.com/letterlayout.html?layout=workman.en.ansi) | 2010 | https://workmanlayout.org/ | 
| [QGMLWB](https://keyboard-design.com/letterlayout.html?layout=qgmlwb.en.ansi) | 2009 | http://mkweb.bcgsc.ca/carpalx/?full_optimization | 
| [Colemak Mod-DH](https://keyboard-design.com/letterlayout.html?layout=colemak-mod-DH-full.en.ansi) | 2017 | https://colemakmods.github.io/mod-dh/ | 
| [Colemak](https://keyboard-design.com/letterlayout.html?layout=colemak.en.ansi) | 2006 | https://colemak.com/ | 
| [ASSET](https://keyboard-design.com/letterlayout.html?layout=asset.en.ansi) | 2006 | http://millikeys.sourceforge.net/asset/ | 
| [Capewell-Dvorak](https://keyboard-design.com/letterlayout.html?layout=capewell.en.ansi) | 2004 | http://michaelcapewell.com/projects/keyboard/layout_capewell-dvorak.htm |
| [Dvorak](https://keyboard-design.com/letterlayout.html?layout=dvorak.en.ansi) | 1936 | https://en.wikipedia.org/wiki/Dvorak_keyboard_layout | 
| [QWERTY](https://keyboard-design.com/letterlayout.html?layout=qwerty.en.ansi) | 1873 | https://en.wikipedia.org/wiki/QWERTY |

## Factors used to compute the Engram layout <a name="factors">
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

### Step 1: Define the shape of the key layout to minimize lateral finger movements

We will assign 24 letters to 8 columns of keys separated by two middle columns reserved for punctuation. These 8 columns require no lateral finger movements when touch typing, since there is one column per finger. The most comfortable keys include the left and right home rows (keys 5-8 and 17-20), the top-center keys (2,3 and 14,15) that allow the longer middle and ring fingers to uncurl upwards, as well as the bottom corner keys (9,12 and 21,24) that allow the shorter fingers to curl downwards. We will assign the two least frequent letters, Z and Q, to the two hardest-to-reach keys lying outside the 24-key columns in the upper right:

        Left:            Right:
     1  2  3  4       13 14 15 16  Q/Z
     5  6  7  8       17 18 19 20  Z/Q
     9 10 11 12       21 22 23 24

### Step 2: Arrange the most frequent letters based on comfort and bigram frequencies

We will assign letters to keys by choosing the arrangement with the highest score according to our scoring model. However, there are over four hundred septillion, or four hundred trillion trillion (26! = 403,291,461,126,605,635,584,000,000, or 4.032914611 E+26) possible arrangements of 26 letters (24! = 6.204484017 E+23), so we will arrange the letters in stages, based on ergonomic principles.
    
In prior experiments using the methods below, all vowels consistently automatically clustered together. Below, we will arrange vowels on one side and the most frequent consonants to the other side to encourage balance and alternation across hands. Since aside from the letters Z and Q there is symmetry across left and right sides, we will decide later which side the vowels and which side the most frequent consonants should go.

#### Vowels
    
**E**, T, **A, O, I**, N, S, R, H, L, D, C, **U**, M, F, P, G, W, **Y**, B, V, K, X, J, Q, Z

We will assign the four most frequent vowels (E,A,O,I) to the most comfortable keys in the home and upper rows (keys 5-8 and 2-3) of one side, with the letter E, the most frequent in the English language, assigned to either of the strongest keys (7 and 8, the middle and index fingers on the left home row). The letter U may also take the less comfortable key 4. We will arrange the vowels such that any top-frequency bigram (more than 1 billion instances in Peter Norvig's analysis of Google data) reads from left to right (ex: TH, not HT) for ease of typing (roll-in from little to index finger vs. roll-out from index to little finger). These constraints lead to two comfortable and efficient layouts:
    
         -  O  U  -
         I  -  E  A    

         -  -  U  - 
         I  O  E  A      
   
#### Consonants

Next, to populate the home row on the other side of the keyboard, we examine all possible sequences of four letters from the eight most frequent consonants (T,N,S,R,H,L,D,C), covering half the alphabet, where each letter has at least 100 billion (at least 3% of) instances in Peter Norvig's analysis:

E, **T**, A, O, I, **N, S, R, H, L, D, C**, U, M, F, P, G, W, Y, B, V, K, X, J, Q, Z

These eight consonants are included among the highest frequency bigrams, listed below in bold, with more than 10 billion instances:

**TH, ND, ST, NT, CH, NS, CT, TR, RS, NC**, (RT), SH, LD, RD, LS, DS, LT, (TL), RL, HR, NL, (SL)
    
To maximize the number of bigrams we can comfortably type, we select 4-consonant sequences that consist of three consecutive highest frequency (>10 billion instances) bigrams, such as NSTR = NS + ST + TR. We also restrict T to the strongest (middle or index) fingers, because T is the most frequent consonant. Below are the resulting 4 consonant sequences:

         N  S  T  H
         N  S  T  R
         N  C  T  H
         N  C  T  R
    
The resulting 2 arrangements of five vowels on the left and 4 arrangements of four consonants on the right gives us 8 layouts, each with 15 unassigned keys (letters on the right side are reversed, in case Hand 2 is assigned to the right hand):

        Hand 1            Hand 2
    -OU- I-EA ----    ---- HTSN ----
    -OU- I-EA ----    ---- RTSN ----
    -OU- I-EA ----    ---- HTCN ----
    -OU- I-EA ----    ---- RTCN ----
    --U- IOEA ----    ---- HTSN ----
    --U- IOEA ----    ---- RTSN ----
    --U- IOEA ----    ---- HTCN ----
    --U- IOEA ----    ---- RTCN ----    

### Step 3: Optimize assignment of the remaining letters
    
We want to assign the 15 missing letters to the unassigned keys in each of the above 8 layouts based on our scoring model. That would mean scoring all possible arrangements for each layout and choosing the arrangement with the highest score, but since there are over 1.3 trillion possible ways of arranging 15 letters (15! = 1,307,674,368,000), we will need to break up the assignment into two stages: first for the most frequent remaining letters, and second for the least frequent remaining letters. 
    
#### Most frequent letters
First we will compute scores for every possible arrangement of the 9 most frequent remaining letters among those in bold below for the most comfortable of the remaining positions (4,9,12,13,14,15,21,24, and either 2 or 6):

E, T, A, O, I, N, **S, R, H, L, D, C**, U, **M, F, P, G, W**, Y, B, V, K, X, J, Q, Z

       Hand 1:          Hand 2:
     -  2  -  4       13 14 15  -
     -  6  -  -        -  -  -  -
     9  -  - 12       21  -  - 24
    
Since there are 9! = 362,880 possible combinations, and we have 8 layouts, we need to score and evaluate 2,903,040 combinations.  
    
To score each arrangement of letters, we construct a frequency matrix of each ordered pair of letters (bigram), and multiply this frequency matrix by our speed-strength-flow matrix to compute a score. 
    
#### Least frequent letters
Second, we will compute scores for every possible arrangement of the 8 least frequent letters (aside from Z and Q) in bold below for the least comfortable remaining positions (1,10,11,16,22,23, and again: 4,13):

E, T, A, O, I, N, S, R, H, L, D, C, U, M, F, P, **G, W, Y, B, V, K, X, J**, Q, Z

       Hand 1:          Hand 2:
     1  -  -  4       13  -  - 16
     -  -  -  -       -   -  -  -
     - 10 11  -       -  22 23  -   

Since there are 8! = 40,320 possible combinations, and we have 8 layouts, we need to score and evaluate 322,560 more combinations.    
    
    
#### **Engram Scoring Model**
    
The optimization algorithm finds every permutation of a given set of letters, maps these letter permutations to a set of keys, and ranks these letter-key mappings according to a score reflecting ease of typing key pairs and frequency of letter pairs (bigrams). The score is the average of the scores for all possible bigrams in this arrangement. The score for each bigram is a product of the frequency of occurrence of that bigram and the factors Flow, Strength, and Speed: 

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

These are left-right averaged versions derived from the study data below, to compensate for right-handedness of participants in the study (we used this data for early experimentation and validation):

"Estimation of digraph costs for keyboard layout optimization", 
A Iseri, Ma Eksioglu, International Journal of Industrial Ergonomics, 48, 127-138, 2015. 

    
### Step 4: Stability Tests
    
We will run three types of stability tests on the 8 winning layouts:
    1. Exchange letters in rows
    2. Compare effects of Flow, Strength, and/or Speed matrices
    3. Reset parameters

It is clear from the results of all of the tests above that one layout consistently scores at the top, and we will accept this as the winning layout. Since the middle row spells "I HEARTS N" we'll put Z to the right for "I HEARTS NZ" (for New Zealand) so that it is easy to remember, and place the Q above:

             Y  O  U  X     W  D  C  V  Q 
             I  H  E  A     R  T  S  N  Z      
             P  K  J  G     L  B  F  M             
    
Our arrangement of letters is complete!
    
### Step 5. Arrange non-letter characters in easy-to-remember places

Now that we have all 26 letters accounted for, we turn our attention to non-letter characters, taking into account frequency of punctuation and ease of recall.
    
### Frequency of punctuation marks

  - Statistical values of punctuation frequency in 20 English-speaking countries (Table 1): <br>
Sun, Kun & Wang, Rong. (2018). Frequency Distributions of Punctuation Marks in English: Evidence from Large-scale Corpora. English Today. 10.1017/S0266078418000512. <br> 
https://www.researchgate.net/publication/328512136_Frequency_Distributions_of_Punctuation_Marks_in_English_Evidence_from_Large-scale_Corpora
  <br>"frequency of punctuation marks attested for twenty English-speaking countries and regions... The data were acquired through GloWbE."
  "The corpus of GloWbE (2013) is a large English corpus collecting international English from the internet, containing about 1.9 billion words of text from twenty different countries. For further information on the corpora used, see https://corpus.byu.edu/."
  
  - Google N-grams and Twitter analysis: <br>
"Punctuation Input on Touchscreen Keyboards: Analyzing Frequency of Use and Costs" <br>
S Malik, L Findlater - College Park: The Human-Computer Interaction Lab. 2013 <br>
https://www.cs.umd.edu/sites/default/files/scholarly_papers/Malik.pdf <br>
 "the Twitter corpora included substantially higher punctuation use than the Google corpus,  <br>
 comprising 7.5% of characters in the mobile tweets and 7.6% in desktop versus only 4.4%...  <br>
With the Google corpus,only 6 punctuation symbols (. -’ ( ) “) appeared more frequently than [q]"

  - "Frequencies for English Punctuation Marks" by Vivian Cook <br>
http://www.viviancook.uk/Punctuation/PunctFigs.htm  <br>
 "Based on a writing system corpus some 459 thousand words long.  <br> 
 This includes three novels of different types (276 thousand words),  <br>
 selections of articles from two newspapers (55 thousand), <br> 
one bureaucratic report (94 thousand), and assorted academic papers <br>
on language topics (34 thousand). More information is in <br>
Cook, V.J. (2013) ‘Standard punctuation and the punctuation of the street’ <br>
in M. Pawlak and L. Aronin (eds.), Essential Topics in Applied Linguistics and Multilingualism,  <br>
 Springer International Publishing Switzerland (2013), 267-290"

  - "A Statistical Study of Current Usage in Punctuation": <br>
Ruhlen, H., & Pressey, S. (1924). A Statistical Study of Current Usage in Punctuation. The English Journal, 13(5), 325-331. doi:10.2307/802253

  - "Computer Languages Character Frequency"
by Xah Lee.  <br>
Date: 2013-05-23. Last updated: 2020-06-29. <br>
http://xahlee.info/comp/computer_language_char_distribution.html <br>
NOTE: biased toward C (19.8%) and Py (18.5%), which have high use of "_".

Frequency: 

             Sun:     Malik:   Ruhlen:    Cook:            Xah:
              /1M   N-gram %   /10,000   /1,000       All%  JS%   Py%

    .    42840.02      1.151       535     65.3       6.6   9.4  10.3
    ,    44189.96                  556     61.6       5.8   8.9   7.5
    "                  2.284        44     26.7       3.9   1.6   6.2
    '     2980.35      0.200        40     24.3       4.4   4.0   8.6
    -     9529.78      0.217        21     15.3       4.1   1.9   3.0
    ()    4500.81      0.140         7                7.4   9.8   8.1
    ;     1355.22      0.096        22      3.2       3.8   8.6
    z                  0.09                   -         -
    :     3221.82      0.087        11      3.4       3.5   2.8   4.7
    ?     4154.78      0.032        14      5.6       0.3
    /                  0.019                          4.0   4.9   1.1
    !     2057.22      0.013         3      3.3       0.4
    _                  0.001                         11.0   2.9  10.5


### Add punctuation keys and number keys

We will assign the most frequent punctuation according to Sun, et al (2018) to the six keys in the middle two columns:  . , " ' - ? ; : () ! _

             Y  O  U  X   '   "   W  D  C  V  Q 
             I  H  E  A   ,   .   R  T  S  N  Z      
             P  K  J  G   -   ?   L  B  F  M             

We will use the Shift key to group similar punctuation marks (separating and joining marks in the left middle column and closing marks in the right middle column):

             Y  O  U  X  '(   ")  W  D  C  V  Q 
             I  H  E  A  ,;   .:  R  T  S  N  Z      
             P  K  J  G  -_   ?!  L  B  F  M             
 
**Separating marks (left)**: The comma separates text in lists; the semicolon can be used in place of the comma to separate items in a list (especially if these items contain commas); open parenthesis sets off an explanatory word, phrase, or sentence. 

**Joining marks (left)**: The apostrophe joins words as contractions; the hyphen joins words as compounds; the underscore joins words in cases where whitespace characters are not permitted (such as in variables or file names). 

**Closing marks (right)**: A sentence usually ends with a period, question mark, or exclamation mark. The colon ends one statement but precedes the following: an explanation, quotation, list, etc. Double quotes and close parenthesis closes a word, clause, or sentence separated by an open parenthesis.

**Number keys**: 
The numbers are flanked to the left and right by [square brackets], and {curly brackets} accessed by the Shift key. Each of the numbers is paired with a mathematical or logic symbol accessed by the Shift key:
    
          {  |  =  ~  +    <   >    ^  &  %  *  }  \
          [  1  2  3  4    5   6    7  8  9  0  ]  /

    1: | (vertical bar or "pipe" represents the logical OR operator: 1 stroke, looks like the number one)
    2: = (equal: 2 strokes, like the Chinese character for "2")
    3: ~ (tilde: "almost equal", often written with 3 strokes, like the Chinese character for "3")
    4: + (plus: has four quadrants; resembles "4")
    5 & 6: < > ("less/greater than"; these angle brackets are directly above the other bracket keys)
    7: ^ (caret for logical XOR operator as well as exponentiation; resembles "7")
    8: & (ampersand: logical AND operator; resembles "8")
    9: % (percent: related to division; resembles "9")
    0: * (asterisk: for multiplication; resembles "0") 

The three remaining keys in many common keyboards (flanking the upper right hand corner Backspace key) are displaced in special ergonomic keyboards, such as the Kinesis Advantage and Ergodox. For the top right key, we will assign the forward slash and backslash: / \\. For the remaining two keys, we will assign two symbols that in modern usage have significance in social media: the hash/pound sign and the "at sign". The hash or hashtag identifies digital content on a specific topic (the Shift key accesses the dollar sign). The "at sign" identifies a location or affiliation (such as in email addresses) and acts as a "handle" to identify users in popular social media platforms and online forums.

The resulting Engram layout:

          {  |  =  ~  +    <   >    ^  &  %  *  }  \
          [  1  2  3  4    5   6    7  8  9  0  ]  /

             Y  O  U  X   '(   ")   W  D  C  V  Q  #$  @
             I  H  E  A   ,;   .:   R  T  S  N  Z      
             P  K  J  G   -_   ?!   L  B  F  M           
