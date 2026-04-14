from setuptools import setup, find_packages

# ✅ 不要 import d2l 来取版本号（构建阶段容易失败）
VERSION = "0.0.1"

# ✅ Colab 友好：不要锁死老版本，避免触发降级/编译失败
install_requires = [
    "numpy>=1.21",         # 或者直接 "numpy"
    "matplotlib>=3.5",
    "requests>=2.25",
    "pandas>=1.2",
]

# ✅ 把 notebook 环境相关依赖放到 extras（Colab 不需要装 jupyter）
extras_require = {
    "notebook": ["jupyter>=1.0.0"],
    # 如果你确实需要 torch 相关（看你 torch.py 是否 import torch/torchvision）
    "torch": ["torch", "torchvision", "pillow", "ipython"],
}

setup(
    name="d2l",  # 如果你怕跟官方 d2l 冲突，可改成 "myd2l"
    version=VERSION,
    python_requires=">=3.8",  # ✅ Colab 通常 3.10+，建议提高下限
    author="D2L Developers",
    author_email="d2l.devs@gmail.com",
    url="https://d2l.ai",
    description="Dive into Deep Learning (custom build for Colab)",
    license="MIT-0",
    packages=find_packages(),
    zip_safe=True,
    install_requires=install_requires,
    extras_require=extras_require,
)
