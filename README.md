README.md
# 🚀 Win11-Optimizer-Lite

Um script leve em Python para otimização e limpeza rápida no Windows 11.

## 🧹 Funcionalidades

- **Limpeza de Arquivos Temporários:** Remove resíduos em `%TEMP%` e `C:\Windows\Temp`.
- **Esvaziamento da Lixeira:** Esvazia a Lixeira do Windows de forma silenciosa via PowerShell.
- **Flush de DNS:** Limpa o cache de DNS da rede (`ipconfig /flushdns`).
- **Otimização de Disco (TRIM):** Executa otimização na unidade `C:`.
- **Geração de Logs:** Salva o histórico de execuções no arquivo `optimization.log`.

## 🛠️ Como Executar

### Pré-requisitos
- Python 3.x instalado no Windows.
- Recomendado executar o terminal como **Administrador** para ter permissão total no sistema.

### Execução

```powershell
python optimizer.py
