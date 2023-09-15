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

環境名を決めます。

```bash
jupyter-aca
```

```text
environment name '' is invalid (it should contain only alphanumeric characters and hyphens)
? Enter a new environment name: jupyter-aca
```

プレビューで確認します。

```bash
azd provision --preview
```

環境を構築します。リージョンは「9」を選択

```bash
azd provision
```

イメージをpushするときにはpush用のポリシーが必要なのでポータル上でポリシーをアタッチする。
最後にデプロイします。

```bash
azd deploy
```

## 片付け

```bash
azd down --force --purge
```

## Jupyterのコマンド

```bash
jupyter kernelspec list
```
