import re
import sys

def add_app_to_settings(app_name):
    settings_file = 'main/settings.py'
    app_config = f'{app_name}.apps.{app_name.capitalize()}Config'

    with open(settings_file, 'r') as file:
        content = file.read()

    new_content = re.sub(
        r'(INSTALLED_APPS *= *\[.*?)(\])',
        r"\1    '{}',\n\2".format(app_config),
        content,
        flags=re.DOTALL
    )

    with open(settings_file, 'w') as file:
        file.write(new_content)

    print(f"✔ {app_name} installed & added to settings.INSTALLED_APPS")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python update_settings.py <app_name>")
        sys.exit(1)

    add_app_to_settings(sys.argv[1])
