#!/usr/bin/env python3
#------------------------------------------------------------------------------
# DRAT Prototype Tool Source Code
# 
# Copyright 2019 Carnegie Mellon University. All Rights Reserved.
# 
# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING 
# INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON
# UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS
# TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE
# OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE
# MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND
# WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
# 
# Released under a MIT (SEI)-style license, please see license.txt or contact
# permission@sei.cmu.edu for full terms.
# 
# [DISTRIBUTION STATEMENT A] This material has been approved for public
# release and unlimited distribution.  Please see Copyright notice for non-US
# Government use and distribution.
# 
# This Software includes and/or makes use of the following Third-Party
# Software subject to its own license:
# 
# 1. Python 3.7 (https://docs.python.org/3/license.html)
# Copyright 2001-2019 Python Software Foundation.
# 
# 2. SQL Alchemy (https://github.com/sqlalchemy/sqlalchemy/blob/master/LICENSE)
# Copyright 2005-2019 SQLAlchemy authors and contributor.
# 
# DM19-0055
#------------------------------------------------------------------------------

"""
Main script for DRAT Tool.
"""
from subprocess import call
import utils.os
from utils.session import State


def main():
    args = utils.os.GetArguments().parse()
    
    # Require one argument - name of configuration file
    conf_file = args.name
    with open(conf_file) as f:
        gather_args = f.read()
    f.close()
    gather_args = gather_args.splitlines()
    
    # Each line in the configuration file is an argument string for gather.py
    # One line per system to gather and analyze.
    for line in gather_args:
        # support commenting-out a line
        if not line[0] == '#':
            name = line.strip().split(" ")[-1]

            print(f"System name: {name}")

            print("Running gather.py")
            cmd = line.strip().split(" ")
            cmd.insert(0, "./gather.py")
            call(cmd)
    
            # load_details.py just wants the system name (no SSH connection)
            # This is a hack - we assume that the last word in each gather
            # argument is the system name.
            print("Running load_details.py")
            call(["./load_details.py", name])
    
            # run_analysis.py takes the full configuration string
            print("Running run_analysis.py")
            cmd = line.rstrip().split(" ")
            call(["./run_analysis.py", name])

            # generate ansible yaml
            print("Running generate.py")
            call(["./generate.py", "-o output", name])


if __name__ == '__main__':
    # Initialize the global database session
    State.startup(action=main)
