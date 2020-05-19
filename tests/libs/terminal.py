from Naked.toolshed.shell import execute_js


def run_script(script_path, arguments):
    if len(arguments) > 0:
        js_command = "" + script_path + " " + arguments
    else:
        js_command = "" + script_path
    result = execute_js(js_command)
    if result:
        return True  # JavaScript is successfully executed
    else:
        return False  # JavaScript is failed
