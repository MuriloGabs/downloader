# Downloader.py

Gerenciador interativo de downloads via terminal, com suporte a curl, wget, aria2c e MediaFire. Roda no Termux (Android) e no CachyOS / Arch Linux.

## Instalação

Termux (Android):

    pkg update
    pkg install python curl wget aria2 git

CachyOS / Arch Linux:

    sudo pacman -S python curl wget aria2 git

## Uso

    git clone https://github.com/SEU-USUARIO/downloader.git
    cd downloader
    chmod +x main.py

Crie o atalho global.

CachyOS:

    mkdir -p ~/.local/bin
    ln -s "$(pwd)/main.py" ~/.local/bin/dl

Termux:

    ln -s "$(pwd)/main.py" $PREFIX/bin/dl

Depois é só digitar `dl` de qualquer pasta.

## Fluxo

1. Escolha a ferramenta (curl, wget, aria2c ou mediafire)
2. Cole a URL
3. Escolha o destino (atual, último personalizado ou novo)
4. Selecione as flags desejadas
5. Confirme e o download começa

O caminho personalizado fica em cache em ~/.config/downloader/cache.json e aparece como "Último personalizado" na próxima execução.

## Arquitetura

    main.py                    # orquestrador (sem regra de negócio)
    modules/
    ├── types.py               # dataclasses compartilhadas
    ├── env.py                 # detecção de ambiente e binários
    ├── dirs.py                # resolução do diretório (case sensitive)
    ├── cache.py               # preferências em ~/.config/downloader/
    ├── ui.py                  # interação com o usuário
    ├── registry.py            # registro dos gerenciadores
    ├── curl/{flags,runner}.py
    ├── wget/{flags,runner}.py
    ├── aria2c/{flags,runner}.py
    └── mediafire/{flags,runner}.py

## Adicionar um novo gerenciador

1. Crie modules/<nome>/ com __init__.py, flags.py e runner.py seguindo o mesmo contrato (NAME, BINARY, listar_flags, montar, executar)
2. Adicione uma linha em modules/registry.py
3. Se depender de binário externo, adicione a entrada em modules/env.py

O main.py não precisa ser alterado — esse é o ponto do contrato plug-and-play.

## Sobre o MediaFire

O módulo mediafire resolve o link direto da página /file/.../file via scraping e delega o download ao aria2c. Se o MediaFire mudar a estrutura HTML, a regex em modules/mediafire/runner.py precisa ser ajustada.

## Licença

MIT — veja LICENSE.
