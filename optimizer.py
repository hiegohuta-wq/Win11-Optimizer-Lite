import os
import shutil
import subprocess
import ctypes
import sys
from datetime import datetime

def is_admin():
    """Verifica se o script está a ser executado como Administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def log(msg):
    """Exibe no terminal e regista a mensagem num log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {msg}"
    print(formatted_msg)
    with open("optimization.log", "a", encoding="utf-8") as f:
        f.write(formatted_msg + "\n")

def clear_temp_folders():
    """Limpa diretórios de ficheiros temporários no Windows."""
    log("🧹 A iniciar limpeza de ficheiros temporários...")
    temp_dirs = [
        os.environ.get('TEMP'),
        os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp')
    ]
    
    total_cleaned = 0
    for temp_dir in temp_dirs:
        if not temp_dir or not os.path.exists(temp_dir):
            continue
        
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(file_path)
                    os.remove(file_path)
                    total_cleaned += file_size
                except Exception:
                    pass  # Ficheiro em uso pelo sistema

    mb_cleaned = round(total_cleaned / (1024 * 1024), 2)
    log(f"✅ Limpeza concluída! Liberados aproximadamente {mb_cleaned} MB.")

def empty_recycle_bin():
    """Esvazia a reciclagem do Windows via PowerShell."""
    log("🗑️ A esvaziar a Reciclagem...")
    try:
        cmd = "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"
        subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        log("✅ Reciclagem esvaziada com sucesso.")
    except Exception as e:
        log(f"⚠️ Erro ao esvaziar a reciclagem: {e}")

def flush_dns():
    """Limpa a cache de DNS da rede."""
    log("🌐 A efetuar Flush do DNS...")
    try:
        subprocess.run(["ipconfig", "/flushdns"], capture_output=True, check=True)
        log("✅ Cache de DNS limpa com sucesso.")
    except Exception as e:
        log(f"⚠️ Erro ao limpar a cache de DNS: {e}")

def optimize_drives():
    """Executa a otimização de disco/SSD (TRIM)."""
    log("💾 A otimizar unidades de disco (TRIM/Defrag)...")
    try:
        subprocess.run(["defrag", "C:", "/O"], capture_output=True, check=True)
        log("✅ Otimização da unidade C: efetuada.")
    except Exception as e:
        log("⚠️ Não foi possível otimizar o disco (requer privilégios de Administrador).")

def main():
    print("=" * 50)
    print("🚀 Windows 11 Quick Optimizer & Cleaner Lite")
    print("=" * 50)
    
    if not is_admin():
        print("⚠️ AVISO: Executar este script como Administrador garante a limpeza total do sistema.")
        print("Para melhores resultados, feche e abra o terminal como Administrador.\n")

    clear_temp_folders()
    empty_recycle_bin()
    flush_dns()
    optimize_drives()

    print("\n🎉 Otimização concluída! Registo salvo em 'optimization.log'.")

if __name__ == "__main__":
    main()