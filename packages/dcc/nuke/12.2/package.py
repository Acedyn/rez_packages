name = "nuke"
version = "12.2"
timestamp = 0o000000001

requires = [
    "python-2.7",
]
tools = [
    "designer",
    "fcheck",
    "imconvert",
    "imgcvt",
    "lconvert",
    "nuke11.3",
    "python",
    "pyside2-rcc",
    "rcc",
    "shiboken2",
    "uconv",
    "uic",
]


def commands():
    # Set this variable to your nuke install path
    nuke_install_path = "D:/program/nuke_v12.2"

    env.PATH.append(f"{nuke_install_path}")  # noqa
    env.PYTHONPATH.append(f"{nuke_install_path}/pythonextensions/site-packages")  # noqa
    env.QT_PLUGIN_PATH.append(f"{nuke_install_path}/qtplugins")  # noqa
    env.PATH.append(f"{nuke_install_path}/include")  # noqa
