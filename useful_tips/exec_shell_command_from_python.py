"""
Execution of shell commands from the python file.
"""

import sys
import subprocess


# Installed python packages.
pip_pkg1 = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
pip_pkg_lst1 = pip_pkg1.decode("utf-8").split("\r\n")
# print(pip_pkg_lst1)

# Second version.
pip_pkg2 = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE)
pip_pkg_lst2 = pip_pkg2.stdout.decode("utf-8").split("\r\n")
# print(pip_pkg_lst2)

# ls -la command.
ls_la = subprocess.run(["ls", "-la"], stdout=subprocess.PIPE)
ls_ls_out = ls_la.stdout.decode("utf-8")
print(ls_ls_out)
