name = "houdini"
version = "18.5.596"
timestamp = 0o000000001

requires = [
    "python-3.7",
]
tools = [
    "pyside2-rcc",
    "rcc",
    "uic",
    "hbatch",
    "houdinifx",
    "hrender",
    "hscript",
    "hython",
]

variants = [["platform-windows"]]


def commands():
    # Set this variable to your houdini install path
    houdini_install_path = "D:/program/houdini_v18.5.596"

    env.PATH.append(f"{houdini_install_path}/bin")  # noqa
    env.PYTHONPATH.append(f"{houdini_install_path}/python37/lib/site-packages")  # noqa
    env.PYTHONPATH.append(f"{houdini_install_path}/houdini/python3.7libs")  # noqa
    env.PATH.append(f"{houdini_install_path}/toolkit/include")  # noqa
