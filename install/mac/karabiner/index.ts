import {
  layer,
  map,
  rule,
  simlayer,
  // toKey,
  withMapper,
  withModifier,
  writeToProfile,
} from 'karabinerts'
import { engram, engram_left, engram_right } from './engram.ts'

// writeToProfile("--dry-run", [
writeToProfile('karabiner.ts', [
  layer('⇪', 'nav').manipulators([
    withModifier('optionalAny')([
      map('u').to('↖︎'),
      map('i').to('⇟'),
      map('o').to('⇞'),
      map('p').to('↘︎'),
      map('j').to('←'),
      map('k').to('↓'),
      map('l').to('↑'),
      map(';').to('→'),
      map('m').to('z', '<⌘'),
      map(',').to('x', '<⌘'),
      map('.').to('c', '<⌘'),
      map('/').to('v', '<⌘'),
    ]),
  ]),
  simlayer('f', '<⇧').manipulators([
    // Reminder to experiment with .toDelayedAction() method
    // map('<⌘').toIfAlone('⌫').to('<⌘').toDelayedAction(toKey('m'), toKey('t')),
    // withMapper(engram_right)((k) => map(k.from, k.fromMod).to(k.to, "⌘⇧").condition(ifVar("<⌘", 1))),
    // withMapper(engram_right)((k) => map(k.from, k.fromMod).to(k.to, "⇧⌥").condition(ifVar("<⌥", 1))),
    // withMapper(engram_right)((k) => map(k.from, k.fromMod).to(k.to, "⌃⇧").condition(ifVar("<⌃", 1))),
    withMapper(engram_right)((k) => map(k.from, k.fromMod).to(k.to, '⇧')),
  ]),
  simlayer('j', '>⇧').manipulators([
    // withMapper(engram_left)((k) => map(k.from, k.fromMod).to(k.to, "⌘⇧").condition(ifVar(">⌘", 1))),
    // withMapper(engram_left)((k) => map(k.from, k.fromMod).to(k.to, "⇧⌥").condition(ifVar(">⌥", 1))),
    // withMapper(engram_left)((k) => map(k.from, k.fromMod).to(k.to, "⌃⇧").condition(ifVar(">⌃", 1))),
    withMapper(engram_left)((k) => map(k.from, k.fromMod).to(k.to, '⇧')),
  ]),
  simlayer('d', '<⌘').manipulators([
    // withMapper(engram_right)((k) => map(k.from, k.fromMod).to(k.to, "⌘⌥").condition(ifVar("<⌥", 1))),
    withMapper(engram_right)((k) => map(k.from, k.fromMod).to(k.to, '⌘')),
  ]),
  simlayer('k', '>⌘').manipulators([
    // withMapper(engram_left)((k) => map(k.from, k.fromMod).to(k.to, "⌘⌥").condition(ifVar(">⌥", 1))),
    withMapper(engram_left)((k) => map(k.from, k.fromMod).to(k.to, '⌘')),
  ]),
  simlayer('s', '<⌥').manipulators([
    withMapper(engram_right)((k) => map(k.from, k.fromMod).to(k.to, '⌥')),
  ]),
  simlayer('l', '>⌥').manipulators([
    withMapper(engram_left)((k) => map(k.from, k.fromMod).to(k.to, '⌥')),
  ]),
  simlayer('a', '<⌃').manipulators([
    withMapper(engram_right)((k) => map(k.from, k.fromMod).to(k.to, '⌃')),
  ]),
  simlayer(';', '>⌃').manipulators([
    withMapper(engram_left)((k) => map(k.from, k.fromMod).to(k.to, '⌃')),
  ]),

  rule('short pinkies').manipulators([
    withModifier('optionalAny')([
      map('<⌘').toIfAlone('⌫').to('<⌘'),
      map('>⌘').toIfAlone('⏎').to('<⌘'),
      map('=').to('⌫'),
      map('>⇧', '<⇧').to('\\'),
      map('>⇧').to('/'),
    ]),
  ]),
  rule('engram').manipulators([
    withModifier('optionalAny')([
      withMapper(engram)((k) => map(k.from, k.fromMod).to(k.to, k.toMod)),
    ]),
  ]),
], {
  'simlayer.threshold_milliseconds': 300,
  'basic.to_delayed_action_delay_milliseconds': 251,
  'basic.to_if_alone_timeout_milliseconds': 250,
  'basic.to_if_held_down_threshold_milliseconds': 251,
})
