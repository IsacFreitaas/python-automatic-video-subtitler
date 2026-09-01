### Automatic Video Subtitler! ㏄
# Gere Legendas De Qualquer Vídeo Automaticamente com Python!

Com esta ferramenta você vai conseguir gerar **legendas** **automaticamente** a partir de um vídeo utilizando `Python`, `Whisper` e incorporá-las diretamente ao vídeo com `MoviePy`. 👨🏻‍💻

Este projeto foi desenvolvido com o objetivo de automatizar uma parte do processo de edição de vídeo, te possibilitando **legendar** um **vídeo** através de um **único** comando no Terminal. 🧠

# 🚀 Tecnologias utilizadas

- [Python](https://www.python.org)
- [Whisper (faster-whisper)](https://pypi.org/project/faster-whisper/)
- [MoviePy](https://pypi.org/project/moviepy/)
- [FFmpeg](https://www.ffmpeg.org)

# ⚙️ Recursos

- **Execução** através de um **único comando** no Terminal.

- **Transcrição automática** do áudio **do vídeo** com `Whisper`, com a identificação do momento em que cada palavra é falada.

- **Geração automática** de um **arquivo .srt** (*legenda*), com divisão de legendas por pontuação e quantidade pré-definida de palavras.

- **Renderização** das legendas **diretamente no vídeo**, com texto centralizado com contorno para facilitar a leitura e **exportação do vídeo final** utilizando `MoviePy` e `FFmpeg`.

# 📦 Instalação

### No **Terminal**, clone o repositório:

```bash
git clone https://github.com/IsacFreitaas/python-automatic-video-subtitler.git
```

### Entre na **pasta** do projeto:

```bash
cd python-automatic-video-subtitler
```

### **Crie** e **ative** o [**Ambiente Virtual:**](https://youtu.be/kyiLBafjpMQ)


```bash
python3 -m venv venv
```

### MacOS X / Linux:

```bash
source venv/bin/activate
```

### Windows:

```bash
venv\Scripts\activate
```

### 📦 Instale as dependências:

```bash
pip3 install -r requirements.txt
```

*Também é necessário instalar o **FFmpeg** e adicioná-lo ao **PATH** do sistema.

#### Para isso, siga os comandos:


Em distribuições **Linux**: 
```bash
sudo apt update && sudo apt install ffmpeg
```

No **MacOS X** (com o brew instalado):
```bash
brew install ffmpeg
```

#### Já no **Windows**, entre no site e faça o download: https://www.ffmpeg.org

# 🧠 Como usar

### **no Terminal, na pasta do projeto:**

```bash
python3 main.py nome_do_video.mp4*
```

- Ao invés de "`nome_do_video.mp4`", coloque o **local do seu vídeo** e a extensão do arquivo.

### Então o programa irá:

1. **Carregar** o modelo **Whisper**;

2. **Transcrever** o áudio do **vídeo**;

3. Identificar os **timestamps** das palavras;

4. Criar o **arquivo de legendas** `.srt`;

5. **Dividir as legendas** em blocos menores (como foi pré-definido);

6. **Renderizar as legendas sobre o vídeo**;

7. **Exportar o vídeo final**.

### O arquivo de saída será criado automaticamente no mesmo diretório do vídeo:

```bash
nome_do_arquivo_legendado.mp4*
```

# ➡️ Como as legendas são divididas?

#### O projeto utiliza os **timestamps individuais** fornecidos pelo `Whisper` para construir legendas menores e **sincronizadas** com a **fala**.

Uma nova legenda é criada quando:

- existem pelo menos **3 palavras** e/ou o texto termina com `,`, `.`, `?` ou `!`;

- ou o bloco chega a **5 palavras** (que é o máximo pré-definido).

#### Isso evita manter frases **muito longas** na tela e permite que cada **legenda** utilize o **momento real** em que as palavras foram **pronunciadas**.

# ⚙️ Fluxo do projeto:


                    Vídeo
                      │
                      ▼
               faster-whisper
                      │
                      ▼
            Transcrição + timestamps
                      │
                      ▼
               Geração do .srt
                      │
                      ▼
              Leitura com pysrt
                      │
                      ▼
          Insere no vídeo com MoviePy
                      │
                      ▼
               Vídeo legendado

# ⚠️ Observações

#### Atualmente, por padrão, o **modelo de transcrição** utilizado é o **medium**, configurado para execução em **CPU**:

    WhisperModel(
        "medium",
        device="cpu",
        compute_type="int8"
    )

#### Modelos maiores e melhores podem oferecer **maior qualidade** de transcrição, mas também exigem mais **recursos computacionais** e **tempo de processamento**.

#### A velocidade e a qualidade da transcrição podem variar de acordo com o hardware, qualidade do áudio e características do vídeo.

# 🎥 Este projeto é relacionado ao conteúdo do canal

#### Este **projeto** faz parte de uma série de **conteúdos** sobre automação utilizando **Python**, mostrando como tarefas normalmente realizadas **manualmente** podem ser **automatizadas** através de **programação**.

#### **Documentei** **todo o processo**, mostrando a **construção** **do projeto** e **explicando** **na prática**, no momento da **construção inicial do projeto** no vídeo do YouTube. Confere lá: [Clique aqui.](https://youtu.be/va4TGsFv0p0) ⬅️

## 👨🏻‍💻 Sobre mim:

<p align="left"> <a href="https://www.youtube.com/@isaczeitgeist"> <img src="https://github.com/IsacFreitaas.png" width="145" alt="Meu perfil"> </a> <img src="https://github.com/IsacFreitaas/IsacFreitaas/assets/65254733/00d94d72-7789-4961-b1b2-d0313bc80b48" width="218" ></img> </p>

# [Isac Freitas](https://www.instagram.com/isaczeitgeist)


### Desenvolvedor **Python** | **Backend** & **Ciência de Dados** | **APIs** e **Automação** | Simplificando Python e transformando código em aplicações reais






### ➡️ Me encontre nas redes sociais: [https://inktr.ee/isaczeitgeistpy](https://linktr.ee/isaczeitgeistpy)



---

**Obrigado pela atenção!**