name = "maya"
version = "2019.3"
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
    "maya",
    "mayabatch",
    "mayapy",
    "pyside2-rcc",
    "rcc",
    "shiboken2",
    "uconv",
    "uic",
]

variants = [["platform-windows"]]


def commands():
    # Set this variable to your maya install path
    maya_install_path = "D:/program/maya_v2019.3"

    env.PATH.append(f"{maya_install_path}/bin")  # noqa
    env.PYTHONPATH.append(f"{maya_install_path}/Python/Lib/site-packages")  # noqa
    env.QT_PLUGIN_PATH.append(f"{maya_install_path}/qt-plugins")  # noqa
    env.PATH.append(f"{maya_install_path}/devkit")  # noqa
    env.PATH.append(f"{maya_install_path}/include")  # noqa
