from setuptools import setup, find_namespace_packages

base_packages = [
    "PyQt5",
    "pandas",
    "requests",
    "beautifulsoup4",
    "html5lib",
    "lxml",
]

dev_packages = [
    "pyqt5-tools"
]

setup(
    name='superz-qt-box',
    version='0.0.1',
    python_requires=">=3.8",
    package_dir={"": "src"},
    package_data={
        "": ["./images/**.*"]
    },
    packages=find_namespace_packages(where="./src"),
    install_requires=base_packages,
    extras_require={
        "mysql": ["pymysql"],
        "postgres": ["psycopg2"],
        "clickhouse": ["clickhouse_driver"],
        "doris": ["pymysql"]
    },
)
