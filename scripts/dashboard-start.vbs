Set sh=CreateObject("WScript.Shell")
root=sh.CurrentDirectory
py=root & "\dashboard\.venv\Scripts\python.exe"
app=root & "\dashboard\app\main.py"
cmd="""" & py & """ -m streamlit run """ & app & """ --server.headless=true --server.address=127.0.0.1 --server.port=8501"
sh.Run cmd,0,False
