# rpi-vidlooper

A video looper for the Raspberry Pi, controlled by GPIO pins. Designed to
run an unattended video display, where users can select the active video
by switch.

MIT licensed.

## Features

* Play videos using [OMXplayer](https://elinux.org/Omxplayer), a hardware-
assisted video player for smooth playback.
* Switch between 2 or more videos using hardware switches wired to the
Raspberry Pi's GPIO pins.
* Optionally, indicate the active video by LED. This can be used with
arcade-style switches which have built-in LEDs, or separate ones.
* Callback-based, rather than polling-based. This means that button
presses should always be acted upon.
* Thread locking, to avoid issues when buttons are pressed rapidly
and the video hasn't finished loading yet.

## Usage

On the hardware side, you'll need a Raspberry PI with several switches,
one for each video. Each switch should be connected to a GPIO pin, and
to ground. Optionally, you can set up an indicator LED for each video,
connected to a GPIO pin.

Install dependencies:

```
sudo apt-get update
sudo apt-get install python3-pip omxplayer fbi
```

Install rpi-vidlooper:

```
pip3 install rpi-vidlooper
```

This creates the `vidlooper` command. For usage help, see:

```
vidlooper --help
```

## Troubleshooting

### RuntimeError: No access to /dev/mem. Try running as root!

By default, you'll need to run `sudo vidlooper`, to gain access to the GPIO
pins and the graphics card (GPU) for `omxplayer`. Generally, this is not
recommended.

To avoid this, the user you want to run the vidlooper as will need to be
in the `gpio` group. For example, for the `pi` user, you'd need to do this:

```
sudo usermod -a -G gpio pi
```

See [further information on this issue](https://raspberrypi.stackexchange.com/questions/40105/access-gpio-pins-without-root-no-access-to-dev-mem-try-running-as-root).

### No rights to /dev/vchiq

See the [OMXplayer troubleshooting](https://elinux.org/Omxplayer) to fix
this issue. It's also possible to avoid by running `sudo vidlooper`, but
as above, this is not recommended.

## Further reading

* [Python on the Raspberry Pi](https://www.raspberrypi.org/documentation/linux/software/python.md)
* [OMXPlayer, a hardware-accelerated video player for Raspberry Pi](https://www.raspberrypi.org/documentation/raspbian/applications/omxplayer.md)
