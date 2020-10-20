# Arno's Engram key layout

The [Engram layout](https://github.com/binarybottle/engram-layout) is a keyboard layout optimized for comfortable touch typing in English created by [Arno Klein](https://binarybottle.com), with open source code to create other optimized key layouts.

             Y  G  U  K            B  L  D  F
             I  O  E  A            R  T  S  N
             V  Z  X  C            H  W  P  M

The Shift (and Alt) key accesses (capital letters), less common punctuation, and characters that look similar to the numbers. Swapping the Backspace and Caps lock keys completes the layout:

          ^  !  ?  <  +   $    @   >  &  %  *  ~  \
          #  1  2  3  4   5    6   7  8  9  0  =  /    Caps

    Tab      Y  G  U  K  '-   "_   B  L  D  F  Q  #`  @|
    Back     I  O  E  A  ,;   .:   R  T  S  N  J      Enter
    Shift    V  Z  X  C  ([{  )]}  H  W  P  M         Shift

    Ctrl  Fn  Cmd  Alt    Space     Alt   Ctrl       Arrows    
    

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

Despite the fact that the Engram layout was designed to reduce strain and discomfort, not specifically to increase speed or reduce finger travel from the home row, it scores higher than all other key layouts (Colemak, Dvorak, QWERTY, etc.) for some large, representative, publicly available data, according to the online [Keyboard Layout Analyzer](http://patorjk.com/keyboard-layout-analyzer/):

> The optimal layout score is based on a weighted calculation that factors in the distance your fingers moved (33%), how often you use particular fingers (33%), and how often you switch fingers and hands while typing (34%).

[Analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/mN0CTbZ3) 
    of the first chapter of __Alice in Wonderland__, a standard text used for comparing layouts:
    
    #1 Engram 67.51
    #2 Programmer Dvorak 66.11
    #3 Simplified Dvorak 65.86
    #4 Colemak 65.83
    #5 Personalized 56.01
    #6 AZERTY 49.54

The first __100,000 tweets__ from: [Sentiment140 dataset](https://data.world/data-society/twitter-user-data) training data <br>
Go, A., Bhayani, R. and Huang, L., 2009. <br>
Twitter sentiment classification using distant supervision. <br>
CS224N Project Report, Stanford, 1(2009), p.12.

    #1 Engram 61.20
    #2 Programmer Dvorak 61.11
    #3 Simplified Dvorak 60.93
    #4 Colemak 60.67
    #5 Personalized 56.60
    #6 AZERTY 46.26

All __20,000 tweets__ from [Gender Classifier Data](https://www.kaggle.com/crowdflower/twitter-user-gender-classification) <br>
Added: November 15, 2015 by CrowdFlower

    #1 Simplified Dvorak 55.56
    #2 Engram 55.18
    #3 Programmer Dvorak 55.08
    #4 Colemak 54.97
    #5 Personalized 49.02
    #6 AZERTY 42.35

[Analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/fv3Cj2zQ) of [MASC](http://www.anc.org/data/masc/corpus/) tweets (cleaned of html markup):

    #1 Engram 57.10
    #2 Colemak 57.04
    #3 Simplified Dvorak 56.59
    #4 Programmer Dvorak 56.24
    #5 Personalized 49.74
    #6 AZERTY 42.43
    
[Analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/CvHXTg7n) of [MASC](http://www.anc.org/data/masc/corpus/) spoken transcripts (phone and face-to-face: 25,783 words):

    #1 Simplified Dvorak 62.75
    #2 Programmer Dvorak 62.72
    #3 Colemak 61.36
    #4 Engram 61.13
    #5 Personalized 57.05
    #6 AZERTY 48.26

[Analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/fv3Cj2zQ) of [Corpus of Contemporary American English](https://www.english-corpora.org/coca/) [blog samples](https://www.corpusdata.org/) with hundreds of thousands of words (cleaned of html markup):
    
    #1 Engram 57.10
    #2 Colemak 57.04
    #3 Simplified Dvorak 56.59
    #4 Programmer Dvorak 56.24
    #5 Personalized 49.74
    #6 AZERTY 42.43

[Analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/CtwvHjM5) of the [Google home page](google.com) (accessed 10/20/2020): 

    #1 Engram 34.39
    #2 Programmer Dvorak 32.95
    #3 AZERTY 31.71
    #4 Colemak 31.48
    #5 Simplified Dvorak 28.85
    #6 Personalized 27.80

[Analysis](http://patorjk.com/keyboard-layout-analyzer/#/load/szdpfS3K) of the "Tower of Hanoi" (programming languages A-Z compiled from [Rosetta Code](https://rosettacode.org/wiki/Towers_of_Hanoi) in [SteveP's fork of Patrick's Keyboard Layout Analyzer](https://stevep99.github.io/keyboard-layout-analyzer/#/main)):

    #1 Colemak 48.65
    #2 Programmer Dvorak 47.10
    #3 Engram 45.91
    #4 Simplified Dvorak 45.55
    #5 Personalized 44.58
    #6 AZERTY 36.27

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

- [Step 1: Define the shape of the key layout to minimize lateral finger movements](#step1)
- [Step 2: Assign command shortcut letters to the bottom left row](#step2)
- [Step 3: Arrange the most frequent letters based on comfort and bigram frequencies](#step3)
- [Step 4: Optimize assignment of the remaining letters](#step4)
- [Step 5: Arrange non-letter characters in easy-to-remember places](#step5)

### 1: Define the shape of the key layout to minimize lateral finger movements  <a name="step1">

We will assign 24 letters to 8 columns of keys separated by two middle columns reserved for punctuation. These 8 columns require no lateral finger movements when touch typing, since there is one column per finger. The most comfortable keys include the left and right home rows (keys 5-8 and 17-20), the top-center keys (2,3 and 14,15) that allow the longer middle and ring fingers to uncurl upwards, as well as the bottom corner keys (9,12 and 21,24) that allow the shorter fingers to curl downwards. We will reserve the bottom left row (keys 9-12) for common command shortcut letters (Z,X,C,V), and will reserve the two hardest-to-reach keys lying outside the 24-key columns in the upper right to the two least frequent remaining letters, Q and J:

        Left:            Right:
     1  2  3  4       13 14 15 16  Q
     5  6  7  8       17 18 19 20  J
    [9 10 11 12]      21 22 23 24

### 2: Assign command shortcut letters to the bottom left row  <a name="step2">

We begin by assigning the common command letters V,Z,X,C to the bottom left row. We place V and Z to the left of X and C, because V and Z are often repeated (to paste multiple times or to undo multiple mistakes) whereas C and X are not (the copy and cut buffers are overwritten), and should lie closer to the Ctrl/Cmd key for ease of access with one hand. V and C are assigned to the most comfortable of the four keys (as noted above) because they are more frequent letters in English than Z and X.

     -  -  -  -        -  -  -  -
     -  -  -  -        -  -  -  -
     V  Z  X  C        -  -  -  -

### 3: Arrange the most frequent letters based on comfort and bigram frequencies  <a name="step3">

In prior experiments using the methods below, all vowels automatically clustered together, with the most frequent letters assigned to the strongest fingers (in order: middle, index, ring, little), and the letter Y consistently landed in the top left key for the highest-scoring layouts. Below, we will arrange vowels to the left side and the most frequent consonants to the right side to encourage balance and alternation across hands.
    
#### Vowels
    
**E**, T, **A, O, I**, N, S, R, H, L, D, [C], **U**, M, F, P, G, W, **Y**, B, [V], K, [X], J, Q, [Z]

We will assign the four most frequent vowels (E,A,O,I) to the most comfortable keys in the left home and upper rows (keys 5-8 and 2-3), with the letter E, the most frequent in the English language, assigned to either of the strongest keys (7 and 8, the middle and index fingers on the left home row). The letter U may also take the less comfortable key 4. We will arrange the vowels such that any top-frequency bigram (more than 1 billion instances in Peter Norvig's analysis of Google data) reads from left to right (ex: TH, not HT) for ease of typing (roll-in from little to index finger vs. roll-out from index to little finger). These constraints lead to comfortable and efficient layouts:
    
    Y  O  U  -
    I  -  E  A    

    Y  -  U  - 
    I  O  E  A      

    Y  -  -  U 
    I  O  E  A      

    Y  -  O  U   
    I  -  E  A    

    Y  -  O  U   
    -  I  E  A    

    Y  I  O  U    
    -  -  E  A     

#### Consonants

Next, to populate the home row on the right side, we examine all possible sequences of four letters from the seven most frequent consonants (T,N,S,R,H,L,D):

E, **T**, A, O, I, **N, S, R, H, L, D**, [C], U, M, F, P, G, W, Y, B, [V], K, [X], J, Q, [Z]

These seven consonants are included in the highest frequency bigrams listed below, with more than 1 billion instances in Peter Norvig's analysis:

**TH, ND, ST, NT, NS, TR, RS**, (RT), SH, LD, RD, LS, DS, LT, (TL), RL, HR, NL, (SL)

To maximize the number of bigrams we can comfortably type, we select 4-consonant sequences that consist of three consecutive highest frequency bigrams, such as NSTR = NS + ST + TR. We also restrict T and R to the strongest (middle or index) fingers, because T is the most frequent consonant, and the letter R needs to be preceded by other consonants to comfortably type frequent bigrams (TR,DR,HR,PR,FR,BR,GR, etc.) by rolling in from little-to-index finger.

    N  S  T  R
    N  L  T  R
    D  S  T  R    
    N  S  T  H
    N  L  T  H    
    L  S  T  H    
    D  S  T  H    
    N  L  S  T      
    N  D  S  T    
    L  D  S  T    
    
When reordered from right-to-left for ease of typing with the right hand, we have 10 consonant sequences:
RTSN, RTLN, RTSD, HTSN, HTLN, HTSL, HTSD, TSLN, TSDN, TSDL. The resulting 6 arrangements of five vowels on the left and 10 arrangements of four consonants on the right gives us 60 possible layouts, each with 10 unassigned keys:

      Left hand         Right hand
    YOU- I-EA VZXC    ---- RTSN ----
    YOU- I-EA VZXC    ---- RTLN ----
    YOU- I-EA VZXC    ---- RTSD ----
    YOU- I-EA VZXC    ---- HTSN ----
    YOU- I-EA VZXC    ---- HTLN ----
    YOU- I-EA VZXC    ---- HTSL ----
    YOU- I-EA VZXC    ---- HTSD ----
    YOU- I-EA VZXC    ---- TSLN ----
    YOU- I-EA VZXC    ---- TSDN ----
    YOU- I-EA VZXC    ---- TSDL ----

    Y-U- IOEA VZXC    ---- RTSN ----
    Y-U- IOEA VZXC    ---- RTLN ----
    Y-U- IOEA VZXC    ---- RTSD ----
    Y-U- IOEA VZXC    ---- HTSN ----
    Y-U- IOEA VZXC    ---- HTLN ----
    Y-U- IOEA VZXC    ---- HTSL ----
    Y-U- IOEA VZXC    ---- HTSD ----
    Y-U- IOEA VZXC    ---- TSLN ----
    Y-U- IOEA VZXC    ---- TSDN ----
    Y-U- IOEA VZXC    ---- TSDL ----

    Y--U IOEA VZXC    ---- RTSN ----
    Y--U IOEA VZXC    ---- RTLN ----
    Y--U IOEA VZXC    ---- RTSD ----
    Y--U IOEA VZXC    ---- HTSN ----
    Y--U IOEA VZXC    ---- HTLN ----
    Y--U IOEA VZXC    ---- HTSL ----
    Y--U IOEA VZXC    ---- HTSD ----
    Y--U IOEA VZXC    ---- TSLN ----
    Y--U IOEA VZXC    ---- TSDN ----
    Y--U IOEA VZXC    ---- TSDL ----
    
    Y-OU I-EA VZXC    ---- RTSN ----
    Y-OU I-EA VZXC    ---- RTLN ----
    Y-OU I-EA VZXC    ---- RTSD ----
    Y-OU I-EA VZXC    ---- HTSN ----
    Y-OU I-EA VZXC    ---- HTLN ----
    Y-OU I-EA VZXC    ---- HTSL ----
    Y-OU I-EA VZXC    ---- HTSD ----
    Y-OU I-EA VZXC    ---- TSLN ----
    Y-OU I-EA VZXC    ---- TSDN ----
    Y-OU I-EA VZXC    ---- TSDL ----

    Y-OU -IEA VZXC    ---- RTSN ----
    Y-OU -IEA VZXC    ---- RTLN ----
    Y-OU -IEA VZXC    ---- RTSD ----
    Y-OU -IEA VZXC    ---- HTSN ----
    Y-OU -IEA VZXC    ---- HTLN ----
    Y-OU -IEA VZXC    ---- HTSL ----
    Y-OU -IEA VZXC    ---- HTSD ----
    Y-OU -IEA VZXC    ---- TSLN ----
    Y-OU -IEA VZXC    ---- TSDN ----
    Y-OU -IEA VZXC    ---- TSDL ----
    
    YIOU --EA VZXC    ---- RTSN ----
    YIOU --EA VZXC    ---- RTLN ----
    YIOU --EA VZXC    ---- RTSD ----
    YIOU --EA VZXC    ---- HTSN ----
    YIOU --EA VZXC    ---- HTLN ----
    YIOU --EA VZXC    ---- HTSL ----
    YIOU --EA VZXC    ---- HTSD ----
    YIOU --EA VZXC    ---- TSLN ----
    YIOU --EA VZXC    ---- TSDN ----
    YIOU --EA VZXC    ---- TSDL ----
    
### 4: Optimize assignment of the remaining letters  <a name="step4">

We will assign missing letters to the above layouts by scoring every possible arrangement of these 10 letters and selecting the top-scored arrangement. Since there are 3,628,800 (10 factorial) possible permutations for 10 letters, and we have 60 possible layouts each with 10 missing letters, we need to score and evaluate 217,728,000 permutations.  
    
To score each arrangement of letters, we construct a frequency matrix of each ordered pair of letters (bigram), and multiply this frequency matrix by our speed-strength-flow matrix to compute a score. 
    
The 10 missing letters in each layout are among those in bold below:

E, T, A, O, I, N, **S, R, H, L, D**, C, U, **M, F, P, G, W**, Y, **B**, V, **K**, X, J, Q, Z    

#### **Scoring details**
    
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

#### **Scoring results**

We obtain 60 layouts, where each represents the top-scoring layout for one of the 60 vowel/consonant initializations above, and are the result of computing scores for 217,728,000 letter permutations. 
    
Top 10 layouts as lists:

    L: upper L: home  L:lower  R: upper R: home  R:lower
    Y,G,U,K, I,O,E,A, V,Z,X,C, B,L,D,F, R,T,S,N, H,W,P,M
    Y,O,U,K, I,H,E,A, V,Z,X,C, W,D,G,F, R,T,S,N, L,B,P,M
    Y,P,O,U, H,I,E,A, V,Z,X,C, W,D,G,K, R,T,S,N, L,B,F,M
    Y,G,U,K, I,O,E,A, V,Z,X,C, B,L,D,W, H,T,S,N, R,F,P,M
    Y,P,O,U, I,H,E,A, V,Z,X,C, W,D,G,K, R,T,S,N, L,B,F,M
    Y,O,U,K, I,H,E,A, V,Z,X,C, G,D,R,F, T,S,L,N, M,B,W,P
    Y,G,P,U, I,O,E,A, V,Z,X,C, K,D,L,B, R,T,S,N, H,W,F,M
    Y,P,O,U, H,I,E,A, V,Z,X,C, G,D,R,B, T,S,L,N, M,K,W,F
    Y,O,U,K, I,H,E,A, V,Z,X,C, G,D,M,B, R,T,L,N, S,W,F,P
    Y,O,U,K, I,H,E,A, V,Z,X,C, G,R,P,F, T,S,D,N, L,W,B,M
    
  - Vacancies in the left upper row were filled with G or P for center fingers and K for the index finger.
  - Every winner's left home row that had to fill a vacancy did so with an H.
  - Of the winners' right home rows, all have T and N, all but one have T, S, and N, and half are identical (R,T,S,N), including for 1st, 2nd, and 3rd places.
    
We then test the robustness of order of the scores for the top 10 layouts:
    
Test set 1: Ignore Strength, Flow, and/or Speed matrices:

  - Flow and Strength (not Speed) matrices
  - Flow and Speed (not Strength) matrices
  - Only Speed matrix
  - Only Flow matrix

Test set 2: Reset parameters and rescore:
    
  - Set all parameters equal
  - Set all parameters equal and include the Speed matrix
  - Strongly penalize same-finger bigrams or home-row skips

It is clear from the results of all of the tests above that the 1st place layout consistently scores at the top, and we will accept this as the winning layout:

    Y  G  U  K        B  L  D  F
    I  O  E  A        R  T  S  N
    V  Z  X  C        H  W  P  M
    
### 5. Arrange non-letter characters in easy-to-remember places  <a name="step5">

Now that we have all 26 letters accounted for, we turn our attention to non-letter characters, taking into account frequency of punctuation and ease of recall.
    
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

**Add punctuation keys and number keys**

We will have the Shift-key access characters that look similar to the numbers:

             !  ?  <  +  $  @  >  &  %  *
             1  2  3  4  5  6  7  8  9  0

We will place the most common punctuation in the middle columns (without moving the number keys):

             .  ,  ;  :  -  _  "  '  (  ) 

Finally, we will also swap the Backspace and Caps keys:

          ^  !  ?  <  +   $    @   >  &  %  *  ~  \
          #  1  2  3  4   5    6   7  8  9  0  =  /    Caps

    Tab      Y  G  U  K  '-   "_   B  L  D  F  Q  #`  @|
    Back     I  O  E  A  ,;   .:   R  T  S  N  J      Enter
    Shift    V  Z  X  C  ([{  )]}  H  W  P  M         Shift

**Rationale for shift-characters**

**# ^** &nbsp;&nbsp; The pound/hash represents numbers, and is set next the number keys, while the caret indicates a superscript for characters accessible by the Shift-key.

**= ~** &nbsp;&nbsp; The equal sign means "equal to" and the tilde can mean "approximately equal to" (here "similar-looking" to the numbers).

**/ \\** &nbsp;&nbsp; The slash and backslash are a natural pair.

**' -** &nbsp;&nbsp; The apostrophe joins words as contractions while the hyphen joins words as compounds. As a single quotation mark and a spaced en dash, respectively, each can also set off a phrase for emphasis or as a parenthetical.

**" \_** &nbsp;&nbsp; "Double quotation marks can set off a quotation or phrase or title, and the underscore can \_underline a phrase\_ for emphasis or as a title.

**, ;** &nbsp;&nbsp; The comma is used to separate text, for example in lists; the semicolon can be used in place of the comma to separate items in a list.

**. :** &nbsp;&nbsp; The period ends a sentence. The colon similarly ends a statement but precedes something following: explanation, quotation, list, etc.

**([{ )]}** &nbsp;&nbsp; The different brackets naturally go together. Parentheses are more frequently used than square brackets, and the Alt-key can access curly brackets, which are commonly used by programmers.  

**# \`** &nbsp;&nbsp; The hashtag (repeat of the pound/hash sign above) is a metadata tag used in social networks to process/find message strings, while the backtick can be used to process/evaluate a string as part of a general command.

**@ |** &nbsp;&nbsp; The "at sign" (duplicate from the "6" key for ease of access) can be used as a handle in social media to direct the flow of information, and a vertical line or "pipe" can be used to direct the output of a computer command.
