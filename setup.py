# Copyright 2021 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
from setuptools import find_packages

extras = {}
extras["quality"] = ["black ~= 22.0", "isort >= 5.5.4", "flake8 >= 3.8.3", "hf-doc-builder >= 0.3.0"]
extras["docs"] = []
extras["test_prod"] = ["pytest", "pytest-xdist", "pytest-subtests", "parameterized"]
extras["test_dev"] = ["datasets", "evaluate", "transformers", "scipy", "sklearn", "deepspeed<0.7.0", "tqdm"]
extras["testing"] = extras["test_prod"] + extras["test_dev"]
extras["rich"] = ["rich"]

extras["test_trackers"] = ["wandb", "comet-ml", "tensorboard"]
extras["dev"] = extras["quality"] + extras["testing"] + extras["rich"]

extras["sagemaker"] = [
    "sagemaker",  # boto3 is a required package in sagemaker
]

setup(
    name="accelerate",
    version="0.14.0.dev0",
    description="Accelerate",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="deep learning",
    license="Apache",
    author="The HuggingFace team",
    author_email="sylvain@huggingface.co",
    url="https://github.com/huggingface/accelerate",
    package_dir={"": "src"},
    packages=find_packages("src"),
    entry_points={
        "console_scripts": [
            "accelerate=accelerate.commands.accelerate_cli:main",
            "accelerate-config=accelerate.commands.config:main",
            "accelerate-launch=accelerate.commands.launch:main",
        ]
    },
    python_requires=">=3.7.0",
    install_requires=["numpy>=1.17", "packaging>=20.0", "psutil", "pyyaml", "torch>=1.4.0"],
    extras_require=extras,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)

# Release checklist
# 1. Change the version in __init__.py and setup.py.
# 2. Commit these changes with the message: "Release: VERSION"
# 3. Add a tag in git to mark the release: "git tag VERSION -m 'Adds tag VERSION for pypi' "
#    Push the tag to git: git push --tags origin main
# 4. Run the following commands in the top-level directory:
#      python setup.py bdist_wheel
#      python setup.py sdist
# 5. Upload the package to the pypi test server first:
#      twine upload dist/* -r pypitest
#      twine upload dist/* -r pypitest --repository-url=https://test.pypi.org/legacy/
# 6. Check that you can install it in a virtualenv by running:
#      pip install -i https://testpypi.python.org/pypi accelerate
#      accelerate env
#      accelerate test
# 7. Upload the final version to actual pypi:
#      twine upload dist/* -r pypi
# 8. Add release notes to the tag in github once everything is looking hunky-dory.
# 9. Update the version in __init__.py, setup.py to the new version "-dev" and push to master
