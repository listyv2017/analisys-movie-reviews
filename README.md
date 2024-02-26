# analisys-movie-reviews
映画のレビューサイトのコメント欄から感情分析を行うWebアプリケーション


このプロジェクトでは、[pyenv](https://github.com/pyenv/pyenv)と[Poetry](https://python-poetry.org/)を使用してPythonのバージョン管理と依存関係の管理を行っています。

# poetryのインストール方法

この手順では、poetryをインストールし環境変数を設定する方法を説明します。

## インストール手順

poetryはプロジェクトの依存関係の管理を行うツールです。
以下のコマンドを使用して、poetryのインストールスクリプトを実行します。

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 環境変数の設定

環境変数の設定と`poetry`コマンドをパスに追加するために、`.bashrc`に次の内容を追加してください。

```bash
export POETRY_HOME="$HOME/.poetry"
export PATH="$POETRY_HOME/bin:$PATH"
```

これにより、poetryコマンドが実行可能な状態になります。.bash_profileにはこれらの設定は不要です。

最後に、変更を反映させるために、新しいターミナルを開いて、.bashrcを再読み込みするか、次のようにして反映させます。

```bash
source ~/.bashrc
```

### インストールの確認
以下のコマンドを使用してpoetryが正しくインストールされているか確認できます。

```bash
poetry --version
```

バージョン番号が表示されれば、poetryのインストールは成功です。

これで、poetryコマンドが使用可能な状態になります。



# pyenvのインストール方法

この手順では、pyenvをインストールし環境変数を設定する方法を説明します。

## インストール手順

poetryは複数のPythonバージョンの管理を容易にするためのツールです。
以下のコマンドを使用して、pyenvのインストールスクリプトをダウンロードします。

```bash
curl https://pyenv.run | bash
```


### 環境変数の設定

環境変数の設定のために、`.bashrc`に次の内容を追加してください。

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```


最後に、変更を反映させるために、新しいターミナルを開いて、.bashrcを再読み込みするか、次のようにして反映させます。

```bash
source ~/.bashrc
```

### インストールの確認
以下のコマンドを使用してpyenvが正しくインストールされているか確認できます。

```bash
pyenv --version
```

バージョン番号が表示されれば、pyenvのインストールは成功です。


