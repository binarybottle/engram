# Arno's Engram key layout

Engram is a key layout optimized for comfortable and efficient touch typing in English 
created by [Arno Klein](https://binarybottle.com), 
with [open source code](https://github.com/binarybottle/engram) to create other optimized key layouts.
You can install the Engram layout on [Windows, macOS, and Linux](https://keyman.com/keyboards/engram)
or [try it out online](https://keymanweb.com/#en,Keyboard_engram).

Letters are optimally arranged according to a scoring model that reflects ergonomic factors that promote reduction of lateral finger movements and increase in efficient typing of high-frequency letter pairs: 

             Y  O  U  X            W  D  C  V  Q 
             I  H  E  A            R  T  S  N  Z      
             P  K  J  G            L  B  F  M             

Punctuation marks are logically grouped together in the middle columns (accessed by the Shift and R-Alt keys) and numbers are paired with mathematical and logic symbols (accessed by the Shift Key):

          $  -  =  ~  +   <    >   /  &  %  *  ^  `
          #  1  2  3  4   5    6   7  8  9  0  |  \

             Y  O  U  X  ([{  )]}  W  D  C  V  Q 
             I  H  E  A  ,;:  .?!  R  T  S  N  Z      
             P  K  J  G  "#@  '-_  L  B  F  M             

See below for a full description and comparisons with other key layouts.

<!-- ### Default
![Default state](https://github.com/binarybottle/engram/blob/master/assets/FIXengram-base-layer.png?raw=true)
### Shift
![Shift state](https://github.com/binarybottle/engram/blob/master/assets/FIXengram-shift-layer.png?raw=true)
### Ctrl
![R-Alt state](https://github.com/binarybottle/engram/blob/master/assets/FIXengram-ralt-layer.png?raw=true)
[Keyboard images care of [Keyman Developer](https://keyman.com/developer/).]
-->

(c) 2021 Arno Klein, MIT license

----------------

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

Despite the fact that the Engram layout was designed to reduce strain and discomfort, not specifically to increase speed or reduce finger travel from the home row, it scores higher than all other key layouts (Colemak, Dvorak, QWERTY, etc.) for some large, representative, publicly available data (all text sources are listed below and available on [GitHub](https://github.com/binarybottle/text_data)). Below are tables of different prominent key layouts scored using the Engram Scoring Model (detailed below), and generated by the online [Keyboard Layout Analyzer](http://patorjk.com/keyboard-layout-analyzer/):
> The optimal layout score is based on a weighted calculation that factors in the distance your fingers moved (33%), how often you use particular fingers (33%), and how often you switch fingers and hands while typing (34%).

#### Engram Scoring Model scores for existing layouts based on publicly available text data
    
| Layout | Google bigrams | Alice | 100K tweets | 20K tweets | MASC tweets | MASC spoken | COCA blogs | Google | Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Engram | 0.02483 | 0.01933 | 0.03281 | 0.02958 | 0.02770 | 0.01829 | 0.02468 | 0.04331 | 0.02718 |
| Halmak2.2 | 0.02465 | 0.01924 | 0.03282 | 0.02951 | 0.02765 | 0.01826 | 0.02455 | 0.04342 | 0.02705 |
| Norman | 0.02416 | 0.01899 | 0.03224 | 0.02892 | 0.02709 | 0.01798 | 0.02409 | 0.04201 | 0.02653 |
| MTGAP Shifted | 0.02426 | 0.01899 | 0.03219 | 0.02886 | 0.02722 | 0.01794 | 0.02419 | 0.04130 | 0.02624 |
| Workman | 0.02445 | 0.01906 | 0.03251 | 0.02924 | 0.02742 | 0.01804 | 0.02431 | 0.04277 | 0.02687 |
| QGMLWB | 0.02324 | 0.01830 | 0.03116 | 0.02811 | 0.02601 | 0.01738 | 0.02320 | 0.04094 | 0.02545 |
| Colemak Mod-DH | 0.02421 | 0.01876 | 0.03213 | 0.02876 | 0.02713 | 0.01783 | 0.02407 | 0.04216 | 0.02674 |
| Colemak | 0.02431 | 0.01881 | 0.03229 | 0.02888 | 0.02724 | 0.01790 | 0.02418 | 0.04221 | 0.02703 |
| ASSET | 0.02371 | 0.01831 | 0.03170 | 0.02836 | 0.02676 | 0.01743 | 0.02365 | 0.04188 | 0.02652 |
| Capewell-Dvorak | 0.02383 | 0.01860 | 0.03177 | 0.02844 | 0.02670 | 0.01768 | 0.02374 | 0.04141 | 0.02620 |
| Dvorak | 0.02363 | 0.01847 | 0.03148 | 0.02831 | 0.02640 | 0.01760 | 0.02355 | 0.04101 | 0.02596 |
| QWERTY | 0.02133 | 0.01684 | 0.02879 | 0.02580 | 0.02404 | 0.01581 | 0.02133 | 0.03793 | 0.02401 |

#### Keyboard Layout Analyzer scores for existing layouts based on publicly available text data
    
| Layout | Alice | 100K tweets | 20K tweets | MASC tweets | MASC spoken | COCA blogs | Google | Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Engram | 67.51 | 61.20 | 55.18 | 57.10 | 61.13 | 57.10 | 34.39 | 45.91 |
| Halmak2.2 | - | - | --- | --- | --- | --- | --- | --- |
| Norman | 62.76 | - | --- | --- | --- | --- | --- | --- |
| MTGAP Shifted | 69.73 | - | --- | --- | --- | --- | --- | --- | 
| Workman | 64.78 | - | --- | --- | --- | --- | --- | --- | 
| QGMLWB | - | - | --- | --- | --- | --- | --- | --- | 
| Colemak Mod-DH | - | - | --- | --- | --- | --- | --- | --- | 
| Colemak | 65.83 | 60.67 | 54.97 | 57.04 | 61.36 | 57.04 | 31.48 | 48.65 | 
| ASSET | 64.60 | - | --- | --- | --- | --- | --- | --- | 
| Capewell-Dvorak | 63.40 | - | --- | --- | --- | --- | --- | --- | 
| Dvorak | 65.86 | 60.93 | 55.56 | 56.59 | 62.75 | 56.59 | 28.85 | 45.55 | 
| QWERTY | 53.06 | - | --- | --- | --- | --- | --- | --- | 

---
    
| Text source | Information |
| --- | --- |
| "Alice" | [Analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/mN0CTbZ3) of Alice in Wonderland (Ch.1), a standard text used for comparing layouts |
| "100K tweets" | The first 100,000 tweets from: [Sentiment140 dataset](https://data.world/data-society/twitter-user-data) training data [Go, A., Bhayani, R. and Huang, L., 2009. Twitter sentiment classification using distant supervision. CS224N Project Report, Stanford, 1(2009), p.12.] |
| "20K tweets" | All 20,000 tweets from [Gender Classifier Data](https://www.kaggle.com/crowdflower/twitter-user-gender-classification) (Added: November 15, 2015 by CrowdFlower) |
| "MASC tweets" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/fv3Cj2zQ) of [MASC](http://www.anc.org/data/masc/corpus/) tweets (cleaned of html markup) |
| "MASC spoken" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/CvHXTg7n) of [MASC](http://www.anc.org/data/masc/corpus/) spoken transcripts (phone and face-to-face: 25,783 words) |
| "COCA blogs" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/fv3Cj2zQ) of [Corpus of Contemporary American English](https://www.english-corpora.org/coca/) [blog samples](https://www.corpusdata.org/) with hundreds of thousands of words (cleaned of html markup) |
| "Google" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/CtwvHjM5) of the [Google home page](https://google.com) (accessed 10/20/2020) |
| "Code" | [KLA analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/szdpfS3K) of the "Tower of Hanoi" (programming languages A-Z compiled from [Rosetta Code](https://rosettacode.org/wiki/Towers_of_Hanoi)) |

| Layout | Year | Website |
| --- | --- | --- |
| Engram | 2020 | https://engram.dev |
| Halmak2.2 | 2016 | https://github.com/MadRabbit/halmak |
| Norman | 2013 | https://normanlayout.info/ |
| MTGAP Shifted | 2012 | https://mathematicalmulticore.wordpress.com/category/keyboards/ |
| Workman | 2010 | https://workmanlayout.org/ | 
| QGMLWB | 2009 | http://mkweb.bcgsc.ca/carpalx/?full_optimization | 
| Colemak Mod-DH | 2017 | https://colemakmods.github.io/mod-dh/ | 
| Colemak | 2006 | https://colemak.com/ | 
| ASSET | 2006 | http://millikeys.sourceforge.net/asset/ | 
| Capewell-Dvorak | 2004 | http://michaelcapewell.com/projects/keyboard/layout_capewell-dvorak.htm |
| Dvorak | 1936 | https://en.wikipedia.org/wiki/Dvorak_keyboard_layout | 
| QWERTY | 1873 | https://en.wikipedia.org/wiki/QWERTY |


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

- [Step 1: Define the shape of the key layout to minimize lateral finger movements](#step1)
- [Step 2: Arrange the most frequent letters based on comfort and bigram frequencies](#step2)
- [Step 3: Optimize assignment of the remaining letters](#step3)
- [Step 4: Stability tests](#step4)
- [Step 5: Arrange non-letter characters in easy-to-remember places](#step5)

### Step 1: Define the shape of the key layout to minimize lateral finger movements  <a name="step1">

We will assign 24 letters to 8 columns of keys separated by two middle columns reserved for punctuation. These 8 columns require no lateral finger movements when touch typing, since there is one column per finger. The most comfortable keys include the left and right home rows (keys 5-8 and 17-20), the top-center keys (2,3 and 14,15) that allow the longer middle and ring fingers to uncurl upwards, as well as the bottom corner keys (9,12 and 21,24) that allow the shorter fingers to curl downwards. We will assign the two least frequent letters, Z and Q, to the two hardest-to-reach keys lying outside the 24-key columns in the upper right:

        Left:            Right:
     1  2  3  4       13 14 15 16  Q/Z
     5  6  7  8       17 18 19 20  Z/Q
     9 10 11 12       21 22 23 24

### Step 2: Arrange the most frequent letters based on comfort and bigram frequencies  <a name="step2">

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

### Step 3: Optimize assignment of the remaining letters <a name="step3">
    
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

    
### Step 4: Stability Tests <a name="step4">
    
We will run three types of stability tests on the 8 winning layouts:
    1. Exchange letters in rows
    2. Compare effects of Flow, Strength, and/or Speed matrices
    3. Reset parameters

It is clear from the results of all of the tests above that one layout consistently scores at the top, and we will accept this as the winning layout. Since the middle row spells "I HEARTS N" we'll put Z to the right for "I HEARTS NZ" (for New Zealand) so that it is easy to remember, and place the Q above:

             Y  O  U  X     W  D  C  V  Q 
             I  H  E  A     R  T  S  N  Z      
             P  K  J  G     L  B  F  M             
    
Our arrangement of letters is complete!
    
### Step 5. Arrange non-letter characters in easy-to-remember places  <a name="step5">

Now that we have all 26 letters accounted for, we turn our attention to non-letter characters, taking into account frequency of punctuation and ease of recall.
    
#### Frequency of punctuation 

These sources helped guide our arrangement:
    
  - "Punctuation Input on Touchscreen Keyboards: Analyzing Frequency of Use and Costs" <br>
    S Malik, L Findlater - College Park: The Human-Computer Interaction Lab. 2013 <br>
    https://www.cs.umd.edu/sites/default/files/scholarly_papers/Malik.pdf

  - "Frequencies for English Punctuation Marks" by Vivian Cook <br>
    http://www.viviancook.uk/Punctuation/PunctFigs.htm

  - "Computer Languages Character Frequency" <br>
    Xah Lee. Date: 2013-05-23. Last updated: 2020-06-29. <br>
    http://xahlee.info/comp/computer_language_char_distribution.html

#### Add punctuation keys and number keys

We will place the most common punctuation marks in the middle columns: 
**( ,  .  '  "  ;  :  -  _ )** 

             Y  O  U  X  (    )    W  D  C  V  Q 
             I  H  E  A  ,    .    R  T  S  N  Z      
             P  K  J  G  '    "    L  B  F  M             

We will use the Shift and R-Alt keys to group similar punctuation marks:

             Y  O  U  X  ([{  )]}  W  D  C  V  Q 
             I  H  E  A  ,;:  .?!  R  T  S  N  Z      
             P  K  J  G  "#@  '-_  L  B  F  M             
    
([{ )]} 
&nbsp;&nbsp;&nbsp;&nbsp;
Brackets: parentheses, square brackets, curly brackets (angle brackets are placed in the two number keys directly above).  

, ; : 
&nbsp;&nbsp;&nbsp;&nbsp;
Separating marks: the comma separates text, for example in lists; the semicolon can be used in place of the comma to separate items in a list (especially if these items contain commas); the colon ends one statement but precedes the following: an explanation, quotation, list, etc. 

. ? ! 
&nbsp;&nbsp;&nbsp;&nbsp;
Ending marks: the period, question mark, and exclamation mark end a sentence.

" # @ 
&nbsp;&nbsp;&nbsp;&nbsp;
Identifying characters: double quotation marks are for direct quotations from an identified source; the hashtag is a popular modern use of the pound/hash sign to identify digital content on a specific topic; the "at sign" identifies a location or affiliation (such as in email addresses), and acts as a "handle" to identify users in popular social media platforms and online forums.   

' - _ 
&nbsp;&nbsp;&nbsp;&nbsp;
Joining characters: the apostrophe joins words as contractions; the hyphen joins words as compounds; the underscore joins words in cases where whitespace characters are not permitted (such as in variables or file names). 

For the number keys, we will have the Shift key access mathematical and logic symbols:
    
          $  -  =  ~  +   <    >   /  &  %  *  ^
          #  1  2  3  4   5    6   7  8  9  0  |

\# $ 
&nbsp;&nbsp;&nbsp;&nbsp;
The pound/hash (duplicate) represents numbers and is set next to the number keys; the dollar sign signifies additional symbols ("S").

\-  =  ~  +   <    >   \/  &  %  * &nbsp;&nbsp;&nbsp;&nbsp; 

    1: - (minus/hyphen: 1 stroke, like the Chinese character for "1")
    2: = (equal: 2 strokes, like the Chinese character for "2")
    3: ~ (tilde: "almost equal", often written with 3 strokes, like the Chinese character for "3")
    4: + (plus: has four quadrants; resembles "4")
    5 & 6: < > ("less/greater than"; these angle brackets are directly above the other bracket keys)
    7: / (forward slash: for division; resembles "7")
    8: & (ampersand: logical AND operator; resembles "8")
    9: % (percent: related to division; resembles "9")
    0: * (asterisk: for multiplication; resembles "0")

| ^
&nbsp;&nbsp;&nbsp;&nbsp;
The vertical bar or "pipe" represents the logical OR operator; the caret represents the logical XOR operator, as well as exponentiation.

Use of the Shift and R-Alt keys enables easy access to the most common punctuation marks in the middle columns, and it also frees up the three remaining keys in many common keyboards (flanking the upper right hand corner Backspace key). These three keys excessively stretch the right little finger, and are displaced in special ergonomic keyboards, such as the Kinesis Advantage and Ergodox. So for two of these keys, we will simply repeat the use of four of punctuation marks that are accessed in the middle columns by the R-Alt key (: ! and @ _). For the final (top rightmost) key, we will assign to it the two remaining symbols, used primarily by computer programmers:

\\ \` 
&nbsp;&nbsp;&nbsp;&nbsp;
The backslash is often used as an escape character or to enclose regular expressions to process text; the backtick processes an enclosed string as part of a computer command (command substitution) or indicates code in comments.

The resulting Engram layout:

          $  -  =  ~  +   <    >   /  &  %  *  ^  `
          #  1  2  3  4   5    6   7  8  9  0  |  \

             Y  O  U  X  ([{  )]}  W  D  C  V  Q 
             I  H  E  A  ,;:  .?!  R  T  S  N  Z      
             P  K  J  G  "#@  '-_  L  B  F  M             
