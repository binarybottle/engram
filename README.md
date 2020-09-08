# Arno's Engram key layout

The Engram layout is an optimal keyboard layout for touch typing in English:



                ~  !  =  ?  +  $  @  ^  &  %  *  <  >
                #  1  2  3  4  5  6  7  8  9  0  [  ]     

                   F  I  O  U  '  "  D  N  G  W  Q  -  /
                   C  H  E  A  ,  .  T  S  R  P  J        
                   Z  Y  X  V  (  )  L  M  K  B           


Shift accesses:

                   `    \    ;    :    {    }    |    _
                   '    "    ,    .    (    )    /    -


## Setup and data
  - **N-gram letter frequencies** (based on Google's book scanning project)
  - **Flow factors** (affecting transitions between ordered key pairs) <br>
    These factors are influenced by Dvorak's 11 criteria (1936)  
    that can be summarized as follows:
      - Alternate between hands and balance finger loads.
      - Avoid using the same finger.
      - Avoid the upper and lower rows.
      - Avoid skipping over the home row ("hurdling").
      - Avoid tapping adjacent rows ("reaching") with (same or) adjacent fingers.
  - **Finger strengths** (peak keyboard reaction forces, in newtons) <br>
      Based on  from <br>
      "Keyboard Reaction Force and Finger Flexor Electromyograms during Computer Keyboard Work" <br>
      BJ Martin, TJ Armstrong, JA Foulke, S Natarajan, Human Factors,1996,38(4),654-664.
  - **Speed** (unordered interkey stroke times in milliseconds) <br>
      "Estimation of digraph costs for keyboard layout optimization", <br>
      A Iseri, Ma Eksioglu, International Journal of Industrial Ergonomics, 48, 127-138, 2015. <br>
      Speed data were used for exploration of early key layouts.

## Engram criteria
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
  
## Summary of steps
  1. Optimize arrangement of the 12 most frequent letters in English across left and right sides.
  2. Fill in the rest of the left side with the most common command shortcut characters.
  3. Optimize arrangement of letters on the right side.
  4. Add punctuation, and characters above the number row.

### Step (1)
### Optimize arrangement of the 12 most frequent letters across left and right sides

Select the 12 most frequent letters in the English language 
(excluding C, which we group with other common command shortcut characters):

                   E, T, A, O, I, N, S, R, H, L, D, (C), U

Set an initial key position for E and T, the most common letters in English
(left and right middle finger home row positions), compute all 3,628,800
permutations of the remaining 10 letters, and determine an initial optimal
arrangement of these letters according to our (strengh, speed, and flow) criteria.
The resulting arrangement led to all vowels and H on the left:

                   -  I  O  U        D  N  L  -  - 
                   -  H  E  A        R  T  S  -  -
                   -  -  -  -        -  -  -  -

### Step (2)
### Fill in the rest of the left side with the most common command characters

The top-scoring arrangements for C,Y,Z,X,V include:

                   -  I  O  U
                   C  H  E  A
                   Z  Y  X  V

We choose this 5th place arrangement over 1st place
(which differ only by the order of Z and Y) because:

  - Z,Y,X,V is an extremely easy sequence to remember.
  - Z will be in the standard position, which is also easy to remember.
  - Undo (Z) & Redo (Y), and Cut (X) & Paste (V) are both common command sequences. 

For the final key on the left, we choose one of the most common command keys, F (find):

                   F  I  O  U
                   C  H  E  A
                   Z  Y  X  V

  - F's most common bigrams (OF, FO, IF, FI) would be on the same line.
  - Q is another option, but is the 2nd least frequent letter, 
      so should be relegated to a remote key location.

### Step (3)
### Optimize arrangement of letters on the right side

Include 6 of the 8 remaining letters (M, P, G, W, B, K)
and scramble letters on the right side in two stages.
First, scramble letters in pairs of rows to find which letters 
consistently score highest in the same locations:

                                     -  -  G  -
                                     T  S  -  -
                                     L  -  -  -
                                
Second, fix these four letters in place and find the highest-scoring of 40,320 permutations:

                   F  I  O  U        D  N  G  W
                   C  H  E  A        T  S  R  P
                   Z  Y  X  V        L  M  K  B

Place the 2nd and 3rd least frequent letters, J and Q, in the upper right:

                   F  I  O  U        D  N  G  W  Q
                   C  H  E  A        T  S  R  P  J 
                   Z  Y  X  V        L  M  K  B

### Step (4)
### Add punctuation, and characters above the number keys

                   1  2  3  4  5  6  7  8  9  0  {  }
      
                   F  I  O  U  '  "  D  N  G  W  Q  /  -
                   C  H  E  A  ,  .  T  S  R  P  J 
                   Z  Y  X  V  (  )  L  M  K  B   

Shift to access similar-looking characters above the numbers:


          ~        !  =  ?  +  $  @  ^  &  %  *  <  >
          #        1  2  3  4  5  6  7  8  9  0  [  ]     Back

        Tab        F  I  O  U  '  "  D  N  G  W  Q  -     /
        Cap        C  H  E  A  ,  .  T  S  R  P  J        Enter
        Shift      Z  Y  X  V  (  )  L  M  K  B           Shift

        Ctrl  Fn  Cmd  Alt  Space   Alt  Ctrl       Arrows


Shift to access less common, but similar-meaning punctuation:

          ~    `    \    ;    :    {    }    |    _
          #    '    "    ,    .    (    )    /    -

Rationale for shift-characters:
- **#**  The pound/hash represents numbers, and sits to the left of the number keys.
- **~**  The tilde has several meanings, including "approximately equal to" 
   (here "similar-looking" to the numbers), is used as command-line shorthand 
   for the home directory (appropriate for upper left below the Escape key), 
   and is in the same position as the standard QWERTY key layout.

- **'**  Single quotation marks are used to quote text for 'emphasis',
   or to quote text within a quote.
- **`**  One use of the backquote (or backtick, or grave accent) is to quote computer code.
   In computer programming, it is used in an analogous manner as a single quote within
   a quote, to quote code within code for command substitution (to replace a command with output).

- **"**  Double quotation marks are "usually used to quote direct speech", or so they say.
- **\**  The backslash is an escape character used to quote special characters in regular expressions.

- **,**  The comma is used to separate text, for example in lists, or to provide a pause.
- **;**  The semicolon provides a stronger separation or pause; it can be used in place 
   of the comma to separate items in a list, especially if those items contain commas.
   It can also be used to end a line of code in some programming languages.
   
- **.**  The period ends a sentence.
- **:**  The colon similarly ends a statement but precedes something following:
   an explanation, a description, a quotation, a list, etc.

- **|**  The pipe connects commands in computer code.
- **/**  In addition to its use in mathematics, the slash connects 
   conjunctions/disjunctions/alternatives, or locations such as file paths or urls.

- **-**  The dash connects side-by-side words, or can surround a phrase for emphasis.
- **_**  The underscore connects strings within variable or file names, 
   or can _underline a phrase_ for emphasis.
