from setuptools import setup, find_packages
import versioneer
import os

def main():
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, 'README.md'), 'r') as f:
        long_description = f.read()

    setup(
        name='rpi_vidlooper',
        version=versioneer.get_version(),
        description='Raspberry Pi GPIO-controlled video looper',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Alex Lubbock',
        author_email='code@alexlubbock.com',
        packages=find_packages(),
        install_requires=['RPi.GPIO'],
        cmdclass=versioneer.get_cmdclass(),
        zip_safe=True,
        entry_points = {
            'console_scripts': ['vidlooper=rpi_vidlooper.vidlooper:main']
        }
    )


if __name__ == '__main__':
    main()
