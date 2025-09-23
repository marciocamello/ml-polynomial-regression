import os
import uvicorn

if __name__ == "__main__":
    # Render (e outras plataformas) definem a porta via variável de ambiente PORT
    port = int(os.environ.get("PORT", 10000))
    host = os.environ.get("HOST", "0.0.0.0")
    # No ambiente de desenvolvimento você pode continuar usando: python api_main.py
    uvicorn.run("api_modelo_salario:app", host=host, port=port, log_level="info")