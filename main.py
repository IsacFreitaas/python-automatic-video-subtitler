# @isaczeitgeist

# LEGENDAR VÍDEOS AUTOMATICAMENTE
#          COM PYTHON!

# 1- TRANSCREVER O ÁUDIO.
# 2- GERAR AS LEGENDAS.
# 3- INSERIR AS LEGENDAS NO VÍDEO.
# 4- EXPORTAÇÃO.

import os
import sys
import pysrt

from faster_whisper import WhisperModel
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
# Requer a instalação avulsa do FFmpeg.

MAX_PALAVRAS = 5

PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))

FONT = os.path.join(
    PASTA_PROJETO,
    "assets",
    "fonts",
    "Coolvetica Rg.otf"
)

if not os.path.isfile(FONT):
    print("Erro: a fonte não foi encontrada em assets/fonts/")
    sys.exit(1)

SAIDA_SUFIXO = "_legendado"

print("Iniciando o processo...")


def formatar_tempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos = segundos % 60

    tempo = f"{horas:02}:{minutos:02}:{segundos:06.3f}"

    return tempo.replace(".", ",")


# Verifica se o vídeo foi informado
if len(sys.argv) != 2:
    print("Uso:")
    print("python3 main.py video.mp4")
    sys.exit(1)


VIDEO = sys.argv[1]

# Verifica se o vídeo existe
if not os.path.isfile(VIDEO):
    print(f'Erro: o arquivo "{VIDEO}" não foi encontrado.')
    sys.exit(1)


# Nome do arquivo de saída
nome, extensao = os.path.splitext(VIDEO)

SAIDA = f"{nome}{SAIDA_SUFIXO}{extensao}"

SRT = os.path.join(
    PASTA_PROJETO,
    "legendas.srt"
)


# WHISPER
print("Carregando modelo Whisper...")

model = WhisperModel(
    "medium",
    device="cpu",
    compute_type="int8"
)


# TRANSCRIÇÃO
print("Transcrevendo vídeo...")

segments, _ = model.transcribe(
    VIDEO,
    language="pt",
    beam_size=5,
    vad_filter=True,
    word_timestamps=True
)


# CRIANDO O SRT
print("Criando legendas...")

with open(SRT, "w", encoding="utf-8") as arquivo:

    numero = 1

    for segment in segments:

        palavras = []

        for palavra in segment.words:

            palavras.append(palavra)

            texto = " ".join(
                p.word.strip()
                for p in palavras
            )

            pontuacao = texto.endswith(
                (",", ".", "!", "?")
            )

            if (
                len(palavras) >= 3
                and pontuacao
            ) or len(palavras) >= MAX_PALAVRAS:

                inicio = formatar_tempo(
                    palavras[0].start
                )

                fim = formatar_tempo(
                    palavras[-1].end
                )

                arquivo.write(
                    f"{numero}\n"
                    f"{inicio} --> {fim}\n"
                    f"{texto}\n\n"
                )

                numero += 1
                palavras = []

        # Caso sobrem palavras no segmento
        if palavras:

            texto = " ".join(
                p.word.strip()
                for p in palavras
            )

            inicio = formatar_tempo(
                palavras[0].start
            )

            fim = formatar_tempo(
                palavras[-1].end
            )

            arquivo.write(
                f"{numero}\n"
                f"{inicio} --> {fim}\n"
                f"{texto}\n\n"
            )

            numero += 1


# ADICIONANDO AS LEGENDAS
print("Adicionando legendas ao vídeo...")

video = VideoFileClip(VIDEO)

largura, altura = video.size

clips = [video]


for legenda in pysrt.open(SRT):

    texto = TextClip(
        text=legenda.text,
        font=FONT,
        font_size=38,
        color="white",
        stroke_color="black",
        stroke_width=2,
        method="caption",
        size=(int(largura * 0.8), 140),
        text_align="center"
    )

    texto = (
        texto
        .with_start(
            legenda.start.ordinal / 1000
        )
        .with_end(
            legenda.end.ordinal / 1000
        )
        .with_position(
            ("center", altura * 0.85)
        )
    )

    clips.append(texto)


# JUNTANDO VÍDEO E LEGENDAS
video_final = CompositeVideoClip(clips)


# EXPORTAÇÃO
print("Exportando vídeo...")

video_final.write_videofile(
    SAIDA,
    codec="libx264",
    audio_codec="aac"
)


video.close()
video_final.close()


# Remove o SRT temporário
if os.path.exists(SRT):
    os.remove(SRT)


print()
print("Processo concluído!")
print(f"Vídeo salvo em: {SAIDA}")