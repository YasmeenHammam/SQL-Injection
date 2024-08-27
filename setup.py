from setuptools import setup, find_packages

setup(
    name='sql_injection_detector',
    version='0.1.0',
    description='A SQL injection detector package using Flask',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yasmeen',
    author_email='hammamyasmeen7@gmail.com',
    url='https://github.com/YasmeenHammam/SQL-Injection',
    packages=find_packages(),
    install_requires=[
        'Flask==3.0.3',
        'blinker==1.8.2',
        'click==8.1.7',
        'colorama==0.4.6',
        'Flask==3.0.3',
        'gunicorn==23.0.0',
        'itsdangerous==2.2.0',
        'Jinja2==3.1.4',
        'MarkupSafe==2.1.5',
        'packaging==24.1',
        'Werkzeug==3.0.3',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'run-sql-injection-detector=sql_injection_detector.app:run_app',
        ],
    },
)
