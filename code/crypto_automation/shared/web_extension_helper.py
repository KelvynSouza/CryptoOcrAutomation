import requests
def update_extension(extension_path, url_download_path):
    #para trocar a extensão, foque na informações no final da string, o x=id%, apois isso é o id da pagina da extensão do chrome
    r = requests.get(url_download_path, allow_redirects=True)
    open(extension_path, 'wb').write(r.content)