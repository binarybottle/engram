import {
  FromKeyParam,
  // layer,
  LayerKeyParam,
  map,
  ModifierParam,
  rule,
  simlayer,
  // ToKeyParam,
  withMapper,
  withModifier,
  writeToProfile,
} from 'karabinerts'
import { engram, engram_left, engram_right } from './engram.ts'

const qhr: FromKeyParam[] = ['a', 's', 'd', 'f', 'j', 'k', 'l', ';']
const mods = ['‹⌃', '‹⌥', '‹⌘', '‹⇧', '›⇧', '›⌘', '›⌥', '›⌃']

  writeToProfile('karabiner.ts', [

    // Uncomment for home row mods. This is an incomplete implementation! Use KMonad for the full experience.
    
    // ...(qhr.map((key, i) =>
    //   simlayer(key as LayerKeyParam, mods[i])
    //     .manipulators([
    //       withMapper(i < 4 ? engram_right : engram_left)((k) =>
    //         map(k.from).to(k.to, mods[i] as ModifierParam)
    //       ),
    //     ])
    // )),

    // Engram base layer
    rule('engram').manipulators([
      withModifier('optionalAny')([
        withMapper(engram)((k) => map(k.from).to(k.to)),
      ]),
    ]),
  ], {
    'simlayer.threshold_milliseconds': 500,
    'basic.to_if_alone_timeout_milliseconds': 199,
    'basic.to_delayed_action_delay_milliseconds': 200,
    'basic.to_if_held_down_threshold_milliseconds': 200,
  })
