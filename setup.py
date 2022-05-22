import setuptools


setuptools.setup(
    name='dofbot',
    version='1.0',
    description='Depth Of Field calculation Telegram Bot',
    author='github.com/devldavydov',
    packages=setuptools.find_packages(where='source'),
    package_dir={'': 'source'},
    include_package_data=True,
    install_requires=[
        'pyTelegramBotAPI==4.5.1'
    ],
    entry_points={'console_scripts': ['dofbot=dofbot.__main__:main']},
    python_requires=">=3.6"
)
