# -*- coding: utf-8 -*-

#import subprocess
from i3pystatus import Status
from i3pystatus.mail import maildir

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %d %b %T",)

status.register("xkblayout",
    layouts=["es", "us"])
status.register("mem_bar")
status.register("cpu_usage_bar")

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load",
    format="{avg1}",
    critical_limit=2)

# Shows your CPU temperature, if you have a Intel CPU
#status.register("temp",
#    format="{temp:.0f}°C",)

# Network traffic
#status.register("network_traffic",
#    interface="em1")
#status.register("network_graph",
#    interface="em1")

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="eno1",
    format_up="{v4cidr}",)

# Has all the options of the normal network and adds some wireless specific things
# like quality and network names.
#
# Note: requires both netifaces and basiciw
#status.register("wireless",
#    interface="wlan0",
#    format_up="{essid} {quality:03.0f}%",)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/home",
    format="/home [{avail}G]",)

status.register("disk",
    path="/",
#    format="/ {used}/{total}G [{avail}G]",)
    format="/ [{avail}G]",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("alsa",
    format="♪{volume}",)

# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
status.register("mpd",
    format="{title}{status}{album}",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },
    log_level=0,)

status.register("mail",
    format="{unread} new emails",
    backends=[
        maildir.MaildirMail(
            account="Account",
            directory="/home/ismaelpf/Mail/account/INBOX/"
        )
    ])

status.run()
