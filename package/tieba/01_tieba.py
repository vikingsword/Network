import requests
from bs4 import BeautifulSoup

root_url = 'https://tieba.baidu.com'
count = 0

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Origin": "https://tieba.baidu.com",
    "Cookie": "PSTM=1673437541; BAIDUID=696E2983DEA75CE5A9B79FBCB375DB7E:FG=1; BAIDUID_BFESS=696E2983DEA75CE5A9B79FBCB375DB7E:FG=1; BIDUPSID=A814F33108F52F09B55EA5EC2CB53E7B; BAIDU_WISE_UID=wapp_1673444228611_893; __bid_n=18589bf8365fb8352d4207; arialoadData=false; FPTOKEN=xQUIGudNev70TMR/xQyHKjdHlIo2s3fS40cOnaLIZYbTOLTssjTlcNqd6z1CQqzZFoFXxSytGCX/4IAFyxP/NlE/Qsly6dLBVKCrSdDwkRROYVLB30W8DXnjuLETRbQULAa+SS7WQUzT8u0pUDbTvpZ48CWWK1OFZDA+X2nC8Dwuo83XXPGADu3tHYFhOanCWDXvHuaTeQpDEV3QPbL66sPg5AyN8V8bMHunZYtnvaf85O1YIkRhp1UgpIoKyFNztKHHFDv/LpuMwWmqoqPi4ACEaQyGYv/Nyv8w0NWNr3UrVRjpam1ydBd5NiqRw05DXVreUfyFAezEsAXN85HpItZJQzDbCXJMJRb6e+Kr+mHDOhR/77vXH9MqMQILIJ0Ipo6EpqvJ6KqOOyj7cWGMjg==|LZgUa9GPwNeIw26nJ9M5szG3/tnsMHM5YeJDzrM62eU=|10|0ad0019cf5d51d4589f118ee3487107a; USER_JUMP=-1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1673253320,1673318753,1673444212,1673446486; BAIDU_SSP_lcr=https://www.google.com/; st_key_id=17; H_PS_PSSID=36552_37647_38020_36920_38034_37989_36805_37933_26350_37881; BCLID=12651217624228653656; BCLID_BFESS=12651217624228653656; BDSFRCVID=fm_OJeCT5G09-d6jlutMuvRTMB68_65TTPjcTR5qJ04BtyCVcmiREG0PtqlC9g-M_EGSogKKB2OTHnkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=fm_OJeCT5G09-d6jlutMuvRTMB68_65TTPjcTR5qJ04BtyCVcmiREG0PtqlC9g-M_EGSogKKB2OTHnkF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbIJoDK5JDD3fP36q45HMt00qxby26nj3bn9aJ5nQI5nhKIzb5j8hbL4bqoqQq3uKm5r0Rj_QUbmjRO206oay6O3LlO83h52aC5NKl0MLPbUqqjG-UjYBUL10UnMBMnGteOnanro3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRjj8KjjbBDHRf-b-XKD600PK8Kb7Vbn7Lyfnkbft7jttjqCrbJDQQLxT7b4QCShCR3l703xI73b3B5h3NJ66ZoIbPbPTTSROzMq5pQT8r5-nMJ-JtHmjdKl3Rab3vOp_4XpO1h4PzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjttJnut_KLhf-3bfTrP-trf5DCShUFs24tLB2Q-5M-a3KtBKJ-CM4vhWf405R5nW6JpyTQpafbmLncjSM_GKfC2jMD32tbp5-r0LeTxoUJ2Bb05HPKzXqnpQptebPRi3jj9QgbXBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hIKmD6_bj6oM5pJfetjK2CntsJOOaCv0MM7Oy4oT35L1DauLKT5BaTTGW-5KLfbYHqTsbtQ83h0rMxbnQjQDWJ4J5tbX0MQjDJT-Qft20b0vKtQt5M5uX2Txbb7jWhvIhl72y-TOQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCet60HJRkqoCv5b-0_HRjYbb__-P4DeUjLyMRZ5m7n_l0Mf66fMRc15JOY5JKw3-cGtjvdJJTn-UJ_KMbCMtj_D5OI5bFd3xbLalj43bRTLPjs0KTJKq63QfJ6hP-UyPKHWh37aD3lMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafJOKHICRjjtWeMK; H_BDCLCKID_SF_BFESS=tbIJoDK5JDD3fP36q45HMt00qxby26nj3bn9aJ5nQI5nhKIzb5j8hbL4bqoqQq3uKm5r0Rj_QUbmjRO206oay6O3LlO83h52aC5NKl0MLPbUqqjG-UjYBUL10UnMBMnGteOnanro3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFRjj8KjjbBDHRf-b-XKD600PK8Kb7Vbn7Lyfnkbft7jttjqCrbJDQQLxT7b4QCShCR3l703xI73b3B5h3NJ66ZoIbPbPTTSROzMq5pQT8r5-nMJ-JtHmjdKl3Rab3vOp_4XpO1h4PzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjttJnut_KLhf-3bfTrP-trf5DCShUFs24tLB2Q-5M-a3KtBKJ-CM4vhWf405R5nW6JpyTQpafbmLncjSM_GKfC2jMD32tbp5-r0LeTxoUJ2Bb05HPKzXqnpQptebPRi3jj9QgbXBhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hIKmD6_bj6oM5pJfetjK2CntsJOOaCv0MM7Oy4oT35L1DauLKT5BaTTGW-5KLfbYHqTsbtQ83h0rMxbnQjQDWJ4J5tbX0MQjDJT-Qft20b0vKtQt5M5uX2Txbb7jWhvIhl72y-TOQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCet60HJRkqoCv5b-0_HRjYbb__-P4DeUjLyMRZ5m7n_l0Mf66fMRc15JOY5JKw3-cGtjvdJJTn-UJ_KMbCMtj_D5OI5bFd3xbLalj43bRTLPjs0KTJKq63QfJ6hP-UyPKHWh37aD3lMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafJOKHICRjjtWeMK; BDUSS=c1em5wSlAxMnd2YlpVR1pvQmQ2UDNNNGx6QWhDZ250Zm4zQmt-QmdtaWNYT1pqRVFBQUFBJCQAAAAAAQAAAAEAAAB5ruJpbmllbWFuZGVhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJzPvmOcz75jR0; BDUSS_BFESS=c1em5wSlAxMnd2YlpVR1pvQmQ2UDNNNGx6QWhDZ250Zm4zQmt-QmdtaWNYT1pqRVFBQUFBJCQAAAAAAQAAAAEAAAB5ruJpbmllbWFuZGVhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJzPvmOcz75jR0; STOKEN=271cde4fe7f820dc33c2b47afcf98011f9fede765538ebbb29bebc9bdb40894c; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1673449359; XFI=fdd2c370-91c0-11ed-86c8-bfcb35bb959f; ab_sr=1.0.1_ZmY5YmM3YWE2ZTkxZGViN2Y5MjVkNzUwYzIxN2Y2OTI2YmEzMThhN2RkZmM2MjEyY2JiNjIwYjE4ODYyOTczZmM2MGJmZjkyNmJlMjY3NDcwZDNhNTI3NmFkMDhlOWZmMjhhZWUxZDM5YzRiZWRmZDk3NTNhYTgxMjY0Y2RmNDk4NzNjMWUzN2VhMDA2OTAyNzU4NTlmZmNmM2RhYzM0ODYzZjI0NWU0MWQ4YmQ5N2Q5M2NmOTRmZmVjMGQyNTA1; st_data=3f2027b0636160bb2ac41d646957655e19d53230fed0815725ae29c084a3278b6c06e5ca08772284f9cdde0faddc9d45896ed018d7b3eeb752406a5b6d5dd55c7076ad9a40efac997af177a7176b4c18f35e4a4187a79a3efff622e7a3710c70; st_sign=dbbb773c; XFCS=2A64C37A09A5C2E444F8417BE7F2E90582E8172F6EBB8C33FB16CB666FB1E899; XFT=0jeX5VO559PxwuR/A5fw/en+Kjs+WX56aHGkm9gV/Yc=; tb_as_data=996b5182a7b21949cc81070758a7e0dbef19b871c4b63ea7f6e99f392652987fc434dd556112dc27c7274d4c38f343c37bd0992d5b4648af7e96d66430ccc9200cf8e65c97976bcfd7a167b2ff3c4e481b633992ddb8df02ada605384fba5faaf5c288738f07c3fba877c21766ab16d3; RT=\"z=1&dm=baidu.com&si=fc843b4f-bd0e-4dfd-aaa4-6f4cd689ff1d&ss=lcrph4lp&sl=4a&tt=8id9&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&nu=ubov6bsn&cl=3ajox&ld=3ajfd"
}


# get hot class
def getClass():
    url = 'https://tieba.baidu.com/f/index/forumclass'
    req = requests.get(url=url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    linkList = soup.find_all('a', attrs={'class', 'class-item-title'})
    classList = []
    for i in linkList:
        target = root_url + i['href']
        classList.append(target)
    return classList


# get tieba list from hot class
def getTiebaList(list):
    tiebaList = []
    for i in list:
        req = requests.get(url=i)
        soup = BeautifulSoup(req.text, 'html.parser')
        linkList = soup.find_all('a', attrs={'class', 'ba_href clearfix'})
        for j in linkList:
            url = root_url + j['href']
            tiebaList.append(url)

    return tiebaList


# subscription tieba
# todo : get fid / fname / tbs from script as data to post
def subscription(tiebaList):
    target = 'https://tieba.baidu.com/f/like/commit/add'
    for tieba_url in tiebaList:
        req = requests.post(url=target, headers=headers)
        print(req.status_code)


if __name__ == '__main__':
    classList = getClass()

    tiebaList = getTiebaList(classList)

    subscription(tiebaList)
