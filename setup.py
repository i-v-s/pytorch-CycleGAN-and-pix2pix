from setuptools import setup, find_packages

setup(
      name='cyclegan_p2p',
      version='0.0.1',
      install_requires=[
            'dominate', 'visdom', 'wandb'
      ],
      packages=find_packages()
)
