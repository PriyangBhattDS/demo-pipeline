from setuptools import setup,find_packages
setup(name="census-income",
      version="0.0.1",
      author="priyang bhatt",
      author_email="priyangbhatt@gcet.ac.in",
      packages=find_packages(),
      install_requirements=["pandas","numpy","flask"]
      )
