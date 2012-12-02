# -*- coding: utf-8 -*-

# A script to spam a series of messages in an irc channel

# Copyright (c) 2012 Ivan Sichmann Freitas, Sergio Durigan Junior

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import weechat as w
import re

w.register("add_join", "Ivan Sichmann Freitas, Sergio Durigan Junior", "0.1", "GPL3",
           "Add a channel to the autojoin list", "", "")

def append_channel(data, buffer, args):
    buffer_name = w.buffer_get_string(buffer, "short_name")
    server_name = w.buffer_get_string(buffer, "name").split(".")[0]
    config = "irc.server.%s.autojoin" % (server_name)
    channels = w.config_string(w.config_get(config))
    if (args != "" and args in channels) or (buffer_name in channels):
        w.prnt ('', "The channel %s is already present in the list." % buffer_name)
        return w.WEECHAT_RC_OK
    if args == "":
        channels = channels + "," + buffer_name
    else:
        channels = channels + "," + args
    w.command('', "/set irc.server.%s.autojoin %s" % (server_name, channels))

    return w.WEECHAT_RC_OK

w.hook_command("append_join",
               "Append a channel to the autojoin list",
               "[<channel>]",
               "channel: name of the appended channel\n"
               "without arguments add the current buffer",
               "",
               "append_channel",
               "")
