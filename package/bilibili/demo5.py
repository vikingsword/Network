from pywebcopy import save_website
save_website(
    url='https://www.bilibili.com/read/cv18169456/?from=readlist',
    project_folder="E://Dev//Python//Project//Network//package//bilibili",
    project_name="my_site",
    bypass_robots=True,
    debug=True,
    open_in_browser=True,
    delay=None,
    threaded=False,
)