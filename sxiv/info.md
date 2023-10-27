# Sxiv Settings

## Adding a Background Color

Add to your `~/.Xresources` the following lines:

```bash
! For sxiv
Sxiv.background: #000000
Sxiv.foreground: #00C0FF
Sxiv.font: hack 13
```

Then reload the file with the bellow commend:

```bash
xrdb -merge ~/.Xresources
```

## For Copy Support

Install `xcopy`
