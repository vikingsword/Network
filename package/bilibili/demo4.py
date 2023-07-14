from pywebcopy import save_webpage

url = 'https://www.bilibili.com/read/cv18169456/?from=readlist'
download_folder = '/downloads/'

kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}

save_webpage(url, download_folder, **kwargs)

