import cx_Freeze
executables= [cx_Freeze.Executable("C:/Users/Your_PC_Name_here/PycharmProjects/game1/AIGAME.py")]
cx_Freeze.setup(
    name="The interrupting snake",
    options={"build.exe": {"packages":["pygame","numpy","random"],
                          "include_files":["C:/Users/Your_PC_Name_here/Desktop/snakegame.bmp","C:/Users/Your_PC_Name/Desktop/Game-Menu_Looping.mp3"]}},
    executables = executables
)