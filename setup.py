from setuptools import setup, find_packages

setup(
    name="sports_biomechanics",
    version="0.1.0",
    description="A Python package for analyzing biomechanics data from videos",
    author="Kumarasinghege Nadeesha Piushan",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/sports_biomechanics",  # Update with your repository
    packages=find_packages(),  # Automatically find all modules in the project
    install_requires=[         # Dependencies
        "opencv-python",
        "mediapipe",
        "pandas",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',   # Minimum Python version required
)
