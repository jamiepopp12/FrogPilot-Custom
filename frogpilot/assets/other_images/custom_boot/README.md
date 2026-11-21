# Boot logos

`boot_logo_C.jpg`, `boot_logo_D.jpg`, and `boot_logo_E.jpg` are the files copied to `/usr/comma/bg.jpg`. They are 2160×1080 landscape JPEGs. `update_boot_logo()` copies the file and does not rotate it.

On this comma 3X the splash shows `bg.jpg` as-is, fitted to the landscape screen, with no rotation. A 1080×2160 file stays a narrow portrait strip in the middle. These three files are the upright `variants/*_land.jpg` masters, so the castle top is at the top of the frame and the picture fills the screen.

`frogpilot_boot_logo.jpg` and `stock_bg.jpg` in this repo are 1080×2160, with the frog and the comma mark upright in that tall file. That shape letterboxes on this device, so the castle files do not follow it.

`variants/*_rot90cw.jpg` are the same art rotated 90° clockwise into a tall canvas. They are not installed.
