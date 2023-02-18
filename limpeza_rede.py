import os
import shutil


lista_proibidos = ['Trabalhista']
pasta_sincronizacao = ['.sync']


def salvar_logs(conteudo):
    with open(os.getcwd() + os.sep + 'log_limpeza_u_dp.txt', 'a') as log:
        print(conteudo, file=log)


def remover_arquivo(arquivo):
    try:
        os.remove(arquivo)
        salvar_logs(f'{arquivo} removido com sucesso')
    except Exception as E:
        salvar_logs(E)


def limpeza_unico_pastas():

    folder_list = []

    os.chdir('U:\\')
    cwd = os.getcwd()

    if os.path.exists('log_limpeza_u_dp.txt'):
        os.remove('log_limpeza_u_dp.txt')

    for i in os.listdir(cwd):
        if os.path.isdir(i) and i in lista_proibidos and i not in pasta_sincronizacao:
            folder_list.append(i)
        elif i in lista_proibidos and i not in pasta_sincronizacao and '.py' not in i:
            remover_arquivo(i)
            pass

    for folder_raiz in folder_list:
        if folder_raiz:
            path2 = cwd + '\\' + folder_raiz
            os.chdir(path2)
            sub_folder_list = [i if os.path.isdir(
                i) else remover_arquivo(i) for i in os.listdir(path2)]

        for subfolder in sub_folder_list:
            if subfolder:
                path3 = path2 + '\\' + subfolder
                os.chdir(path3)
                for folder2 in os.listdir(path3):
                    if folder2:
                        try:
                            if os.path.isfile(folder2):
                                remover_arquivo(folder2)
                            else:
                                shutil.rmtree(folder2)
                        except PermissionError:
                            pass
                        except:
                            pass

    salvar_logs('limpeza efetuada com sucesso!!')


# limpeza_unico_pastas()
