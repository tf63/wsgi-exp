FROM python:3.8

# コンテナのワークディレクトリを/appに指定
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true

# 非インタラクティブモードにする (入力待ちでブロックしなくなる)
ARG DEBIAN_FRONTEND=noninteractive

# UIDとGIDは外から与える
ARG USER_UID
ARG USER_GID

# コンテナ内でのユーザー名， グループ名
ARG USER_NAME=user
ARG GROUP_NAME=user

# グループが存在しなかったら，適当なグループを作成
RUN if ! getent group $USER_GID >/dev/null; then \
    groupadd -g $USER_GID $GROUP_NAME; \
    fi

# ユーザーを作成
RUN useradd -m -u $USER_UID -g $USER_GID -s /bin/bash $USER_NAME

# 初期ユーザーの変更
USER $USER_NAME

# pathを通す
ENV PATH="$PATH:/home/${USER_NAME}/.local/bin:/app/.venv/bin"

# poetryのインストール
RUN curl -sSL https://install.python-poetry.org | python -

# プロジェクト直下に.venvを作る
RUN poetry config virtualenvs.in-project true

