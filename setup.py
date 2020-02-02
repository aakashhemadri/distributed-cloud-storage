import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="template-flask-restful",
    version="0.0.1",
    author="Aakash Hemadri",
    author_email="aakashhemadri123@gmail.com",
    description="A template flask-restful package",
    long_description="# A simple setup. - template-flask-restful",
    long_description_content_type="text/markdown",
    url="https://github.com/aakashhemadri/template-flask-restful",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)