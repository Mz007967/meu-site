from flask import Flask

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Meu Site | Python</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #020b20;
            color: white;
            overflow-x: hidden;
        }

        /* FUNDO */
        body::before {
            content: "";
            position: fixed;
            width: 500px;
            height: 500px;
            background: #1264ff;
            filter: blur(180px);
            opacity: 0.18;
            top: -150px;
            right: -150px;
            pointer-events: none;
        }

        body::after {
            content: "";
            position: fixed;
            width: 400px;
            height: 400px;
            background: #5b21ff;
            filter: blur(180px);
            opacity: 0.15;
            bottom: -150px;
            left: -150px;
            pointer-events: none;
        }

        /* MENU */
        nav {
            position: sticky;
            top: 0;
            z-index: 1000;

            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 18px 6%;

            background: rgba(2, 11, 32, 0.82);
            backdrop-filter: blur(15px);

            border-bottom: 1px solid rgba(80, 140, 255, 0.15);
        }

        .logo {
            font-size: 25px;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .logo span {
            color: #3185ff;
        }

        .menu {
            display: flex;
            align-items: center;
            gap: 28px;
        }

        .menu a {
            color: #cbd8f5;
            text-decoration: none;
            font-size: 15px;
            transition: 0.3s;
        }

        .menu a:hover {
            color: #3b8cff;
        }

        .menu-button {
            background: linear-gradient(135deg, #087cff, #3155ff);
            color: white !important;
            padding: 12px 22px;
            border-radius: 30px;
            font-weight: bold;
            box-shadow: 0 8px 25px rgba(0, 100, 255, 0.25);
        }

        /* HERO */
        .hero {
            min-height: 720px;
            padding: 90px 7% 70px;

            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 50px;

            position: relative;
        }

        .hero-content {
            max-width: 620px;
        }

        .tag {
            display: inline-block;

            padding: 10px 18px;
            margin-bottom: 25px;

            border: 1px solid rgba(50, 130, 255, 0.6);
            border-radius: 30px;

            background: rgba(20, 90, 200, 0.12);
            color: #8fc1ff;

            font-size: 14px;
        }

        h1 {
            font-size: clamp(48px, 7vw, 78px);
            line-height: 0.98;
            margin-bottom: 28px;
            letter-spacing: -3px;
        }

        h1 span {
            color: #287cff;
        }

        .hero-text {
            color: #aebfe4;
            font-size: 19px;
            line-height: 1.7;
            max-width: 560px;
        }

        .buttons {
            display: flex;
            gap: 15px;
            margin-top: 35px;
            flex-wrap: wrap;
        }

        .btn {
            text-decoration: none;
            padding: 16px 28px;
            border-radius: 35px;
            font-weight: bold;
            font-size: 16px;
            transition: 0.3s;
        }

        .btn-primary {
            color: white;
            background: linear-gradient(135deg, #087cff, #3155ff);
            box-shadow: 0 12px 30px rgba(0, 100, 255, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 18px 35px rgba(0, 100, 255, 0.45);
        }

        .btn-secondary {
            color: #dbe7ff;
            border: 1px solid #3b73db;
        }

        .btn-secondary:hover {
            background: rgba(50, 120, 255, 0.1);
        }

        /* ILUSTRAÇÃO */
        .visual {
            width: 440px;
            max-width: 100%;
            position: relative;
        }

        .python {
            position: absolute;
            top: -80px;
            right: 30px;

            font-size: 90px;

            filter: drop-shadow(0 0 20px rgba(0, 140, 255, 0.4));
        }

        .laptop {
            background: linear-gradient(145deg, #14284d, #02091c);
            border: 2px solid #287cff;
            border-radius: 18px;

            padding: 25px;

            box-shadow:
                0 0 30px rgba(0, 110, 255, 0.3),
                0 30px 70px rgba(0, 0, 0, 0.5);

            transform: rotate(-3deg);
        }

        .screen {
            height: 220px;
            border-radius: 10px;
            background: #030b1d;
            border: 1px solid #1d477e;

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 70px;
            color: #1597ff;
        }

        .laptop-base {
            height: 15px;
            width: 115%;
            margin-left: -7.5%;
            margin-top: 10px;

            border-radius: 0 0 20px 20px;
            background: linear-gradient(90deg, #17366b, #4d7cff, #17366b);
        }

        /* RECURSOS */
        .features {
            padding: 90px 7%;

            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;

            border-top: 1px solid rgba(80, 140, 255, 0.12);
        }

        .card {
            padding: 35px 28px;

            background: rgba(8, 24, 55, 0.65);
            border: 1px solid rgba(80, 140, 255, 0.16);
            border-radius: 25px;

            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);
            border-color: rgba(60, 140, 255, 0.5);
            box-shadow: 0 20px 50px rgba(0, 80, 255, 0.12);
        }

        .icon {
            width: 60px;
            height: 60px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 50%;

            background: linear-gradient(135deg, #073da8, #4a27d8);

            font-size: 27px;
            margin-bottom: 22px;
        }

        .card h2 {
            margin-bottom: 12px;
            font-size: 22px;
        }

        .card p {
            color: #9db2dc;
            line-height: 1.7;
        }

        /* SOBRE */
        .about {
            padding: 100px 7%;
            text-align: center;

            background: linear-gradient(
                180deg,
                transparent,
                rgba(10, 50, 130, 0.18),
                transparent
            );
        }

        .about h2 {
            font-size: 40px;
            margin-bottom: 20px;
        }

        .about p {
            max-width: 700px;
            margin: auto;
            color: #aebfe4;
            line-height: 1.8;
            font-size: 17px;
        }

        /* FOOTER */
        footer {
            text-align: center;
            padding: 35px 20px;

            color: #7185ae;
            border-top: 1px solid rgba(80, 140, 255, 0.12);
        }

        /* MOBILE */
        @media (max-width: 800px) {

            nav {
                padding: 16px 5%;
            }

            .menu a:not(.menu-button) {
                display: none;
            }

            .hero {
                min-height: auto;
                padding: 70px 6% 80px;

                flex-direction: column;
                text-align: center;
            }

            .hero-content {
                max-width: 100%;
            }

            h1 {
                font-size: 52px;
                letter-spacing: -2px;
            }

            .hero-text {
                font-size: 17px;
            }

            .buttons {
                justify-content: center;
            }

            .visual {
                margin-top: 50px;
                width: 340px;
            }

            .python {
                font-size: 65px;
                top: -55px;
                right: 5px;
            }

            .screen {
                height: 180px;
                font-size: 55px;
            }

            .features {
                grid-template-columns: 1fr;
                padding: 70px 6%;
            }

            .about {
                padding: 80px 6%;
            }

            .about h2 {
                font-size: 32px;
            }
        }
    </style>
</head>

<body>

    <!-- MENU -->
    <nav>
        <div class="logo">
            🚀 Meu <span>Site</span>
        </div>

        <div class="menu">
            <a href="#inicio">Início</a>
            <a href="#sobre">Sobre</a>
            <a href="#recursos">Recursos</a>
            <a href="#inicio" class="menu-button">Começar</a>
        </div>
    </nav>


    <!-- HERO -->
    <section class="hero" id="inicio">

        <div class="hero-content">

            <div class="tag">
                🚀 Projeto criado no celular
            </div>

            <h1>
                Meu primeiro<br>
                <span>site!</span>
            </h1>

            <p class="hero-text">
                Esse site foi criado com Python pelo celular.
                É só o começo de uma grande jornada! 🚀
            </p>

            <div class="buttons">
                <a href="#recursos" class="btn btn-primary">
                    Começar →
                </a>

                <a href="#sobre" class="btn btn-secondary">
                    Saiba mais
                </a>
            </div>

        </div>


        <div class="visual">

            <div class="python">
                🐍
            </div>

            <div class="laptop">

                <div class="screen">
                    &lt;/&gt;
                </div>

                <div class="laptop-base"></div>

            </div>

        </div>

    </section>


    <!-- RECURSOS -->
    <section class="features" id="recursos">

        <div class="card">

            <div class="icon">⚡</div>

            <h2>Rápido e leve</h2>

            <p>
                Um site moderno, direto e otimizado
                para funcionar muito bem no celular.
            </p>

        </div>


        <div class="card">

            <div class="icon">&lt;/&gt;</div>

            <h2>Feito com Python</h2>

            <p>
                Desenvolvido usando Flask,
                uma ferramenta poderosa para criar sites.
            </p>

        </div>


        <div class="card">

            <div class="icon">📱</div>

            <h2>100% no celular</h2>

            <p>
                Desenvolvido e testado diretamente
                no Android usando Termux.
            </p>

        </div>

    </section>


    <!-- SOBRE -->
    <section class="about" id="sobre">

        <h2>Começando uma nova jornada 🚀</h2>

        <p>
            Esse é o meu primeiro projeto web usando Python.
            A ideia é aprender programação, criar projetos
            cada vez melhores e transformar ideias em sites
            de verdade.
        </p>

    </section>


    <!-- RODAPÉ -->
    <footer>
        © 2026 Meu Site • Criado com Python + Flask 🐍
    </footer>

</body>
</html>
"""


@app.route("/")
def inicio():
    return HTML


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
