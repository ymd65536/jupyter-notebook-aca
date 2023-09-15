# jupyter notebookをazd

## Azureにデプロイ

認証します。

```bash
azd auth login
```

プロジェクトをビルドします。

```bash
azd package
```

環境を構築します。

```bash
azd provision
```

イメージをpushするときにはpush用のポリシーが必要なのでポータル上でポリシーをアタッチする。
最後にデプロイします。

```bash
azd deploy
```

## Jupyterのコマンド

```bash
jupyter kernelspec list
```
