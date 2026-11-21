# Boot logo

`boot_logo_C.jpg` is the only file copied to `/usr/comma/bg.jpg`. It is a 2160×1080 landscape JPEG. `update_boot_logo()` copies the file and does not rotate it. Setup always uses this one image.

On this comma 3X the splash shows `bg.jpg` as-is, fitted to the landscape screen, with no rotation. A 1080×2160 file stays a narrow portrait strip in the middle. This file is the upright `variants/boot_logo_C_nopictures_land.jpg` master: blue castle, “Walt Disney” wordmark, no “PICTURES” line. The castle top is at the top of the frame.

`frogpilot_boot_logo.jpg` and `stock_bg.jpg` in this repo are 1080×2160, with the frog and the comma mark upright in that tall file. That shape letterboxes on this device, so this castle file does not follow it.

`variants/*_land.jpg` and `variants/*_rot90cw.jpg` are earlier masters. The rotated files are tall canvases and are not installed. `boot_logo_D` and `boot_logo_E` are not installed.
