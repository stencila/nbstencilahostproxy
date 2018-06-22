import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='nbstencilahostproxy',
    version='0.1.0',
    author='Nokome Bentley',
    description='Proxy to a Stencila Host from a Jupyter Notebook server',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/stencila/nbstencilahostproxy',
    packages=setuptools.find_packages(),
    keywords=['Jupyter', 'Stencila'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Framework :: Jupyter',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering'
    ],
    install_requires=[
        'nbserverproxy'
    ]
)
