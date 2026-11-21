# Boot logos

`boot_logo_C.jpg`, `boot_logo_D.jpg`, and `boot_logo_E.jpg` are the files copied to `/usr/comma/bg.jpg`. They are 1080×2160, the same size as `frogpilot_boot_logo.jpg`. `update_boot_logo()` copies the file and does not rotate it.

On this comma 3X the packed center-band files showed up as a small sideways castle, with the spires pointing left. These device files are the full-frame `variants/*_rot90cw.jpg` images instead: the landscape artwork rotated 90° clockwise and filling the 1080×2160 canvas. After the same display turn, the spires point up and the picture fills the screen.

`variants/*_land.jpg` are the 2160×1080 upright masters. `variants/*_rot90cw.jpg` are those masters rotated 90° clockwise. If a later boot is upside down, copy the `*_land.jpg` files over `boot_logo_{C,D,E}.jpg` and reboot.
