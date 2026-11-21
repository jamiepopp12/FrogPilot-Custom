# Install on a comma 3X

Install branch: **`custom`**.

Custom software URL:

```
installer.comma.ai/jamiepopp12/custom
```

The device accepts that short form. It is the same as `https://installer.comma.ai/jamiepopp12/custom`.

comma's installer clones `github.com/jamiepopp12/openpilot` and checks out the branch in the URL. This repo is named `FrogPilot-Custom`, and `github.com/jamiepopp12/openpilot` did not exist when this was written, so the URL works after a GitHub redirect from `jamiepopp12/openpilot` to `FrogPilot-Custom`. Create that redirect by renaming this repo to `openpilot` and renaming it back to `FrogPilot-Custom`. Until that redirect exists, use the shell fallback at the bottom.

## Back up settings first

On the device, while parked and still on the current software:

1. Open **FrogPilot → Data → Settings Backups** and tap **BACKUP**.
2. From a shell, keep a second copy. Uninstall can erase what is on the device, so copy these off the comma if you can:

```sh
cp -a /data/params /data/params_before_custom
cp -a /data/toggle_backups /data/toggle_backups_before_custom
```

## Install

Uninstall the current software, or reinstall, and when the device asks for custom software enter:

```
installer.comma.ai/jamiepopp12/custom
```

The first boot selects the user theme **Custom Parks** (sounds, turn signals, and the wheel), turns random themes off, and turns on **Custom Alerts**, **Green Light Alert**, and **Lead Departing Alert**. Later boots refresh the theme files and do not change those settings again.

After reboot, setup copies the theme to `/data/themes/theme_packs/custom_parks-user_created/` and the wheel to `/data/themes/steering_wheels/custom_parks-user_created.gif`. The still `wheel.png` stays in the theme pack. The gif is the wheel FrogPilot shows.

- Startup plays with the startup message on a normal drive. Leave at least one startup message line filled in.
- Going from onroad to offroad plays the shutdown sound.
- The first green light of each drive plays the full go sound. Later green lights, and lead departing, play the engage sound. Other prompt and warning sounds are unchanged.
- Holiday themes do not replace the Custom Parks sound pack, turn signals, or wheel while those three settings still point at Custom Parks. Colors and icons can still follow the holiday. Turn **Holiday Themes** off to stop that too.
- The boot logo is only `boot_logo_C.jpg`, a 1080×2160 JPEG in the same center-band layout as the frog logo. It does not cycle. See `frogpilot/assets/other_images/custom_boot/README.md`.

Restore the settings backup with **FrogPilot → Data → Settings Backups → RESTORE** if you want the previous choices back. A few settings need a reboot after restore.

## Roll back to stock FrogPilot

Back up again if you changed settings you want to keep. Uninstall, and enter:

```
FrogPilot.download
```

That installs public FrogPilot from FrogAi. You can instead enter `installer.comma.ai/FrogAi/FrogPilot`. Stock setup puts the frog boot logo back.

If the settings backup is still on the device, restore it from **FrogPilot → Data → Settings Backups → RESTORE**. If you copied `/data/params_before_custom` off the device, copy it back to `/data/params` after the stock install.

## Shell fallback

Use this only if the installer URL cannot see the repo. The repo is public, so no deploy key is required. SSH to the comma (`ssh comma@<device-ip>`) or use a shell on the device:

```sh
cd /data
sudo rm -rf openpilot
git clone -b custom --recurse-submodules https://github.com/jamiepopp12/FrogPilot-Custom.git openpilot
sudo reboot
```

To roll back from the shell instead of the installer:

```sh
cd /data
sudo rm -rf openpilot
git clone -b FrogPilot --recurse-submodules https://github.com/FrogAi/FrogPilot.git openpilot
sudo reboot
```
