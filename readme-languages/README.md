# Download File Organizer

O script automatiza a organização da sua pasta de downloads.

## Instalação

Use o package manager [pip](https://pip.pypa.io/en/stable/) para instalar o **watchdog**.

```bash
pip install watchdog
```

## Como usar

Antes de tudo, você precisa clonar o repositório.

```sh
git clone https://github.com/CodeByGab/download-file-organizer.git
cd download-file-organizer
```

Agora, edite o caminho para a sua pasta de downloads. <br />
O exemplo dado é um diretório do Windows, mas você pode mudar o diretório para ser compatível com o seu Sistema Operacional.
```python
# Ponha aqui o diretório do seu Download
# Ou só o caminho que você quer organizar / observar

download_file_path = "C:\\Users\\{Seu-Usuario}\\{Seu}\\{Caminho}\\{Aqui}"
```
Então você pode rodar o script.
```bash
python3 fileOrganizer.py
```

Aperte `CTRL + C` no prompt para parar de rodar o script.

## Como rodar automaticamente no Windows

Se você quer rodar o código ao mesmo tempo que o Windows iniciar, siga os seguites passos:
- Aperte `win + r`
- Escreva `shell:startup` dentro da janela de **Executar**
- Copie o script para a pasta **Inicializar**
- Mude a extensão para `.pyw` ao invés de `.py` se você não quiser ver os prints no prompot (O programa vai rodar no background)
- **Opcional** - Converta o script para .exe <br />
Dica: rode o código primeiro com a extensão `.pyw` antes de reiniciar o seu computador, só para ter certeza que o código vai rodar corretamente.

## Contribuição

Pull requests são bem vinda. Para mudanças importantes, 
abra um issue primeiro para discutir o que gostaria de ser mudado

Certifique-se de atualizar os testes conforme apropriado.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)