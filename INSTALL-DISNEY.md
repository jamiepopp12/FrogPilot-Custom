# Install this private Disney fork on a comma 3X

This repo is a private copy of FrogPilot for one comma 3X in a Toyota Highlander. Keep it private. Do not open a pull request on FrogAi/FrogPilot, and do not submit the theme to The Pond or any FrogPilot theme sharing.

comma's installer URL (`https://installer.comma.ai/...` and `FrogPilot.download`) only clones public GitHub repos. It cannot see this repo. Install with SSH or the device shell, then let FrogPilot's own updater track the branch.

## Which branch to install

Install **`cursor/disney-theme-f72d`**. That is the Disney branch. A nightly Action rebases it onto upstream `FrogPilot` and pushes only when that rebase is clean. GitHub runs scheduled workflows from the repo's default branch, so that workflow file is also on `FrogPilot` and on the current default branch.

**`FrogPilot`** here is upstream's release branch for comma 3, comma 3X, and comma four, including Toyota, plus that one workflow file. It does not contain the Disney theme. Use it to roll back inside this repo, or use public `FrogPilot.download` for a checkout with no extra file. Do not install `FrogPilot-GM-CSLC`. That branch is for GM cars. The importer left it as the default branch, and the token used here cannot change the default (GitHub returned 403). In the repo settings, set the default branch to **FrogPilot**.

## Back up settings first

On the device, while parked:

1. Open **FrogPilot → Data → Settings Backups** and tap **BACKUP**.
2. From a shell, keep a second copy:

```sh
cp -a /data/params /data/params_before_disney
cp -a /data/toggle_backups /data/toggle_backups_before_disney
```

The first boot of the Disney branch selects the user theme **Disney Parks** (sounds, Pluto turn signals, and the Mickey wheel), turns random themes off, and turns on **Custom Alerts**, **Green Light Alert**, and **Lead Departing Alert**. Later boots refresh the theme files but do not change those settings again. Restore the backup above if you want the previous choices back.

## Install over SSH with a deploy key

On a computer, make a key and add the public half in GitHub → this repo → Settings → Deploy keys. Leave it read-only. Do not commit the private key, and do not put it in the repo.

```sh
ssh-keygen -t ed25519 -f frogpilot-disney -N ""
```

Copy `frogpilot-disney` to the device at `/data/ssh/frogpilot_disney` (`chmod 600`). SSH to the comma 3X on the same Wi-Fi (`ssh comma@<device-ip>`). Then, on the device:

```sh
mkdir -p /home/comma/.ssh
cat >> /home/comma/.ssh/config << 'EOF'
Host github.com
  HostName github.com
  User git
  IdentityFile /data/ssh/frogpilot_disney
  IdentitiesOnly yes
EOF
chmod 600 /home/comma/.ssh/config

install_branch() {
  git remote set-url origin git@github.com:jamiepopp12/FrogPilot-Disney.git
  git fetch origin cursor/disney-theme-f72d
  git checkout -B cursor/disney-theme-f72d FETCH_HEAD
}

cd /data/openpilot
install_branch
for repo in /data/safe_staging/merged /data/safe_staging/finalized; do
  if [ -d "$repo/.git" ] || [ -f "$repo/.git" ]; then
    git -C "$repo" remote set-url origin git@github.com:jamiepopp12/FrogPilot-Disney.git
    git -C "$repo" fetch origin cursor/disney-theme-f72d
    git -C "$repo" checkout -B cursor/disney-theme-f72d FETCH_HEAD
  fi
done
sudo reboot
```

FrogPilot's updater fetches `origin` inside `/data/safe_staging` and hard-resets to the branch it is already on, so the staging checkouts have to point at this repo too. A nightly rebase force-updates `cursor/disney-theme-f72d` only after the rebase applies cleanly. The updater's hard reset follows that.

## Install from the device terminal

The same shell commands work from a terminal on the device. If you would rather use HTTPS than a deploy key, create a fine-grained GitHub token that can read this one private repo and set the remote on the device only:

```sh
git remote set-url origin https://<github-user>:<token>@github.com/jamiepopp12/FrogPilot-Disney.git
```

The token stays in the device's git config. Do not copy that URL into a commit, a note in this repo, or a screenshot.

## What you should see

After reboot, setup copies the theme to `/data/themes/theme_packs/disney_parks-user_created/` and the wheel to `/data/themes/steering_wheels/disney_parks-user_created.gif`. The still `wheel.png` is kept in the theme pack; the gif is the wheel FrogPilot shows.

- Startup plays the monorail with the startup message on a normal drive. Leave at least one startup message line filled in, or FrogPilot does not show that alert.
- Going from onroad to offroad plays Mickey's "See ya real soon!"
- The first green light of each drive plays the full Peter Pan `go.wav`. Later green lights, and lead-departing, play the engage sparkle. Other prompt and warning sounds are unchanged.
- Holiday themes do not replace the Disney sound pack, turn signals, or wheel while those three settings still point at Disney Parks. Colors and icons can still follow the holiday. Turn **Holiday Themes** off to stop that too.
- The boot logo cycles C, then D, then E, one step each time the car goes offroad. The files installed are the packed 1080×2160 JPEGs, which match `frogpilot_boot_logo.jpg`. Weston scale-crops that shape onto the landscape screen.

If the castle is sideways, copy `frogpilot/assets/other_images/disney_boot/variants/boot_logo_{C,D,E}_rot90cw.jpg` over `boot_logo_{C,D,E}.jpg` in that same folder (keep the short names) and reboot. If it is a small picture in the middle, those packed files were replaced by the `*_land.jpg` masters. See `frogpilot/assets/other_images/disney_boot/README.md`.

## Roll back to stock FrogPilot

Restore settings with **FrogPilot → Data → Settings Backups → RESTORE**, or copy `/data/params_before_disney` back to `/data/params`.

Then point git at the public release and reboot:

```sh
cd /data/openpilot
git remote set-url origin https://github.com/FrogAi/FrogPilot.git
git fetch origin FrogPilot
git checkout -B FrogPilot FETCH_HEAD
sudo reboot
```

Do the same `remote` and `checkout` in `/data/safe_staging/merged` and `/data/safe_staging/finalized` if those directories exist. You can instead uninstall and enter `FrogPilot.download` as a custom software URL. That installs public FrogPilot, not this private branch. Stock setup puts the frog boot logo back. Uninstalling FrogPilot restores comma's `stock_bg.jpg`.
