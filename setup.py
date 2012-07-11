from setuptools import setup

setup(
    name='pingpong',
    version='0.0.1',
    
    author='James Robert',
    author_email='jiaaro@gmail.com',
    
    description=('Django library that makes triggering emails easier'),
    long_description=open('README.markdown').read(),
    
    license='MIT',
    keywords='django',
    
    install_requires=[
        "django",
    ],
    
    url="https://github.com/Rootbuzz/pingpong",

    packages=[
        'pingpong', 
        'pingpong.management',
        'pingpong.management.commands',
    ],
    
    include_package_data=True,
    
    classifiers=[
    	'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ]
)
