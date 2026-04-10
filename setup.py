import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrapely-python-client",
    version="0.1.1",
    author="Scrapely",
    author_email="support@scrapely.io",
    description="Official Python client for Scrapely.io API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scrapely-io/scrapely-python-client",
    project_urls={
        "Bug Tracker": "https://github.com/scrapely-io/scrapely-python-client/issues",
        "Documentation": "https://docs.scrapely.io/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "httpx>=0.24.0",
    ],
    keywords=["web scraping", "crawler", "captcha solver", "scrapely", "api client", "captcha"],
)
