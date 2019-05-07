## MK Automatik

_Only works on OSX, really alpha_

Play MK Towers indefinitely with automation.

#### How to

Make sure you have Python3.7 installed, then, install dependancies with pip3

```
pip3 install -r requirements.txt
```

Open RemotePlay with DualShock Bindings (enable Keyboard use for most DualShock keys, by default, RemotePlay just binds X and gives on onscreen controls for a few more)

```
DYLD_FORCE_FLAT_NAMESPACE=1 DYLD_INSERT_LIBRARIES=dualshock-bindings/iohid_wrap.dylib /Applications/RemotePlay.app/Contents/MacOS/RemotePlay
```

Go to the tower you want to play (either Klassic or Towers in Time) in your RemotePlay and run the script

```
python3 main.py
```

Now the script should select the left variation of **Noob Saibot**, enable AI, and go into fights, whenever you Win, it'll press **Kontinue** automatically, whenever you lose, it'll exit the tower, select it again, pick **Noob Saibot**, and run it again.

#### TODO

- Figure out OSError: [Errno 23] Too many open files in system
- Easy way to select characters (right now it's a key combo hardcoded)
- Easy way to select variations
- Pick tower Difficulty
- Lower key press times
