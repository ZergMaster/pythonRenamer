# Sprite Renamer

*[Русская версия](README.ru.md)*

A small Python script for the boring half of art integration in Unity: renaming a folder of sprites
in bulk, stripping the sidecar files that come with them, and rebasing a 1..n numbering to 0..n-1 so
the filenames line up with the array indices the game reads them into.

Written in 2020 while working on **CyberCat**, a mobile game made at a small studio.

---

## The problem

Art arrives from an artist named the way the artist named it. The game needs it named the way the
code reads it. Between those two facts sits a job that nobody has ever enjoyed doing.

- **A batch is a batch.** A helmet set is twelve icons, and there are a lot of helmet sets. Renaming
  twelve files by hand is five minutes; doing it once per set, every time art is redelivered, is the
  rest of the afternoon.
- **The numbering is off by one, on purpose.** Artists count from 1, because people count from 1.
  Code indexes from 0. Renaming `helmet1..helmet12` to `helmet0..helmet11` by hand means walking the
  list in the right order or clobbering a file that already exists.
- **Unity leaves litter.** Every asset has a `.meta` sidecar. Move or copy a folder the wrong way and
  you are left with orphaned `.meta` files that Unity will happily re-create but that pollute the
  diff in the meantime.
- **Manual renaming is silently wrong.** Miss one file in a set of twelve and nothing breaks — the
  icon is just missing in the game, once, for one helmet, and you find out in a build.

## The solution

Five functions over `os.listdir` and `os.rename`, each doing one transformation, with the target
folder as a variable at the top of the file:

- `renameFilesFromTo(from, to)` — swap a filename prefix across the folder
- `changeNumeration()` — shift the trailing number down by one, in two passes with a `___` prefix in
  between so a rename never lands on a name that still exists
- `addStringToFronName(str)` — prepend to every name
- `addFormat(ext)` — give an extension to files that lost theirs
- `deleFilesFormats()` — delete the sidecars

The two-pass numbering is the only part that is not obvious, and it is the part that matters:
renaming `1→0, 2→1, 3→2` in place collides on every step, so the script renames everything to a
temporary `___`-prefixed name first and strips the prefix in a second sweep.

Calls sit commented out at the bottom of the file — you uncomment the one you need and run it. It is
a tool for one person, and it is shaped like one.

---

## What it looks like

A real run against a folder of helmet icons, the same shape as the ones in CyberCat:

![Before and after: No_act_helmet1..12.png plus .meta and .mp3 files become Helmet0..11.png](docs/before-after.png)

---

## Getting started

```bash
git clone https://github.com/ZergMaster/pythonRenamer.git && cd pythonRenamer
# 1. set `path` at the top of renamer.py to your sprite folder
# 2. uncomment the call you need at the bottom of the file
python3 renamer.py
```

It renames in place with no dry run and no undo, so point it at a copy the first time.

**Two rough edges, stated rather than hidden:** `deleFilesFormats()` ignores its argument and always
deletes `.meta` and `.mp3` — the parameter was never wired up. And `addStringToFronName()` drops the
extension when it renames, so it is only useful on extensionless files or followed by `addFormat()`.

---

## Who used it, and what changed

I used it, on the CyberCat Unity project — the hardcoded path in the file is still pointing at
`Assets/Resources/Sprites/ui/Helmet/Icons/big`. It replaced renaming sprite batches by hand in
Explorer, and nobody else ever ran it.

I am including it because of what it is rather than in spite of it. This is the smallest possible
version of the thing I have built four times since at three studios, and each of those started
exactly here: noticing that a step between the artist and the build was being done by hand, and
writing thirty lines to stop doing it. The ones that mattered grew into a layout-extraction tool, an
asset-delivery pipeline, a reskin diffing tool and a LiveOps content editor — but the reflex is the
same one, and this file is the earliest honest example of it I still have.

---

## Tech

Python 3 · standard library only (`os`)
