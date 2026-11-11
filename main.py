#!/usr/bin/env python3
# main.py
"""
Downloader.py — orquestrador.

Só amarra os módulos. Nenhuma regra de negócio aqui.
"""

from modules import dirs, env, registry, ui


def main() -> int:
    ambiente = env.detectar()
    nome = ui.menu_ferramenta(ambiente)
    modulo = registry.obter(nome)

    url = ui.pedir_url()
    destino = dirs.resolver(ui.menu_destino())

    flags = ui.menu_flags(modulo.listar_flags())
    spec = modulo.montar(url, destino, flags)

    if not ui.confirmar(spec):
        print("Cancelado.")
        return 0

    return modulo.executar(spec)


if __name__ == "__main__":
    raise SystemExit(main())