def init_termux_clipboard():
    """return a copy and paste function for Termux,
    a terminal application for Android.
    more information: https://termux.com/"""
    def copy_termux(text):
        p = subprocess.Popen('termux-clipboard-set',
                             stdin=subprocess.PIPE,
                             close_fds=True)
        p.communicate(input=text.encode('utf-8'))

    def paste_termux():
        p = subprocess.Popen('termux-clipboard-get',
                             stdout=subprocess.PIPE,
                             close_fds=True)
        stdout, stderr = p.communicate()
        return stdout.decode('utf-8')

    return copy_termux, paste_termux

    if _executable_exists("termux-clipboard-get"):
        return init_termux_clipboard()

    return init_no_clipboard()
