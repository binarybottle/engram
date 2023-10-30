# KMonad and Engram

[KMonad](https://github.com/kmonad/kmonad), **the onion of keyboard management**, is a cross platform keyboard management tool. It's `.kbd` config files are concise and easy to read and alter. 

The example configs in this directory are laid out for a MacBook/Air/Pro keyboard, but could easily be adapted or used as a starting point to configure Engram on Linx or Windows as well. KMonad makes trivial work of home row mods. It is fast and easy to work with and may become your preferred way of changing layouts.

Follow [this gist](https://gist.github.com/amiorin/4c74f63fe599a1dcbd0933628df1aac9) by @amiorin to build KMonad. You can replace the `stack build` command with `stack install` and it should place the compiled binaries appropriately on your system. If you don't happen to have haskell installed on your system already, try running `brew install haskell-stack` before proceeding with the above insturctions.

To have the layout load on startup, install the `kmonad.plist` file found in this directory, either via launchctl or, should you prefer to use the GUI, with something like [LaunchControl](https://www.soma-zone.com/LaunchControl/).

Switching to home row mods leaves quite a few spare keys on your keyboard. You can remap these to frequently typed phrases with KMonad's __tap macro__ system:

```kmonad
    (tap-macro K M o n a d)
    #(K M o n a d)
```

There are a few examples included in the sample configuration files in this directory. `engram.kbd` is the vanilla variant that adheres strictly to the official engram layout. `engram-hrm.kbd` also adheres to the vanilla layout, but includes home row mods. An `engrammer.kbd` example is included as well, both for breadth, and to demonstrate KMonad's macro system in practice. See the [KMonad Configuration Guide](https://github.com/kmonad/kmonad/blob/1b2ec006259ddbe6cda30db8eb783e8177a9f12b/keymap/tutorial.kbd#L481C1-L481C2) for more detailed instructions.