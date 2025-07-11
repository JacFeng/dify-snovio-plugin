from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI(
    title="Snovio Plugin API",
    description="Dify插件，用于获取Snovio access_token和查找域名邮箱",
    version="1.6.0"
)

# 允许跨域，方便本地调试
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SNOVIO_CLIENT_ID = "9e4c7d6e309cb4064a4d942a16ff8b88"
SNOVIO_CLIENT_SECRET = "8c77fdb4f359f8ca9883a87860ac9b61"

@app.post("/v1/oauth/access_token")
def get_access_token(
    client_id: str = Form(SNOVIO_CLIENT_ID),
    client_secret: str = Form(SNOVIO_CLIENT_SECRET),
    grant_type: str = Form("client_credentials")
):
    url = "https://api.snov.io/v1/oauth/access_token"
    data = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret
    }
    resp = requests.post(url, data=data, timeout=10)
    return resp.json()

@app.post("/v1/get-domain-emails-with-info")
def get_domain_emails(
    access_token: str = Form(...),
    domain: str = Form(...)
):
    url = "https://api.snov.io/v1/get-domain-emails-with-info"
    data = {
        "access_token": access_token,
        "domain": domain
    }
    resp = requests.post(url, json=data, timeout=10)
    return resp.json()
