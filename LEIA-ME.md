# Diário das Emoções — app instalável

App de registro diário de sentimentos. Funciona offline, guarda tudo no próprio
aparelho e não envia nada para lugar nenhum.

## Arquivos

```
index.html              o app inteiro (interface + lógica)
manifest.webmanifest    identidade do app: nome, ícone, cor, modo de exibição
sw.js                   service worker: faz o app abrir sem internet
icons/                  ícones nos tamanhos exigidos pelo Android
gerar_icones.py         script que gerou os ícones (só se quiser trocar as cores)
```

## Instalação (GitHub Pages)

Para o Android oferecer "Instalar app", os arquivos precisam estar em um endereço
HTTPS. O GitHub Pages faz isso de graça e leva poucos minutos.

1. Crie um repositório novo no GitHub, público, com qualquer nome
   (ex.: `diario-emocoes`).
2. Envie todos os arquivos desta pasta para a raiz do repositório,
   preservando a pasta `icons/`.
3. No repositório: **Settings → Pages**. Em *Source*, escolha
   **Deploy from a branch**; em *Branch*, escolha `main` e a pasta `/ (root)`.
   Salve.
4. Aguarde 1 a 2 minutos. O endereço será:
   `https://SEU-USUARIO.github.io/diario-emocoes/`
5. Abra esse endereço no **Chrome do celular**. Vai aparecer a faixa
   "instalar" dentro do próprio app — toque nela. Se não aparecer, use o
   menu do Chrome (⋮) → **Instalar aplicativo**.

Pronto: o ícone fica na tela inicial e o app abre em tela cheia, sem barra de
navegador. Depois da primeira abertura, funciona sem internet.

### Atualizando o app

Se alterar qualquer arquivo, troque o número da versão no topo do `sw.js`
(`const VERSAO = 'diario-v1'` → `'diario-v2'`) antes de enviar. Sem isso o
celular continua usando a cópia antiga guardada em cache.

## Alternativa sem GitHub

Dá para usar sem hospedar: baixe os arquivos para o celular e abra o
`index.html` pelo Chrome digitando o caminho na barra de endereço
(ex.: `file:///sdcard/Documents/diario-app/index.html`), depois use
**Adicionar à tela inicial**.

Nesse modo funciona tudo, menos a instalação como app de verdade — fica um
atalho que abre no navegador. Abrir pelo gerenciador de arquivos em vez de
digitar o caminho pode gerar um endereço temporário e fazer os registros
sumirem entre uma abertura e outra; por isso o caminho digitado importa.

## Backup

O botão **salvar backup** gera um arquivo `.json` na pasta de downloads.
Guarde-o em algum lugar seguro de vez em quando: se você limpar os dados do
Chrome ou trocar de celular, é ele que traz seus registros de volta pelo botão
**restaurar backup**. A restauração mescla — não apaga o que já existe.

## Lembrete diário

O app não dispara notificações sozinho (isso exigiria um servidor). O lembrete
diário está configurado como alarme no próprio aparelho, às 21h.
