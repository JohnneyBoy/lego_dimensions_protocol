# 0xc2 - Immediately change the colour of one or all pad(s), fade and flash available
# Byte: use
# 0: Always 0x55
# 1: 0x08 Payload size == 8
# 2: 0xc2 Command
# 3: Message counter
# 4: Pad all=0 c=1 l=2 r=3
# 5: Pulse time - needs more investigation
# 6: Pulse count - 0x00 is forever, odd leaves on new colour, even leaves on old colour. 0xc8 and above is forever.
# 8: green
# 9: blue
# 10: Checksum
# 11-31: Padding

# Pulse count byte:
# 0x00 - 000 - is forever
# 0x15 - 021 - stops, stays at new colour
# 0x16 - 022 - stops, stays at old colour
# 0x17 - 023 - stops, stays at new colour
# 0xc6 - 198 - stops, returning to original colour
# 0xc7 - 199 - stops, remaining at new colour
# 0xc8 - 200 - is forever
# 0xe0 - 224 - is forever
# 0xef - 239 - is forever
# 0xfa - 250 - is forever
# 0xfe - 254 - is forever
# 0xff - 255 - is forever

# Pulse time byte:
# TODO: Check with actual timing measurement instrument ex camera/oscilliscope/photodiode
# These values are 'by-eye'
# hex  - dec - description
# 0x00 - 000 - Immediate change to new colour
# 0x01 - 001 - fast
# 0x04 - 004 - noticibly slower
# 0x15 - 021 - about 1 per second
# 0x20 - 032 - about 1 per 2secs
# 0xff - 255 - still pulses but very slow


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

# Pulse count ending state old/new
send_command([0x55, 0x08, 0xc2, 0x0f, 0x01, 0x01, 0xfe, 0xff, 0x00, 0x00])# Flash c:red forever
send_command([0x55, 0x08, 0xc2, 0x0f, 0x01, 0x10, 0x15, 0xff, 0x00, 0x00])# Pulse c:red for a while then stay on c:red
send_command([0x55, 0x08, 0xc2, 0x0f, 0x01, 0x10, 0x16, 0x00, 0xff, 0x00])# Pulse c:green for a while then return to prev colour
send_command([0x55, 0x08, 0xc2, 0x0f, 0x01, 0x10, 0x17, 0x00, 0xff, 0x00])# Pulse c:green for a while then keep new colour
send_command([0x55, 0x08, 0xc2, 0x0f, 0x01, 0x10, 0x18, 0x00, 0x00, 0xff])# Pulse c:blue for a while then keep old colour