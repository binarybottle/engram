# Engram Config for Karabiner

Engram layouts for Karabiner. 


```ts
  [{  1|  2=  3~  4+   5<   6>   7^  8&  9%  0*  ]}  
      bB  yY  oO  uU   '(   ")   lL  dD  wW  vV  zZ  #$  @`
     ⌃cC ⌥iI ⌘eE ⇧aA   ,;   .:  ⇧hH ⌘tT ⌥sS ⌃nN  qQ  
      gG  xX  jJ  kK   -_   ?!   rR  mM  fF  pP  /\
           ⌫              ␣           ⏎
```           


# Using Karabiner with Engram

To use the vanilla Engram layout on MacOS, simply

1. Install Karabiner `brew install karabiner-elements` (you'll have to grant necessary permissions in `System Settings`, detailed on the [Karabiner website](https://karabiner-elements.pqrs.org)).
2. Click this link to open the Engram layout [directly in Karabiner](https://smote.io/install_engram.html)

Or you can view the JSON [here](https://raw.githubusercontent.com/binarybottle/engram/master/install/mac/karabiner/engram.json) (you'll need to place the json file in `~/.config/karabiner/assets/complex_modifications/` and maybe restart Karabiner if you want to customize/ install manually).


## Using a karabiner.json Generator

This directory also includes [Karabiner.ts](https://github.com/evan-liu/karabiner.ts) config, as well as a [Goku](https://github.com/yqrashawn/GokuRakuJoudo) config.

Home Row Mods are working better in the Karabiner.ts config than the Goku one. (They're configured as simlayers in the Karabiner.ts version.) Karabiner.ts also 🏃🏻‍♂️s 53 times faster--73.6ms vs. 3.947s. 

The command keys are set to work more like they do on a mech ergo board.

Currently, Home Row Mods work only one at a time, but hoping to get that sorted shortly. 🤓

Karabiner still has some shortcomings. It seems like no matter how it's configured, typing rhythm isn't as natural with Karabiner as it is with [timeless Home Row Mods](https://github.com/urob/zmk-config#timeless-homerow-mods) in zmk using below config. 

```dtsi
    hrml: home_row_mod_left {
        compatible = "zmk,behavior-hold-tap";
        label = "HOME_ROW_MOD_LEFT";
        #binding-cells = <2>;
        flavor = "balanced";
        tapping-term-ms = <HM_TAPPING_TERM>;
        hold-trigger-key-positions = < KEYS_R THUMBS >;
        hold-trigger-on-release;
        bindings = <&kp>, <&kp>;
        };
```        


## Installing

### Karabiner.ts

1. Clone this repo.
2. cd to this subdirectory `cd engram/install/mac/karabiner`.
3. Create a profile in Karabiner called 'karabiner.ts'.
4. Run `deno task build` in the repo directory.

### Goku 

1. Clone this repository.
2. cd to this subdirectory `cd engram/install/mac/karabiner`.
3. Create a profile in Karabiner called 'goku'.
4. Install Goku `brew install yqrashawn/goku/goku`.
5. From the repo directory, copy the config file to your `.config` directory `cp karabiner.edn ~/.config`.
6. Run Goku `goku`