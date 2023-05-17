import os
import shutil

def copiador(main_path, sec_path, ext):
    contArq = 0
    if os.path.isdir(main_path) and os.path.isdir(sec_path):
        main_path = main_path + '\\'
        sec_path = sec_path + '\\'
        for root,subfolder,filename in os.walk(main_path): #root=diretório base; subfolder=Pastas após o diretório base; filename=Arquivos
            for file in filename:
                if ext in file:
                    contArq = contArq + 1
                    old_path = root + '\\'+ file
                    try:
                        shutil.copy2(old_path, sec_path + file)
                    except:
                        pass

        return contArq
    else:
        return False

if __name__ == '__main__':
    mai = input('Qual a pasta onde se encontram os arquivos? ')
    sec  = input('Qual pasta onde os arquivos devem ser enviados? ')
    ext = input('Digite a extensão: ')
    a = copiador(mai, sec, ext)