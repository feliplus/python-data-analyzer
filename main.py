#!/usr/bin/env python3
"""
Projeto de exemplo - Analisador de dados simples
"""

import requests
import json
from datetime import datetime

def fetch_github_user_info(username):
    """Busca informações públicas de um usuário GitHub"""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def analyze_user_data(user_data):
    """Analisa os dados do usuário"""
    if not user_data:
        return "Usuário não encontrado"
    
    analysis = {
        "nome": user_data.get("name", "N/A"),
        "repositorios_publicos": user_data.get("public_repos", 0),
        "seguidores": user_data.get("followers", 0),
        "seguindo": user_data.get("following", 0),
        "criado_em": user_data.get("created_at", "N/A")
    }
    
    return analysis

def main():
    print("🔍 Analisador de Perfil GitHub")
    username = input("Digite o username do GitHub: ")
    
    user_data = fetch_github_user_info(username)
    analysis = analyze_user_data(user_data)
    
    print("\n📊 Análise:")
    for key, value in analysis.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()

Commit simulado em 2022-02-18 12:00:00

Commit simulado em 2022-03-08 12:00:00

Commit simulado em 2022-05-19 12:00:00

Commit simulado em 2022-05-26 12:00:00

Commit simulado em 2022-06-08 12:00:00

Commit simulado em 2022-08-09 12:00:00

Commit simulado em 2022-03-02 12:00:00
