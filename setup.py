import re, sys, os, shutil, subprocess


def check_pyperclip():
    try:
        info = dict(
            tuple(i.split(': ')) for i in subprocess.check_output([
                sys.executable, '-m', 'pip', 'show', 'pyperclip'
            ]).decode().splitlines())
        return info
    except:
        return {}


def install_pyperclip_plugin():
    if info := check_pyperclip():
        if info['Version'] == '1.8.2':
            print('pyperclip 1.8.2 installed')
            src_path = os.path.abspath(__file__).replace(
                sys.argv[0], 'pyperclip182__init__.py')
            dst_path = f"{info['Location']}/pyperclip/__init__.py"
            try:
                shutil.copyfile(src_path, dst_path)
                return "Installed successfully!"
            except:
                pass
            return 'Installation Failed.\nCheck Github: https://github.com/knightz1224/termuxclip_plugin'
        return 'pyperclip 1.8.2 not installed'
    return 'pyperclip not installed'


if __name__ == "__main__":
    print(install_pyperclip_plugin())
