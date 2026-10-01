README.md
🛠️ Funcionalidades
📊 Auditoria de Espaço em Disco: Verifica a capacidade total, espaço utilizado e livre da unidade C:, emitindo alerta se o uso ultrapassar 85%.

🧹 Limpeza de Temporários: Remove ficheiros desnecessários das pastas %TEMP% e C:\Windows\Temp.

🗑️ Esvaziamento da Reciclagem: Força a limpeza da reciclagem do sistema via PowerShell.

🌐 Diagnóstico e Otimização de Rede:

Limpeza da cache de DNS (ipconfig /flushdns).

Teste de conectividade e resposta ICMP via Ping para DNS público (8.8.8.8).

💾 Otimização de Unidade (TRIM): Executa otimização de disco/SSD via comando defrag.

📝 Registro de Logs: Salva automaticamente o histórico completo de ações com timestamp no arquivo optimization.log.

🔧 Como Executar
Pré-requisitos
Python 3.x instalado no Windows.

Recomendado executar o terminal como Administrador para permitir a execução total das rotinas do sistema.

Passo a passo
Abra o PowerShell ou Prompt de Comando como Administrador.

Navegue até à pasta do projeto:

PowerShell
cd C:\Users\HIEGO\Win11-Optimizer-Lite
Executar o script:

PowerShell
python optimizer.py
📄 Exemplo de Saída
texto simples
============================================================
🚀 Windows 11 Advanced Optimizer, Diagnostics & Cleaner
============================================================
[2026-10-01 00:19:35] 📊 A verificar espaço em disco (C:\)...
[2026-10-01 00:19:35]    💾 Disco C:\ Total: 110.94 GB | Usado: 98.25 GB (88.6%) | Livre: 12.69 GB
[2026-10-01 00:19:35]    ⚠️ ALERTA: O disco C:\ está com mais de 85% de ocupação!
[2026-10-01 00:19:35] 🧹 A iniciar limpeza de ficheiros temporários...
[2026-10-01 00:19:35] ✅ Limpeza concluída! Liberados aproximadamente 0.0 MB.
[2026-10-01 00:19:35] 🗑️ A esvaziar a Reciclagem...
[2026-10-01 00:19:36] ✅ Reciclagem esvaziada com sucesso.
[2026-10-01 00:19:36] 🌐 A iniciar diagnósticos e otimização de rede...
[2026-10-01 00:19:36]    ✅ Cache de DNS limpa com sucesso.
[2026-10-01 00:19:37]    ✅ Conectividade com a Internet ativa (Ping 8.8.8.8 OK).
[2026-10-01 00:19:37] 💾 A otimizar unidades de disco (TRIM/Defrag)...
[2026-10-01 00:19:37] ✅ Otimização da unidade C: efetuada.

🎉 Processo concluído! Registo salvo em 'optimization.log'.
📄 Licença
Este projeto está sob a licença do MIT. Fique à vontade para usar e aprimorar!