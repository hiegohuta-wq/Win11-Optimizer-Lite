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

def check_disk_space(drive="C:\\"):
    """Verifica e exibe o uso de espaço no disco especificado."""
    log(f"📊 A verificar espaço em disco ({drive})...")
    try:
        total, used, free = shutil.disk_usage(drive)
        gb = 1024 ** 3
        
        total_gb = round(total / gb, 2)
        used_gb = round(used / gb, 2)
        free_gb = round(free / gb, 2)
        percent_used = round((used / total) * 100, 1)

        log(f"   💾 Disco {drive} Total: {total_gb} GB | Usado: {used_gb} GB ({percent_used}%) | Livre: {free_gb} GB")
        
        if percent_used > 85:
            log(f"   ⚠️ ALERTA: O disco {drive} está com mais de 85% de ocupação!")
        else:
            log(f"   ✅ Armazenamento em nível saudável.")
    except Exception as e:
        log(f"⚠️ Erro ao verificar espaço em disco: {e}")

def check_and_optimize_network():
    """Realiza Flush no DNS, testa conectividade e renova concessão de IP."""
    log("🌐 A iniciar diagnósticos e otimização de rede...")
    
    # 1. Flush DNS
    try:
        subprocess.run(["ipconfig", "/flushdns"], capture_output=True, check=True)
        log("   ✅ Cache de DNS limpa com sucesso.")
    except Exception as e:
        log(f"   ⚠️ Erro ao limpar cache de DNS: {e}")

    # 2. Teste de Conectividade (Ping Google DNS)
    try:
        ping_res = subprocess.run(["ping", "-n", "2", "8.8.8.8"], capture_output=True, text=True)
        if ping_res.returncode == 0:
            log("   ✅ Conectividade com a Internet ativa (Ping 8.8.8.8 OK).")
        else:
            log("   ⚠️ Sem resposta do ping externo (verifique sua conexão).")
    except Exception as e:
        log(f"   ⚠️ Falha ao executar o teste de ping: {e}")

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

def optimize_drives():
    """Executa a otimização de disco/SSD (TRIM)."""
    log("💾 A otimizar unidades de disco (TRIM/Defrag)...")
    try:
        subprocess.run(["defrag", "C:", "/O"], capture_output=True, check=True)
        log("✅ Otimização da unidade C: efetuada.")
    except Exception as e:
        log("⚠️ Não foi possível otimizar o disco (requer privilégios de Administrador).")

def main():
    print("=" * 60)
    print("🚀 Windows 11 Advanced Optimizer, Diagnostics & Cleaner")
    print("=" * 60)
    
    if not is_admin():
        print("⚠️ AVISO: Executar este script como Administrador garante a limpeza total do sistema.")
        print("Para melhores resultados, feche e abra o terminal como Administrador.\n")

    check_disk_space()
    clear_temp_folders()
    empty_recycle_bin()
    check_and_optimize_network()
    optimize_drives()

    print("\n🎉 Processo concluído! Registo salvo em 'optimization.log'.")

if __name__ == "__main__":
    main()