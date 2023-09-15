# jupyter notebookをazd

## Azure CLIをインストール

```bash
sudo apt-get install azure-cli
```

リソースグループのリストを開く

```bash
az group list --query "[].{name:name}" --output json
```

```bash
az account list --query "[].{name:name, id:id}" --output json
```

```bash
az account list --query "[].{sub_id:id, name:name,user:user.name} | [? contains(name,'Pay-As-You-Go')]" --output json
```

※アサイニーはそのときどきでかわる。

```
az role assignment create --role "AcrPush" --resource-group "rg-jupyter-aca"
```

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
jupyter-notebook-aca-dev
```

```text
environment name '' is invalid (it should contain only alphanumeric characters and hyphens)
? Enter a new environment name: jupyter-notebook-aca-dev
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
