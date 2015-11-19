#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     16/11/2015
# Copyright:   (c) User 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import usb.core
import usb.util
import time

# find our device
dev = usb.core.find(idVendor=0x0e6f)# 0x0e6f Logic3 (made lego dimensions portal hardware)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# Initialise portal
print dev.write(1, [0x55, 0x0f, 0xb0, 0x01, 0x28, 0x63, 0x29, 0x20, 0x4c, 0x45, 0x47, 0x4f, 0x20, 0x32, 0x30, 0x31, 0x34, 0xf7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Startup



# Pad color notation used in comments:
# Left, center, right
# l:colour, c: colour:, r: colour




# General command structure for endpoint 01
# 0x55 Magic number
# command byte 1
# command byte 2
# message counter, no noticed effect
# args...
# checksum, (simple addition of previous bytes with overflow at 255)
# padding to 32 bytes


# Noticed argument conventions
# Pad numbering:
# 0x01, 0x02, 0x03
# Colour ordering
# Red, green, blue
# Colour values 1 byte in length
# 0x00: off, 0xff: maximum brightness


# Checksum characteristics
# 1 Byte in size
# Always the last non-zero byte (Unknown what happens if checksum turns out to be zero)
# Reordering message bytes does not invalidate checksum
# Message counter affects checksum
# Simple addition of previous bytes with overflow at 255


# List of commands for endpoint 01:
# 0x01 0xb3 -
# 0x01 0x08 - Unknown
# 0x04 0xd2 - unknown
# 0x06 0xc0 - Immediately switch pad(s) to a single value
# 0x08 0xc2 - Immediately change the colour of one or all pad(s), fade and flash available
# 0x09 0xc3 - set 1 or all pad(s) to a colour with variable flash rates
# 0x14 0xc6 - fade to value?
# 0x17 0xc7 -
# 0x0a 0xb1 -
# 0x0a 0xd4 -
# 0x0b 0x01 - unknown, no change to lights
# 0x0b 0x02 - unknown, no change to lights
# 0x0b 0x03 - unknown, no change to lights
# 0x0e 0xc8 - Immediately switch to set of colours?
# 0x0f 0xb0 - Startup?

# Commands 0x01 0xXX - all tried have no visible effect, short/no arguments


# 0x0f 0xb0 Startup
# 0: Always 0x55
# 1: Command
# 2: command cont
# 3: Message counter
# 4:
# 5:
# 6:
# 7:
# 8:
dev.write(1, [0x55, 0x0f, 0xb0, 0x01, 0x28, 0x63, 0x29, 0x20, 0x4c, 0x45, 0x47, 0x4f, 0x20, 0x32, 0x30, 0x31, 0x34, 0xf7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Startup




# 0x06 0xc0 Immediately switch pad(s) to a value
# Byte: use
# 0: Always 0x55
# 1: Command
# 2: command cont
# 3: Message counter
# 4: Pad to change 0=all, 1=center, 2=left, 3=right,
# 5: Red value
# 6: Green value
# 7: Blue Value
# 8: Checksum
# 9-31: padding, 0x00

# Sniffed
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0xff, 0xff, 0x1a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to light blue (Found via sniffing)
# Mixed colours found by fuzzing
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0x00, 0xff, 0x1b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to Purple (found via fuzzing)
# RGB Monochromatic hex(28) == 0x1c
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0x00, 0x00, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to red
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0xff, 0x00, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to green (found via fuzzing)
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0xff, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to dark blue (found via fuzzing)
# All pads off
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0x00, 29, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch all pads off (Found by fuzzing)







# 0x14 Fade to value
# Byte 0 is always 0x55
# Byte
##        print dev.write(1, [0x55, 0x14, 0xc6, 0x04, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Fade to dark blue
#[0x55, 0x14, 0xc6, 0x26, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0xfd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All dark Blue
#[0x55, 0x14, 0xc6, 0x27, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0xfb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All pink
#[0x55, 0x14, 0xc6, 0x28, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0xb4, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All red
#[0x55, 0x14, 0xc6, 0x29, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All yellow
#[0x55, 0x14, 0xc6, 0x2a, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All green
#[0x55, 0x14, 0xc6, 0x2b, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x4c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All cyan
#[0x55, 0x14, 0xc6, 0x2c, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All dark blue








# 0x0e 0xc8 Immediately switch to set of colours
# Byte: use
# 0: Always 0x55
# 1: 0x0e cmd
# 2: 0xc8 cmd
# 3 Message counter
# 4: ?
# 5: center:red
# 6: center:green
# 7: center:blue
# 8: ?
# 9: left:red
# 10: left:green
# 11: left:blue
# 12: ?
# 13: right:red
# 14: right:green
# 15: right:blue
# 16: Checksum
# 17-31: Padding


# left:cyan, center:yellow, right:pink
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x3e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:cyan, center:yellow, right:pink
dev.write(01, [0x55, 0x0e, 0xc8, 0x1b, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x53, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x26, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x26, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x03, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x3b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x2e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x19, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x07, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x3f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x0c, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x44, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x01, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x39, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1a, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x52, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

# Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x23, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x0d, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x20, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x59, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x25, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x37, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1c, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x37, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x0b, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x55, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1e, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x68, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x30, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x7a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x07, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1a, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x14, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x32, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x02, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x4c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x17, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x61, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x33, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x7d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x0d, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x23, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x01, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x4b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

# Fuzzed:
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x18, 184, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# left:off, center:yellow, right:pink
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x00, 160, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off, center:yellow, right:red
# Center
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:red right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0xff, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:green right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0xff, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:blue right:off
# Left
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:red center:off right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:green center:off right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xff, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:blue center:off right: off
# Right
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:off right:red
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:off right:green
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xff, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:off right:blue

# Failed fuzzing:
#[0x55, 0x0e, 0xc8, 0x20, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0xff, 0xff, chk, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# nothing ever tuns on





# 0x06 0xc0 ?Change one pad?
# Byte: use
# 0: Always 0x55
# 1: 0x06 cmd
# 2: 0xc0 cmd
# 3: Message counter
# 4: 0x0, 0x1, 0x2, 0x3
# 5: Colour?
# 6: Colour?
# 7: Colour?
# 8: Checksum
# 9-31 Padding

dev.write(01, [0x55, 0x06, 0xc0, 0x2b, 0x03, 0xff, 0x00, 0x18, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# l:off, c:off, r:pink
dev.write(01, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0xff, 0xff, 0x1a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# all light blue
dev.write(01, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0xff, 0x1c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# All dark blue
dev.write(01, [0x55, 0x06, 0xc0, 0x2b, 0x00, 0x00, 0x00, 0xff, 0x45, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# All dark blue
dev.write(01, [0x55, 0x06, 0xc0, 0x34, 0x01, 0xf0, 0x00, 0x16, 0x56, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Change center to pink


# 0x04 0x02
# Unknown effect, does not turn on pads?
# Byte: use
# 0: Always 0x55
# 1: 0x04 cmd
# 2: 0x02 cmd
# 3: Message counter
# 4: ?
# 5: ?
# 6: Checksum?
# 7-31: Padding




# 0x0a 0xb3
# Unknown effect, does not turn on or off pads
# Byte: use
# 0: Always 0x55
# 1: 0x0a cmd
# 2: 0xb3 cmd
# 3: Message counter
# 4:
# 5:
# 6:
# 7:
# 8:
# 9:
# 10:
# 11:
# 12: Checksum
# 13-31: Padding




# 0x04 0xd2
# Unknown effect, does not turn on or off pads
# Byte: use
#0: Always 0x55
#1: 0x04 cmd
#2: 0xd2 cmd
#3: Message counter
#4: ?
#5: ?
#6: Checksum?
#7-31: Padding


# 0x08 0xc2 - Immediately change the colour of one or all pad(s), fade and flash available
# Byte: use
# 0: Always 0x55
# 1: 0x08
# 2: 0xc2
# 3: Message counter?
# 4: Pad all=0 c=1 l=2 r=3
# 5: ?change speed - needs more investigation
# 6: ?flash rate/count - fuzz to investigate?
# 8: green
# 9: blue
# 10: Checksum
# 11-31: Padding
[0x55, 0x08, 0xc2, 0x0b, 0x01, 0x03, 0x01, 0xf0, 0x00, 0x16, 0x35, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# c:pink
[0x55, 0x08, 0xc2, 0x0f, 0x03, 0x03, 0x01, 0xf0, 0x00, 0x16, 0x3b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# r:pink
[0x55, 0x08, 0xc2, 0x0f, 0x03, 0x03, 0x01, 0xff, 0x00, 0x00, 52, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# r:red
# rgb
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x03, 0x01, 0xff, 0x00, 0x00, 50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:red
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x03, 0x01, 0x00, 0xff, 0x00, 50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:green
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x03, 0x01, 0x00, 0x00, 0xff, 50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:blue
# fades and flashes:
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0xff, 0x01, 0xff, 0x00, 0x00, 46, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# r:red slow fade in
[0x55, 0x08, 0xc2, 0x0f, 0x03, 0xf0, 0x01, 0x03, 0x00, 0x16, 0x3b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# r:blue slow fade in
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x01, 0xff, 0xff, 0x00, 0x00, 46, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:red rapid flash between red and prev color
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x00, 0xff, 0xff, 0x01, 0x00, 46, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:red rapid flash between red and prev color, almost imperceptible
[0x55, 0x08, 0xc2, 0x0f, 0x03, 0x16, 0x01, 0x03, 0x00, 0xf0, 0x3b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# r:blue qucik fade in
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x55, 0x01, 0xff, 0x00, 0x00, 132, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:red fade from previous colour
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x01, 0x55, 0xff, 0x00, 0x00, 132, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:red rapid flash then solid red
[0x55, 0x08, 0xc2, 0x05, 0x01, 0x01, 0x06, 0x4c, 0x20, 0x00, 0x98, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# Flash yellow quickly several times then return to previous colour







# 0x09 0xc3 - set 1 or all pad(s) to a colour with variable flash rates
# Flashes between old and new colour
# Does not appear to synchronise flashes
# Byte: use
# 0: Always 0x55
# 1: 0x09
# 2: 0xc3
# 3: Message counter?
# 4: pad 0:all, 1:center, 2:left 3:right
# 5: On pulse length, higher is longer
# 6: Off pulse length, higher is longer
# 7: Number of pulses, 0xff is forever
# 8: red
# 9: green
# 10: blue
# 11: checksum
# 12-31: padding

[0x55, 0x09, 0xc3, 0x0e, 0x01, 0x02, 0x02, 0x07, 0xff, 0x6e, 0x00, 0xa8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
[0x55, 0x09, 0xc3, 0x3a, 0x03, 0x02, 0x02, 0x07, 0x00, 0x16, 0x04, 0x83, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
[0x55, 0x09, 0xc3, 0x10, 0x02, 0x02, 0x02, 0x07, 0x00, 0x16, 0x04, 0x58, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
[0x55, 0x09, 0xc3, 0x12, 0x02, 0x02, 0x02, 0x07, 0x00, 0x16, 0x04, 0x5a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
send_command([0x55, 0x09, 0xc3, 0x1f, 0x01, 0x02, 0x02, 0x07, 0x00, 0xff, 0x00])# c:green flash qucikly a few times then stay on
send_command([0x55, 0x09, 0xc3, 0x1f, 0x01, 0x02, 0x02, 0x07, 0xff, 0x00, 0x00])# c:red flash qucikly a few times then stay on
send_command([0x55, 0x09, 0xc3, 0x1f, 0x01, 0x02, 0x02, 0x07, 0x00, 0x00, 0xff])# c:blue flash qucikly a few times then stay on
send_command([0x55, 0x09, 0xc3, 0x1f, 0x01, 0x02, 0x02, 0xff, 0x00, 0x00, 0xff])# c:blue flash qucikly forever
send_command([0x55, 0x09, 0xc3, 0x1f, 0x02, 0x02, 0x02, 0xff, 0x00, 0xff, 0x00])# l:green flash qucikly forever



# 0x17 0xc7
#
# Byte: use
#0x55# 00: Always 0x55
#0x17# 01: 0x17
#0xc7# 02: 0xc7
#0x3e# 03: Message counter?
#0x01# 04:
#0x02# 05:
#0x02# 06:
#0x0c# 07:
#0x00# 08:
#0x00# 09:
#0x04# 10:
#0x01# 11:
#0x02# 12:
#0x02# 13:
#0x0c# 14:
#0x33# 15: l:red
#0x00# 16: l:green
#0x00# 17: l:blue
#0x01# 18:
#0x02# 19:
#0x02# 20:
#0x0c# 21:
#0x33# 22: r:red
#0x16# 23: r:green
#0x00# 24: r:blue
#0x24# 25: checksum
#0x00# 26-31: padding

[0x55, 0x17, 0xc7, 0x3d, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x04, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x16, 0x00, 0x01, 0x02, 0x02, 0x0c, 0x33, 0x00, 0x00, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# l:green, c:blue, r:red, returns
[0x55, 0x17, 0xc7, 0x2e, 0x01, 0x02, 0x02, 0x07, 0x30, 0x14, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x02, 0x07, 0x00, 0x16, 0x00, 0xd7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# l:off, c:white, r:green, stays at new values

send_command([0x55, 0x17, 0xc7, 0x3e, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x04, 0x01, 0x02, 0x02, 0x0c, 0xff, 0x00, 0x00, 0x01, 0x02, 0x02, 0x0c, 0x33, 0x16, 0x00,])# l: bright red, c: dim blue, r: dim yellow, returns
send_command([0x55, 0x17, 0xc7, 0x3e, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x04, 0x01, 0x02, 0x02, 0x0c, 0x00, 0xff, 0x00, 0x01, 0x02, 0x02, 0x0c, 0x33, 0x16, 0x00,])# l: bright green, c: dim blue, r: dim yellow, returns
send_command([0x55, 0x17, 0xc7, 0x3e, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x04, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0xff, 0x01, 0x02, 0x02, 0x0c, 0x33, 0x16, 0x00,])# l: bright blue, c: dim blue, r: dim yellow, returns

send_command([0x55, 0x17, 0xc7, 0x3e, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x04, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0xff, 0xff, 0x02, 0x02, 0x0c, 0x33, 0xff, 0x00,])# l: bright blue, c: dim blue, r: bright green, returns

send_command([0x55, 0x17, 0xc7, 0x3e, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x04, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x00, 0xff, 0x02, 0x02, 0x0c, 0xff, 0x00, 0x00,])# l: bright green, c: dim blue, r: bright red, returns
send_command([0x55, 0x17, 0xc7, 0x3e, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x04, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x00, 0xff, 0x02, 0x02, 0x0c, 0x00, 0xff, 0x00,])# l: bright green, c: dim blue, r: bright green, returns
send_command([0x55, 0x17, 0xc7, 0x3e, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x04, 0x01, 0x02, 0x02, 0x0c, 0x00, 0x00, 0x00, 0xff, 0x02, 0x02, 0x0c, 0x00, 0x00, 0xff,])# l: bright green, c: dim blue, r: bright blue, returns







def main():
    pass

if __name__ == '__main__':
    main()
