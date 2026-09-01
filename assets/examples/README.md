# Examples

Esta pasta contém um vídeo de entrada e o respectivo vídeo de saída gerado pelo **Python Automatic Video Subtitler**.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `video.mp4` | Vídeo original utilizado como entrada |
| `video_legendado.mp4` | Mesmo vídeo após a geração e inserção automática das legendas |

## Entrada → Saída

O processo recebe:

```text
video.mp4
```

e gera:

```text
video_legendado.mp4
```

O vídeo de saída contém legendas geradas automaticamente a partir do áudio do vídeo original utilizando **Faster-Whisper** e inseridas no vídeo com **MoviePy**.

## Reproduzindo o exemplo

A partir da pasta raiz do projeto, execute:

```bash
python3 main.py assets/examples/video.mp4
```

O programa irá processar o vídeo e gerar a versão legendada.

> **Observação:** o arquivo gerado será salvo de acordo com o padrão de nome definido no `main.py`.

## Objetivo

Esses arquivos servem como uma demonstração visual do funcionamento do projeto, permitindo comparar o vídeo original com o resultado após o processamento.

O `video.mp4` também pode ser utilizado para verificar se a instalação e o pipeline de geração automática de legendas estão funcionando corretamente.