import { FromKeyParam, ModifierParam, ToKeyParam } from 'karabinerts'

interface IEngram {
  from: FromKeyParam
  fromMod?: ModifierParam
  to: ToKeyParam
  toMod?: ModifierParam
}

const thumbs: IEngram[] = [
  { from: '⇥', to: '⇥' },
  { from: '␣', to: '␣' },
  { from: '<⌘', to: '⌫' },
  { from: '>⌘', to: '⏎' },
]

const left: IEngram[] = [
  // Number Row
  { from: '`', to: '[' },
  { from: 1, fromMod: '⇧', to: '\\', toMod: '⇧' },
  { from: 2, fromMod: '⇧', to: '=' },
  { from: 3, fromMod: '⇧', to: '`', toMod: '⇧' },
  { from: 4, fromMod: '⇧', to: '=', toMod: '⇧' },
  { from: 5, fromMod: '⇧', to: ',', toMod: '⇧' },
  // Center Column/Punctuation
  { from: 't', fromMod: '⇧', to: '9', toMod: '⇧' },
  { from: 't', to: 'quote' },
  { from: 'g', fromMod: '⇧', to: ';' },
  { from: 'g', to: 'comma' },
  { from: 'b', to: '-' },
  // Letters
  { from: 'q', to: 'b' },
  { from: 'w', to: 'y' },
  { from: 'e', to: 'o' },
  { from: 'r', to: 'u' },
  { from: 'a', to: 'c' },
  { from: 's', to: 'i' },
  { from: 'd', to: 'e' },
  { from: 'f', to: 'a' },
  { from: 'z', to: 'g' },
  { from: 'x', to: 'x' },
  { from: 'c', to: 'j' },
  { from: 'v', to: 'k' },
]

const right: IEngram[] = [
  // Number Row
  { from: 6, fromMod: '⇧', to: '.', toMod: '⇧' },
  { from: 7, fromMod: '⇧', to: '6', toMod: '⇧' },
  { from: 8, fromMod: '⇧', to: '7', toMod: '⇧' },
  { from: 9, fromMod: '⇧', to: '5', toMod: '⇧' },
  { from: 0, fromMod: '⇧', to: '8', toMod: '⇧' },
  { from: '-', to: ']' },
  { from: '=', fromMod: '⇧', to: '\\' },
  { from: '=', to: '/' },
  // Center Column/Punctuation
  { from: 'y', fromMod: '⇧', to: '0', toMod: '⇧' },
  { from: 'y', to: '\'', toMod: '⇧' },
  { from: 'h', fromMod: '⇧', to: ';', toMod: '⇧' },
  { from: 'h', to: '.' },
  { from: 'n', fromMod: '⇧', to: '1', toMod: '⇧' },
  { from: 'n', to: '/', toMod: '⇧' },
  { from: ']', fromMod: '⇧', to: '4', toMod: '⇧' },
  { from: ']', to: '3', toMod: '⇧' },
  { from: '\\', fromMod: '⇧', to: '`' },
  { from: '\\', to: '2', toMod: '⇧' },
  { from: '>⇧', fromMod: '⇧', to: '\\' },
  { from: '>⇧', to: '/' },
  // Letters
  { from: 'u', to: 'l' },
  { from: 'i', to: 'd' },
  { from: 'o', to: 'w' },
  { from: 'p', to: 'v' },
  { from: '[', to: 'z' },
  { from: 'j', to: 'h' },
  { from: 'k', to: 't' },
  { from: 'l', to: 's' },
  { from: ';', to: 'n' },
  { from: '\'', to: 'q' },
  { from: 'm', to: 'r' },
  { from: ',', to: 'm' },
  { from: '.', to: 'f' },
  { from: '/', to: 'p' },
]

export const engram = [
  ...left,
  ...right,
]

export const engram_left = [...left, ...thumbs]
export const engram_right = [...right, ...thumbs]
