import warnings


def check_installed_packages(package_descriptions):
    installed_dict = {}
    for name, desc in package_descriptions.items():
        try:
            exec(f"import {name}")
            installed_dict[name] = True
        except ModuleNotFoundError:
            warnings.warn(f'Package "{name}" is not found. {desc}')
            installed_dict[name] = False
    return installed_dict


PACKAGE_DESCRIPTION = {
    'pandas': "The package is used to create a FormalContext based on pandas.DataFrame and vice versa",
    'tqdm': "The package helps to track the progress of looped functions and estimate their time to complete"
}
LIB_INSTALLED = check_installed_packages(PACKAGE_DESCRIPTION)
