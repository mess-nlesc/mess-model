#!/usr/bin/env python

# Copyright (C) 2003-2007  Robey Pointer <robeypointer@gmail.com>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA.

# based on code provided by raymond mosteller (thanks!)

import base64
import getpass
import os
import socket
import sys
import traceback

import paramiko


# setup logging
paramiko.util.log_to_file("demo_sftp.log")

script_name = print(sys.argv[0])

# Paramiko client configuration
hostname= "localhost"
Port = 10022
username = "xenon"
remote_folder="demo_sftp_folder"
password = getpass.getpass('Enter your password: ')

# now, connect and use paramiko Transport to negotiate SSH2 across the connection
try:
    transport = paramiko.Transport((hostname, Port))
    transport.connect(
        username=username,
        password=password
    )
    sftp = paramiko.SFTPClient.from_transport(transport)

    # dirlist on remote host
    dirlist = sftp.listdir(".")
    print("Dirlist: %s" % dirlist)

    # copy this files onto the server
    # create a folder
    try:
        sftp.mkdir(remote_folder)
    except IOError:
        print(f"(assuming {remote_folder}/ already exists)")

    with sftp.open(f"{remote_folder}/README", "w") as f:
        f.write(f"This was created by {script_name}.\n")

    with open("requirements.txt", "r") as f:
        data = f.read()
    sftp.open("demo_sftp_folder/requirements.txt", "w").write(data)
    print("created demo_sftp_folder/ on the server")

    # # copy the README back here
    # with sftp.open("demo_sftp_folder/README", "r") as f:
    #     data = f.read()

    # with open("README_demo_sftp", "w") as f:
    #     f.write(data)
    # print("copied README back here")

    # # BETTER: use the get() and put() methods
    # sftp.put("demo_requirements.txt", "demo_sftp_folder/requirements.txt")
    # sftp.get("demo_sftp_folder/README", "README_demo_sftp")

    t.close()

except Exception as e:
    print("*** Caught exception: %s: %s" % (e.__class__, e))
    traceback.print_exc()
    try:
        t.close()
    except:
        pass
    sys.exit(1)