demo1
├── data
│   └── user.json
├── docs
│   └── history.md
├── pyproject.toml
├── src
│   ├── requests
│   │   └── __init__.py
│   └── sample
│       ├── __init__.py
│       ├── user
│       │   └── __init__.py
│       └── views
│           └── __init__.py
├── tests
│   ├── __init__.py
│   ├── user
│   │   └── __init__.py
│   └── views
│       └── __init__.py
└── tox.ini

# Poetry 是一个用于管理 Python 项目的依赖、虚拟环境、打包和发布的工具，适用于库和应用的开发。
# 创建一个新的 Python 项目结构
pip3 install poetry
# 在现有目录中交互式创建 pyproject.toml 文件
# 创建项目
poetry new my-app
# 进入项目目录
cd my-app
# 添加依赖
poetry add requests flask
# 添加开发依赖
poetry add --dev pytest flake8
# 查看已安装包
poetry show
# 构建项目包
poetry build
# 发布到 PyPI（需提前配置 token）
poetry publish

# 安装分发包
pip3 install dist/your_package-0.1.0-py3-none-any.whl
python -m my_package.main

# demo1为例，在项目根目录执行，开发环境下直接执行
poetry run python src/demo1/hello/main.py

