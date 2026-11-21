# Boot logo

`boot_logo_C.jpg` is the only file copied to `/usr/comma/bg.jpg`. It is a 1080×2160 JPEG, the same size as `stock_bg.jpg` and `frogpilot_boot_logo.jpg`. Setup always uses this one image.

The comma 3X splash is Weston's `scale-crop` of that file onto the 2160×1080 screen. The crop keeps the center 540 rows and scales them by 2. The comma mark and the frog sit in that band, drawn upright. This castle is placed the same way: the 2160×1080 artwork, scaled to 1080×540, pasted at y=810. A 2160×1080 file is the wrong canvas. On the device it showed the castle split across the left and right edges, upside down, with the wordmark mirrored.

`variants/boot_logo_C_nopictures_land.jpg` is the landscape master. `variants/boot_logo_C_nopictures.jpg` is the installed 1080×2160 file. The older `*_land.jpg` and `*_rot90cw.jpg` masters are not installed.
