# Boot logos

`boot_logo_C.jpg`, `boot_logo_D.jpg`, and `boot_logo_E.jpg` in this folder are the files copied to `/usr/comma/bg.jpg`. They are 1080×2160, the same size as `frogpilot_boot_logo.jpg` and `stock_bg.jpg`. FrogPilot's `update_boot_logo()` copies the file and does not rotate it.

The comma 3X UI is landscape (2160×1080). Weston paints `bg.jpg` with `background-type=scale-crop`, which shows the center 1080×540 band of a 1080×2160 file, scaled 2×, with the subject upright. The official frog logo is drawn upright in that tall file, and these three files put the landscape castle in that same center band.

`variants/*_land.jpg` are the 2160×1080 masters. `variants/*_rot90cw.jpg` are those masters rotated 90° clockwise.

If the first boot is sideways, replace the three files in this folder with `variants/boot_logo_{C,D,E}_rot90cw.jpg` (keep the names `boot_logo_C.jpg`, `boot_logo_D.jpg`, and `boot_logo_E.jpg`) and reboot. If the castle is a small centered crop, the landscape masters were copied instead of the packed files.
